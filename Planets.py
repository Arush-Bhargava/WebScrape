import requests
import pandas as pd

link = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
html = requests.get(link).content
df_list = pd.read_html(html)
df = df_list[-1]

print(df)
df.to_csv('myplanets.csv')