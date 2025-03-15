
## 🎯 YouTube Video Summary App

📌 Project Description

The YouTube Video Summary App is a Streamlit-based web application that extracts the transcript of a YouTube video and generates a concise summary using the Google Gemini API. The app is designed to help users quickly understand the key points of a video without watching the entire content.


## 🛠️ Tech Stack

- Python (Backend logic)

- Streamlit (UI Framework)

- Google Generative AI (Gemini API) (For content generation)

- YouTube Transcript API (For fetching the transcript)

## 📋 Prerequisites

- Python 3.x installed

- Google Gemini API Key


## 🔑 Google Gemini API Key Setup

- Visit the Google AI Studio.

- Sign in with your Google account.

- Navigate to API Keys section.

- Generate a new API Key.

- Copy the key for later use.


## 📂 Installation

1.Clone the repository

```bash
  https://github.com/ItsAnurag27/YouTube-Video-Summary-App.git
```

2.Navigate to the project directory:
```bash
cd youtube-summary-app
```
3.Install the dependencies:
```bash
pip install -r requirements.txt
```
4.Create a .env file in the root directory and add your Google API Key:
```bash
GOOGLE_API_KEY=your_api_key_here
```
5.Run the Application
```bash
streamlit run app.py
```
## 🚀 Features

 
- Extracts transcript from any YouTube video.

- Generates a detailed summary in bullet points within 250 words.

- Simple and user-friendly Streamlit UI.

- Handles errors for private or restricted videos.


## 📌 Usage

- Enter the YouTube video URL.

- Click on the Generate Summary button.

- View the detailed summary in bullet points.

## 🛑 Error Handling

- Invalid YouTube URLs are handled with an error message.

- Private or restricted videos are also managed with proper alerts.

## 📚 Dependencies

- Streamlit

- Python-dotenv

- Google Generative AI SDK

- YouTube Transcript API

## ✅ Future Scope

- Support for multi-language transcription.

- Additional summarization models.

- Exporting summaries as PDF or text files.


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anurag-gupta-92962019b/)
