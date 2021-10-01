import os
import zipfile

__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

current_path = os.getcwd()
cache_path_folder = os.path.join(current_path(), "cache")
zip_path_folder = os.path.join(current_path, "files", "data.zip")

def clean_cache():
    # Check if folder "cache" exist
    if os.path.isdir(cache_path_folder):
        for files in os.listdir(cache_path_folder):
            # Remove all files in folder
            os.remove(os.path.join(cache_path_folder, files))
    else:
        # Create folder "cache"
        os.mkdir(cache_path_folder)

def cache_zip(zip_file_folder, cache_path_folder):
    data_zip = zipfile.ZipFile(zip_file_folder, "r")
    data_zip.extractall(path=cache_path_folder)
    return

def cached_files():
    file_list = []
    for entry in os.listdir(cache_path_folder):
        entry_path = os.path.join(cache_path_folder, entry)
        if os.path.isfile(entry_path):
            file_list.append(entry_path)
    return file_list

def find_password(file_list):
    for file in file_list:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    password = line[line.find(" ") +1:-1]
                    return password
    else:
        "Password not found"


if __name__ == '__main__':
    print ("The current working folder is %s" % current_path)
    clean_cache()
    cache_zip("data.zip", "cache")
    cached_files()
    print(find_password(cached_files()))