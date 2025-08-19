import os
from functions.config import FILE_CHAR_LIMIT

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        full_path: str = os.path.join(working_directory, file_path)

        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_path, "r") as f:
            file_content_string: str = f.read(FILE_CHAR_LIMIT)

        if os.path.getsize(full_path) > 10000:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'


        return file_content_string
    except Exception as e:
        return f"Error: {e}"
    
