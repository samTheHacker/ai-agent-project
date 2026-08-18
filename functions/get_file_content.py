import os
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    
    try:
        wd_absoulte_path = os.path.abspath(working_directory)
        
        target_path = os.path.normpath(os.path.join(wd_absoulte_path, file_path)) 
        
        if os.path.commonpath([wd_absoulte_path, target_path]) != wd_absoulte_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        file_content_string: str = ""
        
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            
             # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                
            return file_content_string
             
    except Exception as e:
         return f"Error: {e}" 