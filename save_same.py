import pandas as pd
import os

# Load the MusicCaps dataset
musiccaps = pd.read_csv('./musiccaps-public.csv')
id = musiccaps['ytid'].values
id_lst = set(id.tolist())

# Create a list of ytid from audio files
ytid_lst = []
for (path, dirs, files) in os.walk("/Users/lifeofpy/Documents/musiclm-2023/audioset/"):
    for filename in files:
        preid = os.path.splitext(filename)[0]
        ytid = preid[:11]
        ytid_lst.append(ytid)

ytid_lst = set(ytid_lst)

# Find the common elements between id_lst and ytid_lst
same_lst = id_lst & ytid_lst

# Delete audio files that are not in same_lst
audio_directory = "/Users/lifeofpy/Documents/musiclm-2023/audioset/"

def delete_audio_files_not_in_list(directory_path, same_list):
    for (path, dir, files) in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".wav"):  # Check if it's a .wav file
                file_path = os.path.join(path, filename)  # Include 'path'
                # print(file_path)
                preid = os.path.splitext(filename)[0]
                ytid = preid[:11]
                # if ytid not in same_list:
                #     os.remove(file_path)  # This line deletes the file
                #     print(f"Deleted: {filename}")


delete_audio_files_not_in_list(audio_directory, same_lst)
