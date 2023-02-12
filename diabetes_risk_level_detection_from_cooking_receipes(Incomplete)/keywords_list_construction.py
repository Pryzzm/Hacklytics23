####### Importing Modules & Library #########
import pandas as pd
import csv
import os
import re

os.chdir("/Volumes/Expansion/Hacklytics2023/")

# 1. Individual indredient text cleaning & normalizing

data = pd.read_csv("cleaned_ingredients.csv")
list_ingredients = data['Descrip'].tolist()
removed_token = ['with', 'w', "-"]
#removed_character = ["(",")","-","'"]
cleaned_ingredient = []
ingredient_cues = []
uni_cues = []

# Generating the ingredient cues


def string_cleaning(ingredient):
    for n in removed_token:
        cleaned_ingredient = ingredient.replace(n, "")
        cleaned_ingredient = re.sub("-", " ", cleaned_ingredient)
        cleaned_ingredient = re.sub(' +', ' ', cleaned_ingredient)
        cleaned_ingredient = " ".join(cleaned_ingredient.split()[
                                      :2])  # to capture bigram
        cleaned_ingredient = re.sub("[!@#$'\(\)]", "", cleaned_ingredient)
        return cleaned_ingredient
    cleaned_ingredient.append(cleaned_ingredient)
    # print("Result:",cleaned_ingredient)


for i in list_ingredients:
    cue = string_cleaning(i)
    # print(cue)
    ingredient_cues.append(str(cue))
    print("Cue:", cue, "| The cue is added to list")
    print(len(ingredient_cues))

print('Done')

# Extending the list by adding unigrams
for bigram in ingredient_cues:
    unigram = bigram.split()
    # print(cue)
    for u in unigram:
        uni_cues.append(str(u))
        print("Cue:", u, "| The cue is added to list")

print("Unigram total:", len(uni_cues))

# Omitting irrelevant keywords
for keyw in unigram:
    if re.search("\d",str(keyw)):
        unigram.remove(keyw)
        print("Keyword:",keyw,"is removed")

# Concatenate unigrams and bigrams list
final_list = list(dict.fromkeys(uni_cues))
print("Total final:", len(final_list))

# Save the list
df = pd.DataFrame(final_list)
df.to_csv('ingredient_keyword_final2.csv', index=False)
