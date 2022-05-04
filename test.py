import random
import pandas as pd
import plotly.express as px
import csv
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")

fig=ff.create_distplot([df["Avg_Rating"].tolist()], ["ratings"], show_hist=False)
fig.show()