
import os 

  
def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    try:
        
        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'
        
        wd_absoulte_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(wd_absoulte_path, directory))
        
        # Will be True or False as finds the longest sub-path shared by two paths
        valid_target_dir = os.path.commonpath([wd_absoulte_path, full_path]) == wd_absoulte_path
        
        print(valid_target_dir)
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
        return f'Success: "{directory}" is within the working directory'   
    
    except Exception as e:
         return f"Error encountered: {e}" 
    