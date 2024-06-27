import markovify
import os
import glob
import json

CUTOFF = 2000
NGRAM_SIZE = 3
dir_path = 'hest'

global model


def read_files_from_directory(directory_path):
    # Initialize an empty list to hold the text content
    text_list = []

    # Use glob to get all text files in the directory
    file_pattern = os.path.join(directory_path, '*')
    for i, file_path in enumerate(glob.glob(file_pattern)):
        # Ensure it's a file
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the file content and append to the list
                text_list.append(file.read())
        print(".", end="")
        if i == CUTOFF:
            break

    print("read data")
    return text_list


try:
    with open(f"{dir_path}.markov", "r") as f_model:
        print("Reading model from file")
        model = markovify.Text.from_json(f_model.read())
except FileNotFoundError as e:
    print(e)

    text_list = read_files_from_directory(dir_path)

    # Build the model.
    model = markovify.Text(text_list, NGRAM_SIZE)
    print("Built model")
    try:
        with open(f"{dir_path}.markov", "w") as f_model:
            f_model.write(model.to_json())
    except Exception as e:
        print(f"Could not write built model: {e}")

print("Ready for hest-quest: ")
