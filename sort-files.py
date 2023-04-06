import os

# Defines the working directory being used
parent_directory = os.getcwd()

# All folder names
image_dir = "Image folder"
txt_dir = "TXT folder"
mp3_dir = "MP3 folder"
mp4_dir = "MP4 folder"
word_dir = "Word Documents"

# Creates paths
img_path = os.path.join(parent_directory, image_dir)
txt_path = os.path.join(parent_directory, txt_dir)
mp3_path = os.path.join(parent_directory, mp3_dir)
mp4_path = os.path.join(parent_directory, mp4_dir)
word_path = os.path.join(parent_directory, word_dir)

try:
    # Creates Image folder
    if not os.path.exists(img_path):
        os.makedirs(img_path, exist_ok = True)
        print(f"Created folder {image_dir}")
    else:
        print(f"{image_dir} exist")

    # Creates TXT folder
    if not os.path.exists(txt_path):
        os.makedirs(txt_path, exist_ok = True)
        print(f"Created folder {txt_dir}")
    else:
        print(f"{txt_dir} exist")

    # Creates MP3 folder
    if not os.path.exists(mp3_path):
        os.makedirs(mp3_path, exist_ok = True)
        print(f"Created folder {mp3_dir}")
    else:
        print(f"{mp3_dir} exist")

    # Creates MP4 folder
    if not os.path.exists(mp4_path):
        os.makedirs(mp4_path, exist_ok = True)
        print(f"Created folder {mp4_dir}")
    else:
        print(f"{mp4_dir} exist")
    
    # Creates Word folder
    if not os.path.exists(word_path):
        os.makedirs(word_path, exist_ok = True)
        print(f"Created folder {word_dir}")
    else:
        print(f"{word_dir} exist")

except OSError as e:
    print("File was not created " + e)


file = {
    ".txt": txt_path,
    ".png": img_path,
    ".jpeg": img_path,
    ".mp3": mp3_path,
    ".mp4": mp4_path,
    ".docx": word_path,
    }

print("\nFiles in directory before change")
print("-"*40)

# Find files in the directory
scan_dir = os.scandir(parent_directory)

# Scans each file
for entry in scan_dir:
    if entry.is_file():
        # Formats the files
        extension_finder = os.path.splitext(entry.name)

        # Finds audio files to move to folder
        if extension_finder[1] == ".txt":
            print(f"TXT FOUND {entry.name}")
            new_path = os.path.join(file[extension_finder[1]], os.path.basename(entry))

            # move the file to new folder
            os.rename(entry.path, new_path)

        # Finds picture files to move to folder
        elif extension_finder[1] == ".png" or extension_finder[1] == ".jpeg":
            print(f"IMAGE FOUND {entry.name}")
            new_path = os.path.join(file[extension_finder[1]], os.path.basename(entry))

            # move the file to new folder
            os.rename(entry.path, new_path)

        # Finds audio files to move to folder
        elif extension_finder[1] == ".mp3":
            print(f"AUDIO FOUND {entry.name}")
            new_path = os.path.join(file[extension_finder[1]], os.path.basename(entry))

            # move the file to new folder
            os.rename(entry.path, new_path)

        # Finds video files to move to folder
        elif extension_finder[1] == ".mp4":
            print(f"VIDEO FOUND {entry.name}")
            new_path = os.path.join(file[extension_finder[1]], os.path.basename(entry))

            # move the file to new folder
            os.rename(entry.path, new_path)
                # Finds video filea to move to folder
        
        # Finds video files to move to folde
        elif extension_finder[1] == ".docx":
            print(f"WORD DOC FOUND {entry.name}")
            new_path = os.path.join(file[extension_finder[1]], os.path.basename(entry))

            # move the file to new folder
            os.rename(entry.path, new_path)