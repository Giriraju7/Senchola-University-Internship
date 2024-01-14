# -*- coding: utf-8 -*-
"""Senchola Batch 2 Application Details.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JNLIHFgXvE6GVs2dZqG5fqdJKM6kWODr

**Senchola Batch 2 Application Details**

Import Data from excel file
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df=pd.read_excel('/content/Batch-2 Senchola application details - Data cleaned.xlsx')

df.head()

df.info()

df.isnull().sum()

df.columns

"""## **Insights**

**1. Total number of Applicants**
"""

total_applicants=df['Name '].count()
print("Total number of Applicants:" ,total_applicants)

"""**2.Gender classification**"""

df1= pd.read_excel('/content/Batch-2 Senchola application details - Data cleaned.xlsx', sheet_name='Name & Gender')
gender_counts = df1['Gender'].value_counts()
print(gender_counts)

"""**3.Openness to learn**"""

openness_to_learn = df['Are you open to learn ?'].value_counts()
colors = ['green', 'red', 'yellow']
# Create a pie chart
plt.figure(figsize=(5,5))
plt.pie(openness_to_learn, labels=openness_to_learn.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Openness to Learn')
plt.show()

"""**4.Motivation for Join**"""

text_data = ' '.join(df['Why you want to join this program ?'])

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

# Display the WordCloud image
plt.figure(figsize=(5, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

"""**5.Laptop Availability**"""

laptop_availability = df['Do you have laptop '].value_counts()

# Define custom colors
colors = ['green', 'red']

# Create a pie chart
plt.figure(figsize=(5,5))
plt.pie(laptop_availability, labels=laptop_availability.index, autopct='%2.2f%%', startangle=140, colors=colors)
plt.title('Laptop Availability')
plt.show()

"""**6.Qualification Distribution**"""

qualification_distribution = df['Qualification'].value_counts()

plt.figure(figsize=(5,5))
plt.bar(qualification_distribution.index, qualification_distribution.values, color='blue')
plt.title('Qualification Distribution')
plt.xlabel('Qualification Level')
plt.ylabel('Count')
plt.xticks(rotation=45, ha="right")

for i, value in enumerate(qualification_distribution.values):
    plt.text(i, value + 0.2, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.show()

"""**7.Popular Degree**"""

degree_distribution = df['Degree'].str.upper().value_counts()


top_degrees = degree_distribution.head(10)


plt.figure(figsize=(5,5))
plt.bar(top_degrees.index, top_degrees.values, color='blue')
plt.title('Popular Degrees')
plt.xlabel('Degree')
plt.ylabel('Count')
plt.xticks(rotation=45, ha="right")


for i, value in enumerate(top_degrees.values):
    plt.text(i, value + 0.2, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.show()

"""**8.Gradution Year**"""

df['Pass-out Year'] = pd.to_numeric(df['Pass-out Year'], errors='coerce')

df = df.dropna(subset=['Pass-out Year'])

pass_out_years = df['Pass-out Year'].value_counts().sort_index()

plt.figure(figsize=(5,5))
plt.plot(pass_out_years.index, pass_out_years.values, marker='o', color='blue', linestyle='-')
plt.title('Graduation Year Distribution')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
for i, value in enumerate(pass_out_years.values):
    plt.text(pass_out_years.index[i], value + 1, str(value), ha='center', va='bottom', fontsize=10, color='black')
plt.tight_layout()
plt.show()

"""**9.Top Colleges**"""

top_colleges = df['College Name'].value_counts().head(10)

plt.figure(figsize=(5,5))
plt.bar(top_colleges.index, top_colleges.values, color='blue')
plt.title('Top Colleges')
plt.xlabel('College Name')
plt.ylabel('Count')
plt.xticks(rotation=45, ha="right")

for i, value in enumerate(top_colleges.values):
    plt.text(i, value + 0.2, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.show()

"""**10.City Distribution**"""

city_distribution = df['City'].value_counts().head(10)

plt.figure(figsize=(10,5))
plt.subplot(121)
plt.bar(city_distribution.index, city_distribution.values, color='blue')
plt.title('City Distribution')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45, ha="right")


for i, value in enumerate(city_distribution.values):
    plt.text(i, value + 0.2, str(value), ha='center', va='bottom')

"""**11. Areas of Interest**"""

areas_of_interest = df['What you wan to learn ?'].value_counts().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,8))
plt.plot(areas_of_interest.index, areas_of_interest.values, marker='o', color='blue', linestyle='-')
plt.title('Top 10 Areas of Interest Distribution')
plt.xlabel('Area of Interest')
plt.ylabel('Count')
plt.xticks(rotation=45)

for x, y in zip(areas_of_interest.index, areas_of_interest.values):
    plt.text(x, y, str(y), ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()

"""**12.Tecnical Feedback by**"""

feedback_counts = df['Technical Feeback by'].value_counts().head(10)

plt.figure(figsize=(5,5))
plt.bar(feedback_counts.index, feedback_counts.values, color='blue')
plt.title('Technical Feedback by')
plt.xlabel('Name')
plt.ylabel('Count')
plt.xticks(rotation=45, ha="right")


for i, value in enumerate(feedback_counts.values):
    plt.text(i, value + 0.2, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.show()

"""**13. HR Comments**"""

hr_comments_count = df.groupby('HR Comments').size().sort_values(ascending=False).head(5)

plt.figure(figsize=(10,8))
plt.bar(hr_comments_count.index, hr_comments_count.values, color='blue')
plt.title('Top 5 HR Comments')
plt.xlabel('HR Comments')
plt.ylabel('Count')
plt.xticks(rotation=45, ha="right")

for i, value in enumerate(hr_comments_count.values):
    plt.text(i, value + 0.2, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.show()

"""                                                   **Thank You!!**"""