"""Text cleaning pipeline for a social media post.

Walks one tweet-style sentence through four cleaning steps and prints the
output after each step, so the effect of every step can be seen.
"""
import re

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

verbatim = "  That concert was absolutely INCREDIBLE!!! I had the best time \U0001F60D #UnforgettableNight  "

# Step 1a: remove leading and trailing whitespace
verbatim = verbatim.strip()
print("Remove whitespace:\n" + verbatim)

# Step 1b: remove punctuation, special characters and emojis
verbatim = re.sub(r"[^\w\s]", "", verbatim)
print("\nRemove punctuation:\n" + verbatim)

# Step 2: split attached PascalCase words (e.g. UnforgettableNight)
# Done before lowercasing. The lookbehind/lookahead only splits a lowercase
# letter followed by an uppercase letter, so all-caps words like INCREDIBLE stay whole.
verbatim = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", verbatim)
print("\nSplit attached words:\n" + verbatim)

# Step 3: lowercase
verbatim = verbatim.lower()
print("\nLowercase:\n" + verbatim)

# Step 4a: remove stopwords
stop_words = set(stopwords.words("english"))
verbatim = " ".join(word for word in verbatim.split() if word not in stop_words)
print("\nRemove stopwords:\n" + verbatim)

# Step 4b: tokenise
tokens = nltk.word_tokenize(verbatim)
print("\nTokens:")
print(tokens)
