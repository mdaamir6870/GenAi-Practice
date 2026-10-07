import genai_1
from genai_provider import ask_gemini, ask_ollama, ask_openai
HELP = """
Commands:
  /help   Show this help
  /exit   Quit the chatbot (you can also type: exit)
"""
def model_name():
    """The model name of the provider that was chosen in .env."""
    if genai_1.PROVIDER == "openai":
        return genai_1.OPENAI_MODEL
    if genai_1.PROVIDER == "gemini":
        return genai_1.GEMINI_MODEL
    if genai_1.PROVIDER == "ollama":
        return genai_1.OLLAMA_MODEL

def check_setup():
    """Return a helpful message if something is missing in .env, otherwise None."""
    if genai_1.PROVIDER not in ("openai", "gemini", "ollama"):
        return (
            "LLM_PROVIDER is '" + genai_1.PROVIDER + "'.\n"
            "Please set LLM_PROVIDER to openai, gemini or ollama in the .env file."
        )
    if genai_1.PROVIDER == "openai" and not genai_1.OPENAI_API_KEY:
        return "OPENAI_API_KEY is missing.\nPlease add your OpenAI API key to the .env file."
    if genai_1.PROVIDER == "gemini" and not genai_1.GEMINI_API_KEY:
        return "GEMINI_API_KEY is missing.\nPlease add your Gemini API key to the .env file."
    if not model_name():
        return (
            "The model name for " + genai_1.PROVIDER + " is missing.\n"
            "Please set " + genai_1.PROVIDER.upper() + "_MODEL in the .env file."
        )

def ask_llm(message):
    """Send the message to whichever provider was chosen in .env."""
    if genai_1.PROVIDER == "openai":
        return ask_openai(message)
    elif genai_1.PROVIDER == "gemini":
        return ask_gemini(message)
    else:
        return ask_ollama(message)

def main():
    problem = check_setup()
    if problem:
        print("Error:", problem)
        return

    print("=" * 40)
    print("      Simple GenAI CLI Chatbot")
    print("=" * 40)
    print("\nProvider:", genai_1.PROVIDER)
    print("Model:", model_name())
    print("Type /help for commands.")

    while True:
        message = input("\nYou: ").strip()

        if message in ("exit", "/exit"):
            print("\nGoodbye!")
            break

        if message == "/help":
            print(HELP)
            continue

        if not message:
            continue

        try:
            print("\nAssistant:", ask_llm(message))
        except Exception as error:
            print("\nSorry, the request failed:", error)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
