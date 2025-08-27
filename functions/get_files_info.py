import os
from google.genai import types

def get_files_info(working_directory: str, directory: str =".") -> str:
    try:
        full_path: str = os.path.join(working_directory, directory)

        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        contents: list[str] = []

        for content in os.listdir(full_path):
            content_path: str = os.path.join(full_path, content)
            contents.append(f"- {content}: file_size={os.path.getsize(content_path)}, is_dir={os.path.isdir(content_path)}")


        return "\n".join(contents)
    except Exception as e:
        return f"Error: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)