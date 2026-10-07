import requests                # HTTP requests/API calls ke liye
from google import genai        # Google Gemini API ke liye
from openai import OpenAI       # OpenAI API client ke liye

import genai_1                  # Configuration variables import karne ke liye


def ask_openai(message):
    """Send one message to OpenAI and return the answer as text."""

    # OpenAI client create karta hai using API key from genai_1.py
    client = OpenAI(api_key=genai_1.OPENAI_API_KEY)

    # OpenAI Responses API ko request bhejta hai
    response = client.responses.create(
        model=genai_1.OPENAI_MODEL,          # OpenAI model select karta hai
        instructions=genai_1.SYSTEM_PROMPT,  # System instruction deta hai
        input=message                         # User ka message/prompt
    )

    # API response se generated text return karta hai
    return response.output_text

def ask_gemini(message):
    """
    Send one message to Google Gemini
    and return the generated answer as text.
    """

    # Gemini client create karta hai using API key
    # jo genai_1.py se aa rahi hai
    client = genai.Client(
        api_key=genai_1.GEMINI_API_KEY
    )

    # Gemini API ko text generation request bhejta hai
    response = client.models.generate_content(
        model=genai_1.GEMINI_MODEL,              # Gemini model select karta hai
        contents=message,                         # User ka message/prompt
        config={
            "system_instruction": genai_1.SYSTEM_PROMPT  # AI ke liye system instruction
        },
    )

    # Response se generated text return karta hai
    return response.text

def ask_ollama(message):
    """
    Send one message to a model running locally in Ollama
    and return the generated answer as text.
    """

    # Ollama local machine par run hota hai,
    # isliye API key ki zarurat nahi hoti.
    try:
        # Ollama ke local HTTP API ko POST request bhejte hain
        response = requests.post(
            genai_1.OLLAMA_BASE_URL + "/api/chat",

            # Request body ko JSON format mein send karte hain
            json={
                # Kaunsa Ollama model use karna hai
                "model": genai_1.OLLAMA_MODEL,

                # System instruction aur user message
                "messages": [
                    {
                        "role": "system",
                        "content": genai_1.SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": message
                    },
                ],

                # Complete response ek saath chahiye
                "stream": False,
            },

            # Maximum 120 seconds tak response ka wait
            timeout=120,
        )

    # Agar Ollama server se connection nahi ho paya
    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Could not reach Ollama at "
            + genai_1.OLLAMA_BASE_URL
            + ". Is Ollama running?"
        )

    # HTTP error hone par exception raise karta hai
    response.raise_for_status()

    # JSON response se generated message ka content return karta hai
    return response.json()["message"]["content"]

