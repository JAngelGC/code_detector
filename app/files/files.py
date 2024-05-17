import os

def get_absolute_file_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_paths = []
    for file in os.listdir(script_dir):
        absolute_path = os.path.abspath(os.path.join(script_dir, file))
        if os.path.isfile(absolute_path) and file.startswith('file_'):
            absolute_paths.append(absolute_path)
    
    return absolute_paths