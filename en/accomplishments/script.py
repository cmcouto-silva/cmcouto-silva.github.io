#!/bin/env python

# Import Pandas
import pandas as pd

# Load data and drop missing values
df = pd.read_excel('/home/cmcouto-silva/cmcouto.silva@usp.br/home/datascience_curriculum.xlsx')
df = df.dropna(subset=['Name', 'Completed'])
df.head()

# Fix dtypes
df[['Start_date', 'End_date']] = df[['Start_date', 'End_date']].apply(pd.to_datetime)
df['Completed'] = df['Completed'].astype(bool)

# Get courses with certificate
df = df.dropna(subset=['Start_date'])
df_accomplishments = df[['Name', 'Institution', 'Start_date', 'Link', 'Certificate']].drop_duplicates()

def make_accomplishments(title, organization, date_start, url, certificate_url):
    return(f"""[[item]]
  title = "{title}"
  organization = "{organization}"
  date_start = "{date_start}"
  url = "{url}"
  certificate_url = "{certificate_url}"

""")

with open('accomplishments.txt', 'w') as file:
    for _, row in df_accomplishments.iterrows():
        file.write(make_accomplishments(*row))

