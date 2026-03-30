import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent

client=google.cloud.logging.Client()
client.setup_logging()

load_dotenv()

# Get model from .env (e.g., gemini-2.5-flash)
model_name = os.getenv("MODEL")

# --- Define the Summarizer Agent ---
summarizer = Agent(
    name="Summarizer",
    model=model_name,
    instruction="""
    You are a professional text summarizer. 
    Your task is to take the provided text and return:
    1. A one-line summary of the text.
    2. A bulleted list of the top 3 key takeaways.
    """
)

# Deployment entry point for Cloud Run
root_agent = summarizer