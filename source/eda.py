def unique_values_each_column(df):
    # Print number of unique values in all columns
    for col in df.columns:
        print(col, ':', df[col].nunique())