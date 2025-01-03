import pandas as pd
import matplotlib.pyplot as plt

def get_questions_by_name (df, qname):
    """
    This function retrieves the full question from a DataFrame based on a specific question name.
    Parameters:
        - df: The DataFrame containing the data.
        - qname: The value in the 'qname' column to filter by.
    Returns:
        - The full questions where the 'qname' column matches the specified qname value.
    """
    
    return list(df.loc[df['qname'] == qname, 'question'])

def calculate_unique_value_percentages(df, col):
    """
    Calculate the percentage distribution of unique values in a specified column of a DataFrame.

    This function processes a column of a DataFrame where the values are delimited strings 
    (e.g., "Python;Java;C++"), splits the strings into individual components, and calculates 
    the percentage of occurrences of each unique value.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        col (str): The name of the column to analyze.

    Returns:
        pd.DataFrame: A DataFrame containing the unique values and their percentage occurrence.
    """
    # Drop rows where the specified column has NaN values
    df.dropna(subset=[col], inplace=True)

    # Split the delimited strings in the column into lists
    data_split = df[col].str.split(';')

    # Flatten the lists into a single column
    data_exploded = data_split.explode()

    # Calculate the percentage occurrences of each unique value
    data_counts = pd.DataFrame(data_exploded.value_counts() / df.shape[0] *100)

    # Convert the Series to a DataFrame for better presentation
    result = pd.DataFrame(data_counts)

    return result
