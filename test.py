from datetime import datetime

def print_current_date_time():
    # Get the current date and time
    current_date_time = datetime.now()

    # Format and print the current date and time
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date_time)

# Call the function to print the date and time
print_current_date_time()


# def remove_duplicates(input_file, output_file):
#     # Read the CSV file into a pandas DataFrame
#     df = pd.read_csv(input_file)

#     # Remove duplicates based on values in column 1
#     df_no_duplicates = df.drop_duplicates(subset=df.columns[0], keep='first')

#     # Write the DataFrame without duplicates to a new CSV file, excluding the index column
#     df_no_duplicates.to_csv(output_file, index=False)

# if __name__ == "__main__":
#     # Prompt user to input CSV file name
#     input_csv = input("Enter the input CSV file name: ")

#     # Prompt user to input desired output CSV file name
#     output_csv = input("Enter the output CSV file name: ")

#     # Call the function with user-input file names
#     remove_duplicates(input_csv, output_csv)

#     print("Duplicates removed successfully. Output saved to", output_csv)
