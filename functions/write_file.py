import os

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:
        wd_absoulte_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(wd_absoulte_path, file_path)) 
    
        if os.path.commonpath([wd_absoulte_path, target_path]) != wd_absoulte_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        #check is dir exists with exist_ok, if it doesnt create a dir
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        with open(target_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
        
    except Exception as e:
         return f"Error: {e}" 
               
      