# Voice Assistant with NLP and Speech Recognition

## Overview

This is a voice-controlled assistant built using Python that can recognize speech and execute tasks based on voice commands. It integrates Natural Language Processing (NLP) for understanding commands, and utilizes speech recognition and OpenAI GPT for intelligent responses.

The assistant can be used for various tasks like answering questions, searching the web, setting reminders, or performing simple commands.

## Features

- **Speech-to-Text**: Convert spoken words into text using Google's Speech Recognition API.
- **Natural Language Processing (NLP)**: Understand user intent and respond accordingly using OpenAI GPT (via the OpenAI API).
- **Basic Commands**: Perform tasks such as answering questions, providing weather updates, or performing simple web searches.
- **Voice Feedback**: The assistant responds to the user with synthesized speech.

## Technologies Used

- **Speech Recognition**: Converts speech to text using Google's Speech-to-Text API.
- **OpenAI GPT**: Uses OpenAI's GPT model to understand and respond to user queries.
- **Python Libraries**: 
  - `speech_recognition` for speech recognition
  - `pyttsx3` for text-to-speech functionality
  - `openai` for interaction with the OpenAI API

## Requirements

- Python 3.x
- Required Python libraries (installed via `pip`):
  - `speech_recognition`
  - `pyttsx3`
  - `openai`
  - `python-dotenv`
  - `requests`

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
