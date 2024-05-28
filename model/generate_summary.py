import google.generativeai as genai
import dotenv
import os
dotenv.load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

summary_prompt = """You are a youtube video summarizer. You are given a youtube video transcript and you need to summarize the whole video in about a 250 words summary. The summary should be concise and should cover all the important points of the video. You can use the following transcript to generate the summary: \n"""

def generate_summary(transcript):
    response = model.generate_content(summary_prompt + transcript)
    return response.parts[0].text