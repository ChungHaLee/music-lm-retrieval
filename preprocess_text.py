import torch
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
import pandas as pd

musiccaps_filtered = pd.read_csv('musiccaps-public-filtered.csv')
# Assuming you have a DataFrame with text descriptions (e.g., musiccaps_filtered)
# You should replace 'column_name' with the actual column name in your DataFrame
text_descriptions = musiccaps_filtered['caption'].tolist()
print(text_descriptions)
# Tokenize text data
tokenizer = get_tokenizer('basic_english')
tokenized_texts = [tokenizer(text) for text in text_descriptions]

# Build a vocabulary and convert text to integers
vocab = build_vocab_from_iterator(tokenized_texts)
text_data = []
for tokens in tokenized_texts:
    tokens = [vocab[token] for token in tokens]
    # Ensure each text is of length 256
    if len(tokens) >= 256:
        tokens = tokens[:256]
    else:
        padding = [0] * (256 - len(tokens))
        tokens += padding
    text_data.append(tokens)

# Convert text data to a tensor
text_data = torch.tensor(text_data)

# You now have text data in the desired shape (num_texts, 256)
texts = text_data
torch.save(texts, 'texts.pt')