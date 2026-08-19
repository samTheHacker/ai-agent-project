
import os 

  
def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    try:
        files_info: list[str] = []
        wd_absoulte_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(wd_absoulte_path, directory))
            

        # Will be True or False as finds the longest sub-path shared by two paths
        
        if os.path.commonpath([wd_absoulte_path, target_path]) != wd_absoulte_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            
        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'
        
        for filename in os.listdir(target_path):
            filepath = os.path.join(target_path, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )      
               
        return "\n".join(files_info)
    
    except Exception as e:
         return f"Error: {e}" 
    
    
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
    