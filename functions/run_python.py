import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args=[]):
    try:
        full_path: str = os.path.join(working_directory, file_path)

        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'
        
        if not full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        args.insert(0, file_path)
        args.insert(0, "python3")
        completed = subprocess.run(args=args, timeout=30, capture_output=True, cwd=os.path.abspath(working_directory))
        
        if not completed.stdout:
            return "No output produced."
        
        result: list[str] = []
        result.append(f"STDOUT: {completed.stdout}")
        result.append(f"STDERR: {completed.stderr}")
        if completed.returncode != 0:
            result.append(f"Process exited with code {completed.returncode}")

        return "\n".join(result)
        

    except Exception as e:
        return f"Error: executing Python file: {e}"