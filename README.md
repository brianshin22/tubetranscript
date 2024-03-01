# Tube Transcript
Streamlit web application to transcribe Youtube videos and display them, in any language.

## Sample Youtube Videos
https://www.youtube.com/watch?v=ftlHMGkCODY
https://www.youtube.com/watch?v=ZzDXSlnOGko

## Notes
When running the Docker container, make sure to specify your OPENAI_API_KEY:
'''
docker run -p 8080:8080 -e OPENAI_API_KEY=your_api_key tubetranscribe
'''

## Copyright
ByungHyun Shin

## LICENSE
CC-by-NC 4.0

### Resources
https://github.com/entbappy/Streamlit-app-Docker-Image
https://www.youtube.com/watch?v=DflWqmppOAg
https://github.com/upendrak/streamlit-aws-tutorial
https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker
https://hackernoon.com/using-openais-whisper-and-gpt-3-api-to-build-and-deploy-a-transcriber-app-part-1
https://hackernoon.com/using-openais-whisper-and-gpt-3-api-to-build-and-deploy-a-transcriber-app-part-2
https://platform.openai.com/docs/guides/speech-to-text/prompting
https://github.com/sanchit-gandhi/whisper-jax?tab=readme-ov-file
https://www.reddit.com/r/MachineLearning/comments/14xxg6i/d_what_is_the_most_efficient_version_of_openai/