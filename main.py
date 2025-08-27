import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import schema_get_files_info


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
    model_name: str = "gemini-2.0-flash-001"
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
    )
    system_prompt: str = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
        ),
    )

    metadata = response.usage_metadata
    if "--verbose" in sys.argv:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")
    if response.function_calls:
        for fc in response.function_calls:
            print(f"Calling function: {fc.name}({fc.args})\n")
    else:
        print(f"Response: {response.text}")


if __name__ == "__main__":
    main()
