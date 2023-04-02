# Back-End

This bit of code is what reaches out to the OpenAI API, and retrieves a response.

## How to run this

This is an AWS Lambda function. I don't have a local version of it working. However, if you ask Chat-GPT to help you get it running locally, it can probably assist (ha!).


To keep everything super simple, the same schema is used for input and output.

```json
{
    "conversation_id": "<uuid>",
    "content": "<message>"
}
```

To package this up as a .zip to upload to Lambda, use `docker-compose up`. Then upload `target/function.zip`.

## Musings

This uses the GPT-4 model, which is much more sensitive than the 3.5 model to the "system" prompt. That's what makes this possible.

I used AWS's Secrets Manager to store the secret key. It was surprisingly simple to set up.

Once this Lambda was created, I just created an API Gateway API resource to trigger it.

