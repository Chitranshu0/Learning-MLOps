import pandas as pd 
import os 

data = {
    'name': ['bob', 'rahul', 'sam'],
    'Age': [30, 40, 32],
    'city': ['Delhi', 'Bangalore', 'Gurugoan']
}

df = pd.DataFrame(data)

print(df.head())


os.makedirs('data', exist_ok=True)

file_path = os.path.join('data', 'sample_data.csv')

df.to_csv(file_path, index=False)

print("done")