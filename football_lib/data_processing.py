import pandas as pd
import ast
from sklearn.preprocessing import MinMaxScaler

def combine_csv_to_df(csv_files, expected_columns):
    df_list = []
    
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        position = csv_file.replace('.csv', '')
        df['position'] = position
        attribute_vectors = df['Attribute Vector'].apply(ast.literal_eval)
        df_attributes = pd.DataFrame(attribute_vectors.tolist(), columns=expected_columns)
        df_combined = pd.concat([df[['Name', 'position']], df_attributes], axis=1)
        df_list.append(df_combined)
    
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df = combined_df.loc[:, ~combined_df.columns.duplicated()]
    
    return combined_df

def normalize_data(df, columns_to_normalize):
    scaler = MinMaxScaler()
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
    
    return df
