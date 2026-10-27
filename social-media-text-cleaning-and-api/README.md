# Social Media Text Cleaning and API Data Retrieval

Two short Python exercises in preparing social media data for analysis: a step-by-step text cleaning pipeline for a tweet, and a program that retrieves and displays structured data from a public REST API.

Module: CET365 Social Media Metrics and Analytics, Singapore University of Social Sciences (2025)

## Contents

| File | What it does |
|---|---|
| `text_cleaning.py` | Cleans one tweet in four steps and prints the result after each step |
| `pokeapi_lookup.ipynb` | Sends requests to the [PokeAPI](https://pokeapi.co/), parses the JSON response and displays a Pokémon's details |

## 1. Text cleaning pipeline

Input:

```
That concert was absolutely INCREDIBLE!!! I had the best time 😍 #UnforgettableNight
```

| Step | Output |
|---|---|
| 1. Remove whitespace, punctuation, special characters and emojis | `That concert was absolutely INCREDIBLE I had the best time UnforgettableNight` |
| 2. Split attached words | `That concert was absolutely INCREDIBLE I had the best time Unforgettable Night` |
| 3. Lowercase | `that concert was absolutely incredible i had the best time unforgettable night` |
| 4. Remove stopwords and tokenise | `['concert', 'absolutely', 'incredible', 'best', 'time', 'unforgettable', 'night']` |

A common approach splits words at every uppercase letter, which would break `INCREDIBLE` into single letters. The regular expression `(?<=[a-z])(?=[A-Z])` only splits where a lowercase letter is followed by an uppercase one, so `UnforgettableNight` is split and `INCREDIBLE` stays whole. This step runs before lowercasing so the case information is still available.

## 2. PokeAPI lookup

The notebook:

1. Requests the API's root endpoint and lists the available resources.
2. Asks the user for a Pokémon name and requests `https://pokeapi.co/api/v2/pokemon/{name}`.
3. Converts the JSON response to a Python dictionary.
4. Displays the name, ID, height, weight, types, abilities (marking hidden ones) and base stats.
5. Handles names that are not found and asks the user to try again.

## How to run

```bash
pip install nltk requests
python text_cleaning.py
```

Open `pokeapi_lookup.ipynb` in Jupyter to run the API lookup.

## Skills demonstrated

- Text preprocessing with regular expressions and NLTK
- Calling a REST API with `requests` and parsing JSON
- Input validation and error handling

## Author

Jawenn Lim
