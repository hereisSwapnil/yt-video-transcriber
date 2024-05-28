import streamlit as st
from utils.transcribe import transcribe_video, get_video_id, get_transcript_text
from model.generate_summary import generate_summary

def transcribe_call(video_url):
    global transcribed_text
    video_url_ = get_video_id(video_url)
    transcribed_data = transcribe_video(video_url_)
    if(transcribed_data == "No transcribe found"):
        return "Could not Summarize this video for you. But feel free to give it a another try 😇"
    transcript_text = get_transcript_text(transcribed_data)
    summary = generate_summary(transcript_text)
    return summary

st.title('▶️ Youtube Video Transcriber')

video_url = st.text_input('Enter the URL of the Youtube Video')

if video_url:
    st.image(f'https://i.ytimg.com/vi/{get_video_id(video_url)}/hqdefault.jpg')

    if st.button('Summarize'):
        with st.spinner('Transcribing and summarizing the video...'):
            transcribed_text = transcribe_call(video_url)
            st.write(transcribed_text)
