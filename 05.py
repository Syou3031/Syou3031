import pandas as pd
df = pd.read_csv('file.csv')
df.fillna(0, inplace=True)
df.to_csv('updatedfile.csv', index=False)
print("Missing values have been replaced with 0 and saved to 'updatedfile.csv'.")
