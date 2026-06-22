import pandas as pd 

df = pd.read_csv(r'data\sample_data.csv')

new_df = pd.DataFrame({
    'name': ['Divya'],
    'Age': [22],
    'city': ['Deradun']
})

df = pd.concat([df, new_df], ignore_index=True)

# Save updated dataset
df.to_csv(r'data\sample_data.csv', index=False)

print(df)