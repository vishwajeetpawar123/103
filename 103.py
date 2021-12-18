import pandas as pd
import csv
import plotly.express as px
import csv

df=pd.read_csv("data103.csv")

fig=px.scatter(df, x = 'date', y = 'cases',color="country")

fig.show()
