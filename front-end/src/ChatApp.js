import React, { useState, useEffect } from "react";
import { styled } from "@mui/material/styles";
import { Box, Button, TextField } from "@mui/material";
import { Send } from "@mui/icons-material";
import { v4 as uuidv4 } from "uuid";

const Container = styled(Box)({
  display: "flex",
  flexDirection: "column",
  height: "100vh",
  backgroundColor: "#1E1E1E",
});

const ChatBox = styled(Box)({
  flexGrow: 1,
  overflow: "auto",
  padding: "1rem",
});

const MessageContainer = styled(Box)(({ sentByUser }) => ({
  display: "flex",
  justifyContent: sentByUser ? "flex-end" : "flex-start",
}));

const Message = styled(Box)(({ sentByUser, botMessage }) => ({
  maxWidth: "70%",
  margin: "0.5rem",
  padding: "0.5rem",
  borderRadius: "0.5rem",
  color: "#FFF",
  backgroundColor: sentByUser ? "#388E3C" : "#0D47A1",
  alignSelf: sentByUser ? "flex-end" : "flex-start",
  order: botMessage ? 0 : 1,
}));

const ChatApp = () => {
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState([]);
  // When the app loads, create a conversation_id which is a UUID, and store it in a cookie.
  const [conversationId, setConversationId] = useState("");
  useEffect(() => {
    const uuid = uuidv4();
    setConversationId(uuid);
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    const updatedMessages = [
      ...messages,
      { content: inputValue, role: "user" },
    ];
    setMessages(updatedMessages);
    setInputValue("");
    await fetch(
        "https://4yjvws6jd7.execute-api.us-east-2.amazonaws.com/default/ChatLambda",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                conversation_id: conversationId,
                content: inputValue,
            }),
            }
        )
        .then((response) => response.json())
        .then((response) => {
          setMessages([
            ...updatedMessages,
            response,
          ]);
        })
        .catch((error) => {
          setMessages([
            ...updatedMessages,
            {
              content:
                "Oops! Something went wrong. Please try again later.",
              role: "assistant",
            },
          ]);
        });
    setIsLoading(false);
  };
  

  return (
    <Container>
      <ChatBox>
        {messages.map((message, index) => (
          <MessageContainer
          key={index}
          sentByUser={message.role === "user"}
          >
            <Message
              key={index}
              sentByUser={message.role === "user"}
              botMessage={message.role === "assistant"}
            >
              {message.content}
            </Message>
          </MessageContainer>
        ))}
      </ChatBox>
      <form onSubmit={handleSubmit}>
        <Box display="flex" alignItems="center" padding="1rem">
          <TextField
            label="Type your message"
            variant="filled"
            size="small"
            fullWidth
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            style={{ marginRight: "1rem"}}
          />
          <Button
            variant="contained"
            color="primary"
            disabled={!inputValue || isLoading}
            type="submit"
            endIcon={<Send />}
          >
            Send
          </Button>
        </Box>
      </form>
    </Container>
  );
};

export default ChatApp;
