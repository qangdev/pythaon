# Built-in lib
import csv
from typing import List

# Third Patties lib
# import matplotlib.pyplot as plt

# step 1: load data from csv file
with open('./dataset/orders.csv', newline="") as csvfile:
    data = list(csv.reader(csvfile))   #con trõ đang ở dòng cuối của file csv - if read again we need to reset the con trỏ
    print(data[0])
    for idx, row in enumerate(data):   #how to get a column names list in python???
        if idx == 0:
            print(row)
print(data.__class__)

# I try different way is to import dataframe as a array

# step 3: plot data as histogram