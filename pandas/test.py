import pandas as pd

# Create data frame 
data = [[1, 2], [3, 4]] 
df = pd.DataFrame(data, columns=['Num1', 'Num2'], index=['R1', 'R2'])
print(df)


# Create series
s = df['Num1']
print(s)

csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/refs/heads/main/wine-ratings.csv"

df = pd.read_csv(csv_url,index_col=0)
# print(df.head(10))

# print(df.describe())

# print(df.info())

# print(df.query(("rating>97")).describe())