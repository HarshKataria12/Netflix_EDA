import pandas as pd #FOR DATA MANIPULATION And frame 
import numpy as np #FOR NUMERICAL CALCULATIONS
import matplotlib.pyplot as plt #FOR VISUALIZATION
import seaborn as sns #FOR VISUALIZATION And Graphs

netflix_data = pd.read_csv('/kaggle/input/exploratory-data-analysis-on-netflix-data/netflix_titles_2021.csv') #READING THE DATASET
netflix_data.head() #DISPLAYING THE FIRST 5 ROWS OF THE DATASET
