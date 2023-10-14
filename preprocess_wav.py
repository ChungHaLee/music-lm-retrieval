import torch
import torchaudio
from torchaudio.transforms import Spectrogram
import os

# Set the directory path where your audio files are located
audio_directory = "./audioset"

def find_wav_files(directory):
    # Initialize an empty list to collect the paths of .wav files
    wav_files = []
    
    # Recursively search for .wav files in subdirectories
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".wav"):
                wav_files.append(os.path.join(root, filename))
    
    return wav_files


def preprocess_audio(audio_file):
    try:
        waveform, _ = torchaudio.load(audio_file)
        
        # Ensure the waveform has a single channel (mono)
        if waveform.shape[0] > 1:
            # Convert stereo audio to mono by taking the mean of channels
            waveform = waveform.mean(dim=0, keepdim=True)
        
        # Apply any necessary transformations to make it fit (2, 1024)
        # For example, you can use a spectrogram:
        spectrogram = Spectrogram()(waveform)
        # Resize the spectrogram to (2, 1024) using interpolation or trimming
        if spectrogram.shape[2] >= 1024:
            spectrogram = spectrogram[:, :, :1024]
        else:
            padding = torch.zeros(2, 1024 - spectrogram.shape[2])
            spectrogram = torch.cat([spectrogram, padding], dim=2)
        return spectrogram
    except Exception as e:
        print(f"Error processing {audio_file}: {str(e)}")
        # os.remove(audio_file)  # This line deletes the file
        # print(f"Deleted: {audio_file}")
        return None

# Get a list of all .wav files in subdirectories
audio_files = find_wav_files(audio_directory)

# Process all audio files and stack them into a single tensor
audio_data = torch.stack([preprocess_audio(file) for file in audio_files if preprocess_audio(file) is not None])

# You now have audio data in the desired shape (2, 1024)
wavs = audio_data
print(wavs.size())
# print(wavs)
# torch.save(wavs, 'wavs.pt')