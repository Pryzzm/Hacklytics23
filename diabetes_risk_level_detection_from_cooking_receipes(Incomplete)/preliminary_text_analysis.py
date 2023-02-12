# Mapping high risk ingredient
import pandas as pd
import csv
import os
import re
import wordcloud as wd
import matplotlib.pyplot as plt

os.chdir("/Volumes/Expansion/Hacklytics2023/")

# WordCould: 1. All recipes 2. Recipes that has keywords

# DATASETS
datasets = pd.read_csv("dataset.csv")
datasets.isna().sum()
len(datasets)  # 13501
datasets.head(5)
datasets.tail(5)

# PRELIMINARY RESULTS
mapping_result = pd.read_csv("mapping_keyword_result_test.csv")
len(datasets)
mapping_result.head(5)
mapping_result.tail(5)
total_detected_recipes = len(mapping_result) - \
    len(mapping_result.drop_duplicates())
total_detected_recipes  # 579

# 1. Wordcloud from whole data

# Select the desired column
text_column = datasets["Cleaned_Ingredients"]
cleaned_text = []

# Define the cleaning function


def clean_text(text):
    # Remove punctuation and special characters
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaning = ["toasted", "room temperature", "plus", "chilled", "drained", "fresh", "freshly", "ground", "exra", "drizzling", "packed", "into", "small", "cut", "softened", "room temperature",
                "divided", "grated", "firmly", "cooled", "fried", "grill", "grilled", "frying", "steam", "cooled", "gr", "ml", "l", "kg", "gram", "g", "tbsp", "cup", "cups", "tsp", "teaspoon", "pound",
                "teaspoons", "oz", "stick", "pounds", "lb", "whole", "slice", "slices", "sliced", "clove", "piece", "handful", "packages", "rounded",
                "pinch", "piecies", "packed"]
    text = text.lower()
    text = re.sub("[!@#$'\(\)]", "", text)
    text = re.sub("[0-9]*", '', text)
    text = re.sub("[\W]+", ' ', text)
    text = re.sub("^W?", '', text)
    text = re.sub("[½,¼,¾,⅓,⅔]+", ' ', text)
    for w in cleaning:
        pattern = "\b%s\b" % w
        re.sub(pattern, "", text)
        return text


# for loop to check each character in the string
for line in datasets['Cleaned_Ingredients']:
    cleaning = clean_text(line)
    cleaned_text.append(cleaning)
    print(cleaned_text)

# Save the list
df = pd.DataFrame(cleaned_text)
df.to_csv('cleaned_text.csv', index=False)
