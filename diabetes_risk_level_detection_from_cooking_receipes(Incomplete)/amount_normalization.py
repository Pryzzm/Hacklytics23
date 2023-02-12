import pandas as pd
import csv
import os
import re

ingredients_meassure = ["tbsp", "cup", "cups", "tsp", "teaspoon", "pound", "teaspoons", "oz",
                        "stick", "pounds", "lb", "whole", "slice", "slices", "sliced", "clove", "piece", "handful"]

# symbols = ["½","¼","¾","½","⅔","⅓"] >>> convert them to 1/2, 1/4 ...
sample = ["2¼", "5¼", "3½", "5", "½", "¼", "⅓", "2⅔", "2 1/2", "31/4"]
result = []

# Amount Normalization

def symbols_converter(quantity):
    quantity = quantity
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
        return int(quantity)

for s in sample:
    new = symbols_converter(s)
    result.append(new)
    print(result)

