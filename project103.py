import pandas as pd
import plotly.express as pl

datar = pd.read_csv("c103.csv")
fig = pl.line(datar, x = "date", y = "cases", color = "country")
fig.show()