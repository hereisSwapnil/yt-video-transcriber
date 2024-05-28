from youtube_transcript_api import YouTubeTranscriptApi

def transcribe_video(video_id):
    try:
        transcribed_data = YouTubeTranscriptApi.get_transcript(video_id)
        return transcribed_data
    except:
        return "No transcribe found"

def get_video_id(video_url):
    video_id = video_url.split("v=")[1].split("&")[0]
    return video_id

def get_transcript_text(transcribed_data):
    transcript = ""
    for i in transcribed_data:
        transcript += " " + i['text']
    return transcript