import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types





def main():
    print("Hello from aiagent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    if len(sys.argv) > 1:
        prompt: str = sys.argv[1]
    else:
        print("No prompt given :(")
        sys.exit(1)

    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    #some wacky ai stuff here
    content = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    metadata = content.usage_metadata
    if "--verbose" in sys.argv:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")
    print(f"Response: {content.text}")


if __name__ == "__main__":
    main()
