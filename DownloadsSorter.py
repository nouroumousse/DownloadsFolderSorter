import os
import shutil

download_folder = "/Users/nouroumousse/Downloads"

# create a dictionary to map file extensions to their corresponding folders
file_extensions = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".HEIC": "Images",
    ".heic": "Images",
    ".avif": "Images",
    ".webp": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".mkv": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".m3u": "Documents",
    ".ics": "Documents",
    ".txt": "Text",
    ".py": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".h": "Code",
    ".jar": "Code",
    ".html": "Web",
    ".css": "Web",
    ".js": "Web",
    ".json": "Web",
    ".xml": "Web",
    ".exe": "Executables",
    ".msi": "Executables",
    ".app": "Executables",
    ".dmg": "Executables",
    ".eml": "Mail",
    ".ttf": "Fonts",
    ".zip": "Zip files",
    ".rar": "Zip files",
    ".torrent": "Torrents",
    ".ai": "Design files",
    ".aep": "Design files",
    ".blend": "Design files",
    ".blend1": "Design files",
    ".eps": "Design files",
    ".fig": "Design files",
    ".psd": "Design files",
    ".obj": "Design files",

}

# create the folders if they don't exist
for folder in set(file_extensions.values()):
    folder_path = os.path.join(download_folder, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# sort the files
for filename in os.listdir(download_folder):
    filepath = os.path.join(download_folder, filename)
    if os.path.isfile(filepath):
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension in file_extensions:
            folder = file_extensions[file_extension]
            folder_path = os.path.join(download_folder, folder)
            new_filepath = os.path.join(folder_path, filename)
            if os.path.exists(new_filepath):
                # if the file already exists in the destination folder, add a number to the end of the filename
                name, ext = os.path.splitext(filename)
                i = 1
                while os.path.exists(os.path.join(folder_path, f"{name} ({i}){ext}")):
                    i += 1
                new_filepath = os.path.join(folder_path, f"{name} ({i}){ext}")
            shutil.copy2(filepath, new_filepath)
            os.remove(filepath)
