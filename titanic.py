import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.DataFrame({
    "Name": ["Rahul", 'Aman', 'Priya', 'Riya', 'Mohit'],
    "Age": [22, 25, 21, 24, 23],
    "Marks": [80, 75, 90, 85, 70]
})

print(data.head())
print(data.dtypes)
print(data.isnull().sum())

