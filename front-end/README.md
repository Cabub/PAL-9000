# Front-End

This portion of the code is responsible for displaying the chat messages on the screen and taking user input.

## How to run this

First, install the dependencies `npm install`.

To run the local server, use `npm start`. This will start the local dev server so you can look at the project while you hack away at it.

To make a production build, use `npm build`.

The live version of this lives in AWS Cloudfront. 

To deploy this, dump all the files from the build folder into an S3 bucket, make sure your Cloudfront distrobution can reach them, and you should be golden.

## Musings

I basically made regular old Chat-GPT write this whole thing.

I'm not a fan of messing with CSS for hours to get things just so. I made it look "good enough" and that's "good enough" for my little April Fools' day project.

Essentially all this does is call the API and print the result on the screen. There's no fancy logic going on here.

It's also not very clean. I may spend some time cleaning this up as an exercise in futility, but given the expected lifespan of this project, I doubt I have the time.

