import pandas as pd
import plotly.figure_factory as pff

df = pd.read_csv('data2.csv')
avg_rating = df['Avg Rating'].to_list()

figure = pff.create_distplot([avg_rating], ['AVERAGE RATING'])
figure.show()