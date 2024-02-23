import os

import streamlit as st
# import whisper
from pytube import YouTube

from openai import OpenAI

from helper import format_transcript

system_prompt = "You are a helpful assistant. Your task is to add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."

def generate_corrected_transcript(temperature, system_prompt, raw_transcript):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": raw_transcript
            }
        ]
    )
    return response.choices[0].message.content

# openai_api_key = osenviron.get('OPENAI_API_KEY')

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.placeholder = "Enter Youtube URL"

st.title("Youtube Video Transcriber")
st.caption("A tool by Brian Shin. [brianshin.me](https://brianshin.me)")

st.divider()

with st.container():
    col1, col2 = st.columns([6,2])
    with col2:
        process_button = st.button("Transcribe video")
    with col1: 
        url = st.text_input("Enter Youtube URL below", "", label_visibility="collapsed", placeholder="Enter Youtube URL")


st.divider()

# model = whisper.load_model("base")
client = OpenAI()

if process_button:
    st.header("Video")
    video_container = st.container()

    st.divider()
    # st.header("Transcription")
    transcript_container = st.container()
    transcript_container.header("Transcript")
    # client = OpenAI()
    # task = "Translate the following from Korean to English: "
    transcript_container.empty()

    if not url.startswith("http"):
        st.text("Please enter a valid URL")
        st.stop()
    yt = YouTube(url)
    print(yt)
    video_length = yt.length

    # check video length for less than 10 minutes, current Whisper max
    if video_length > 599:
        video_container.error("Please choose a video shorter than 10 minutes.")
        st.stop()
    video_container.video(url)
    with st.spinner("Transcribing video..."):
        stream = yt.streams.get_by_itag(140)
        # audio_file = stream.download(video_folder)
        audio_file = stream.download()
        print(audio_file)
        if audio_file is not None:
            #filepath = "/home/brian/Downloads/" + audio_file.name
            filepath = audio_file
            file = open(audio_file, "rb")
            # result = model.transcribe(filepath)
            result = client.audio.transcriptions.create(
                model="whisper-1",
                file=file,
                response_format="text"
            )

            # transcript = result['text']
            transcript = result
            print("Original transcript: " + transcript)
            transcript_punctuated = generate_corrected_transcript(0, system_prompt, transcript)
            print("Punctuated transcript: " + transcript_punctuated)
            # format with newlines for easier viewing
            # formatted_transcript = format_transcript(transcript)
            formatted_transcript2 = format_transcript(transcript_punctuated)
            # print(formatted_transcript)
            # print(formatted_transcript2)

            transcript_container.markdown(formatted_transcript2)



    # else:
    #     st.error("Please enter a valid URL")


# if translate_button:
#     if not url.startswith("http"):
#         st.text("Please enter a valid URL")
#         st.stop()
#     if yt is None:
#         translate_container.error("Please transcribe video first")
#         st.stop()
#     translate_container.header("Translation")
#     translate_container.info("Translating text...")
    
#     client = OpenAI()
#     task = "Translate the following to English: "
#     prompt = task + transcription

#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt,
#             }
#         ],
#         model="gpt-3.5-turbo",
#     )
#     st.markdown(chat_completion.choices[0].message.content)
#     st.sidebar.success("Translation complete")