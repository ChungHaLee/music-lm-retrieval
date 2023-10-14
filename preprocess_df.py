import pandas as pd
import os

# Load the MusicCaps dataset
musiccaps = pd.read_csv('./musiccaps-public.csv')

# Set the root directory of audio files
audio_directory = "/Users/lifeofpy/Documents/musiclm-2023/audioset/"

# Create a list to store audio file ytids
audio_ytids = set()

# Recursively traverse all subdirectories and collect audio ytids
for root, dirs, files in os.walk(audio_directory):
    for filename in files:
        if filename.endswith(".wav"):  # Check if it's a .wav file
            preid = os.path.splitext(filename)[0]
            ytid = preid[:11]
            audio_ytids.add(ytid)

# Filter the DataFrame to keep rows with ytids present in the audio files directory
musiccaps_filtered = musiccaps[musiccaps['ytid'].apply(lambda x: x in audio_ytids)]

# Now musiccaps_filtered contains only rows that have corresponding audio files in subfolders
musiccaps_filtered.to_csv('musiccaps-public-filtered.csv')
