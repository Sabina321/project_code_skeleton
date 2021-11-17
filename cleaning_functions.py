import matplotlib.pyplot as plt
import pandas as pd

def extract_last_name(name_column):
    if type(name_column)==str and ',' in name_column:
        return name_column.split(',')[0]
    return "no last name"

## returns a plot which shows survival rates by pclass
def generate_central_plot(df):
    to_plot = df.groupby("Pclass")["Survived"].agg(['mean','count'])
    f, ax = plt.subplots(figsize=(5,5))
    ax.scatter(to_plot.index, to_plot["mean"], s=to_plot["count"])   
    ax.set_ylim(0,1)
    return ax 
