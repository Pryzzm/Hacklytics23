# Extracting info about the amount/quantity of the potential risk ingredients
import pandas as pd
import csv
import os
import re

ingredients_meassure = ["gr", "ml", "l", "kg", "gram","g", "tbsp", "cup", "cups", "tsp", "teaspoon", "pound",
                        "teaspoons", "oz", "stick", "pounds", "lb", "whole", "slice", "slices", "sliced", "clove", "piece", "handful","packages",
                        "pinch", "piecies"]
result = []
normalization_result = []

os.chdir("/Volumes/Expansion/Hacklytics2023/")

def extract_amount(text, ingredient):
    text = text
    ingredient = ingredient
    for im in ingredients_meassure:
        if re.search("^(\d\s)*%s" % im,text):
                value_measurand = re.split(im,text)
                value = value_measurand[0].replace(" ","")
                print(value_measurand)
                data_conversion = {
                "ingredient": ingredient,
                "value": str(value),
                "measurand": im
            }
                return data_conversion
        else:
            print("Done")
            continue
        
def symbols_converter(quantity):
    if re.search("½", quantity):
        quant = quantity.translate({ord("½"): ".50"})
        return float(quant)
    if re.search("¼", quantity):
        quant = quantity.translate({ord("¼"): ".25"})
        return float(quant)
    if re.search("¾", quantity):
        quant = quantity.translate({ord("¾"): ".75"})
        return float(quant)
    if re.search("⅓", quantity):
        quant = quantity.translate({ord("⅓"): ".33"})
        return float(quant)
    if re.search("⅔", quantity):
        quant = quantity.translate({ord("⅔"): ".66"})
        return float(quant)
    if re.search(r"1\/2", quantity):
        quant = re.sub(r"\s?1\/2", ".50", quantity)
        return float(quant)
    if re.search(r"1\/4", quantity):
        quant = re.sub(r"\s?1\/4", ".25", quantity)
        return float(quant)
    if re.search(r"3\/4", quantity):
        quant = re.sub(r"\s?3\/4", ".75", quantity)
        return float(quant)
    if re.search(r"1\/3", quantity):
        quant = re.sub(r"\s?1\/3", ".33", quantity)
        return float(quant)
    if re.search(r"2\/3", quantity):
        quant = re.sub(r"\s?2\/3", ".66", quantity)
        return float(quant)
    else:
        return float(quantity)


# Create new csv file to store the results
header = ['id', 'name', 'ingredients', 'risk_compon', 'value', 'value_normalized', 'measurand']
with open('full_results.csv', 'w', newline='') as csvfile:
    convert_val = csv.writer(csvfile)
    convert_val.writerow(header)

with open("mapping_keyword_result_test.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        id = row[0]
        name = row[1]
        ingredients = row[2]
        risk_compon = row[3]
        print(risk_compon)
        if(risk_compon == 'risk_comp'):
            continue
        print(risk_compon)
        res = extract_amount(risk_compon, ingredients)
        print(res)
        new_value = symbols_converter(res['value'])
        res['normalized_value'] = new_value
        print(res)
        with open('value_result_normalized.csv', 'a', newline='') as csvfile:
            convert_val = csv.writer(csvfile)
            convert_val.writerow([id, name, ingredients, risk_compon, res['value'], res['normalized_value'], res['measurand']])
            csvfile.flush()
            print("The data for",id, "is saved!")
print('Done)')



