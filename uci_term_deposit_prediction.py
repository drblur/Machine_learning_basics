import pandas as pd
import numpy as np
from sklearn import  preprocessing
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid",color_codes=True)
plt.rc("font", size=14)

# importing the dataset
data = pd.read_csv("bank-additional-full.csv", header=0)
data = data.dropna()
print data.shape
print data.columns
print data.head(5)

# exploring and understanding the dataset
desc = pd.DataFrame(data.describe().T)
print desc