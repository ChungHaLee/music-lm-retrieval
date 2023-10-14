import torch
from musiclm_pytorch import MuLaN, AudioSpectrogramTransformer, TextTransformer

audio_transformer = AudioSpectrogramTransformer(
    dim = 512,
    depth = 6,
    heads = 8,
    dim_head = 64,
    spec_n_fft = 128,
    spec_win_length = 24,
    spec_aug_stretch_factor = 0.8
)

text_transformer = TextTransformer(
    dim = 512,
    depth = 6,
    heads = 8,
    dim_head = 64
)

mulan = MuLaN(
    audio_transformer = audio_transformer,
    text_transformer = text_transformer
)

# get a ton of <sound, text> pairs and train

# Load the wavs tensor from the saved file
wavs = torch.load('/Users/lifeofpy/Documents/musiclm-2023/musiclm-pytorch/wavs.pt')
wavs = wavs.view(wavs.size(0), -1)  # Reshape wavs
texts = torch.load('/Users/lifeofpy/Documents/musiclm-2023/musiclm-pytorch/wavs.pt')

print('wavs', wavs)
print('texts', texts)

loss = mulan(wavs, texts)
loss.backward()

# after much training, you can embed sounds and text into a joint embedding space
# for conditioning the audio LM

embeds = mulan.get_audio_latents(wavs)  # during training

embeds = mulan.get_text_latents(texts)  # during inference


print('end of training!')