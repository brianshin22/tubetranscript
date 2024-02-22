import streamlit as st
import whisper
import os
# from openai import OpenAI
from pytube import YouTube

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.placeholder = "Enter Youtube URL"

# video_folder = "/home/brian/projects/whisper/"
yt = None

st.title("Youtube Video Transcriber")
st.caption("A tool by Brian Shin. [brianshin.me](https://brianshin.me)")

# st.sidebar.header("Translation Section")
st.divider()
#audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])


# process_button = st.sidebar.button("Translate audio")
# st.sidebar.markdown("**Note**: Processing can take up to 5 mins, please be patient.")
with st.container():
    col1, col2 = st.columns([6,2])
    with col2:
        process_button = st.button("Transcribe video")
    with col1: 
        url = st.text_input("Enter Youtube URL below", "", label_visibility="collapsed", placeholder="Enter Youtube URL")
    # with col3:
        # translate_button = st.button("Translate video")


st.divider()



model = whisper.load_model("base")

if process_button:
    st.header("Video")
    video_container = st.container()

    st.divider()
    # st.header("Transcription")
    transcript_container = st.container()
    transcript_container.header("Transcript")
    status_placeholder = transcript_container.empty()
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
    status_placeholder.info("Transcribing video...")
    stream = yt.streams.get_by_itag(140)
    # audio_file = stream.download(video_folder)
    audio_file = stream.download()
    print(audio_file)
    if audio_file is not None:
        #filepath = "/home/brian/Downloads/" + audio_file.name
        filepath = audio_file
        result = model.transcribe(filepath)

        transcript = result['text']
        from helper import format_transcript
        formatted_transcript = format_transcript(transcript)
        
        print(formatted_transcript)

        transcript_container.markdown(formatted_transcript)
        status_placeholder.empty()
        status_placeholder.success("Finished transcribing video")
    else:
        st.error("Please enter a valid URL")


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