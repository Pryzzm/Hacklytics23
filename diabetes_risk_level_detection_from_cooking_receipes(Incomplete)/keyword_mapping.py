import pandas as pd
import csv
import os
import re

os.chdir("/Volumes/Expansion/Hacklytics2023/")

#list_ingredient = pd.read_csv("ingredient_keyword_final.csv")
list_ingredient = pd.read_csv("high_contents.csv")
keywords = list_ingredient["ingredient"].values.tolist()


# Create new csv file to store the results
header = ['id', 'name', 'ingredients', 'risk_comp']
with open('mapping_keyword_result_test.csv', 'w', newline='') as csvfile:
    foundtext = csv.writer(csvfile)
    foundtext.writerow(header)

# Cues mapping process
with open("dataset.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        id = row[0]
        name = row[1]
        ingredients = row[5]
        each_ingredient = ingredients.split("',")
        for cue in keywords:
            pattern = r"\b%s\b" % cue
            for each in each_ingredient:
                cleaned_each = re.sub("[\[\]\.!@#$\']", "", each)
                cleaned_each = cleaned_each
                if re.search(pattern, cleaned_each, re.IGNORECASE):
                    print(
                        "+++++++++++++++++Cue: [", cue, "] found in:", id, ">>>", cleaned_each)
                if re.search(pattern, cleaned_each, re.IGNORECASE):
                    print("Cue: [", cue, "] found in:", id, ">>>", cleaned_each)
                    with open('mapping_keyword_result_test.csv', 'a', newline='') as csvfile:
                        foundtext = csv.writer(csvfile)
                        foundtext.writerow([id, name, cue, cleaned_each.lower()])
                        csvfile.flush()
                        print("The text is saved!")
                else:
                    print("Cue:", cue, "Not found")
print("Finish!")
