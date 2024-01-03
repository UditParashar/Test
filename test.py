import pandas as pd

def remove_duplicates(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Remove duplicates based on values in column 1
    df_no_duplicates = df.drop_duplicates(subset=df.columns[0], keep='first')

    # Write the DataFrame without duplicates to a new CSV file, excluding the index column
    df_no_duplicates.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Prompt user to input CSV file name
    input_csv = input("Enter the input CSV file name: ")

    # Prompt user to input desired output CSV file name
    output_csv = input("Enter the output CSV file name: ")

    # Call the function with user-input file names
    remove_duplicates(input_csv, output_csv)

    print("Duplicates removed successfully. Output saved to", output_csv)