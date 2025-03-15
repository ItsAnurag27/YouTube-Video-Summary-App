#importing packages
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

# Load environment variables
load_dotenv()

# Google API Key Configuration
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for Gemini-2.0-flash
prompt = "You are a YouTube video summarizer. "

# Function to extract video ID from URL
def extract_video_id(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        return parse_qs(parsed_url.query).get('v', [None])[0]
    elif parsed_url.hostname in ['youtu.be']:
        return parsed_url.path[1:]
    return None

# Function to fetch YouTube transcript
def extract_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([i["text"] for i in transcript])
        return transcript_text
    except Exception as e:
        st.error("Could not fetch the transcript. Video might be private or restricted.")
        return None

# Function to generate summary from Gemini API
def generate_summary(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit UI
st.title("🎯 YouTube Video Summary App")
youtube_url = st.text_input("📌 Enter YouTube Video Link:")

if youtube_url:
    video_id = extract_video_id(youtube_url)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    else:
        st.error("Invalid YouTube URL. Please try again.")

#button
if st.button("✨ Generate Summary"):
    if video_id:
        transcript = extract_transcript(video_id)
        if transcript:
            summary = generate_summary(transcript, prompt)
            st.markdown("## ✅ Detailed Summary:")
            st.write(summary)
