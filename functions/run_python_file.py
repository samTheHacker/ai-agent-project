import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    
    try:
        wd_absoulte_path = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(wd_absoulte_path, file_path)) 
        
        if os.path.commonpath([wd_absoulte_path, abs_file_path]) != wd_absoulte_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", abs_file_path]
        
        if args:
            command.extend(args)
        
        #run subprocess with commands    
        CompletedProcess = subprocess.run(command, capture_output=True, text=True, timeout=30)      
        
        if CompletedProcess.returncode != 0:
            return f"Process exited with code {CompletedProcess.returncode}"
        
        if not CompletedProcess.stdout and CompletedProcess.stderr:
            return f"No output produced"
        else:
            return f"STDOUT: {CompletedProcess.stdout} \n STDERR: {CompletedProcess.stderr}"
        
        
    except Exception as e:
         return f"Error: executing Python file: {e}"