import os
from moviepy.editor import VideoFileClip

# Define the root directory where your audioset folders are located
root_directory = './audioset'

# Function to convert webm files to wav
def convert_webm_to_wav(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    audio.close()

# Loop through the audioset folders
for genre_folder in os.listdir(root_directory):
    genre_folder_path = os.path.join(root_directory, genre_folder)

    # Check if it's a directory
    if os.path.isdir(genre_folder_path):
        for webm_file in os.listdir(genre_folder_path):
            if webm_file.endswith('.webm'):
                webm_file_path = os.path.join(genre_folder_path, webm_file)

                # Construct the output wav file path
                wav_file = os.path.splitext(webm_file)[0] + '.wav'
                wav_file_path = os.path.join(genre_folder_path, wav_file)

                # Convert webm to wav
                convert_webm_to_wav(webm_file_path, wav_file_path)

print("Conversion completed.")
