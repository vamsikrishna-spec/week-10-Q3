#24331A05E7
#to perform dataframe modification and data cleaning in pandas.
import pandas as pd
data = {
   'Name': ['spidyy', 'maxy', 'starboy', 'krishh'],
   'Age': [19, 20, 23, 18],
   'Marks': [93, 88, 99, 869],
   'Fav subject': ['Biology','mathematics','chemistry','physics']
}
df = pd.DataFrame(data)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(0)
df['Grade'] = ['B', 'A', 'C', 'B']
df.loc[df['Marks'] > 85, 'Grade'] = 'A'
print(df)
