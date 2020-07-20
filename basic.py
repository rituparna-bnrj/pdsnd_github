import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')

print(df.head(6))
