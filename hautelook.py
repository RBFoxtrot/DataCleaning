import pandas as pd
import re

# Load the data from a CSV file
df = pd.read_csv(r"C:\Users\roger\Downloads\hautelook\28M-US-hautelook.com-Online-Fashion-Shopping-UsersDB-csv-2018.csv", low_memory=False)

df.head()

df.info()

# Rename the unnamed columns
df = df.rename(columns={'1@placeholder.xxx': 'e_mail', 'Unnamed: 1': 'password_hash', 'placeholder': 'firstname', 'placeholder.1': 'lastname', 'Unnamed: 4': 'zip_code', 'Unnamed: 5': 'location', 'M': 'gender', 'Unnamed: 7': 'birthdate'})

print(df.isnull().sum())

# Convert the 'birthdate' integer column to datetime
df['birthdate'] = pd.to_datetime(df['birthdate'], errors='coerce')

df.info()

df['birthdate'] = df['birthdate'].dt.date

# Fill missing values with a specific value
df['e_mail'] = df['e_mail'].fillna('NA')
df['password_hash'] = df['password_hash'].fillna('NA')
df['firstname'] = df['firstname'].fillna('NA')
df['lastname'] = df['lastname'].fillna('NA')
df['zip_code'] = df['zip_code'].fillna('00000')
df['location'] = df['location'].fillna('XX')
df['gender'] = df['gender'].fillna('X')
# Fill NaT with the minimum datetime value
df['birthdate'] = df['birthdate'].fillna('0001-01-01')

print(df.isnull().sum())

# Capitalize firstname, lastname, excluding 'NA'
df['firstname'] = df['firstname'].apply(lambda x: x.capitalize() if x != 'NA' else x)
df['lastname'] = df['lastname'].apply(lambda x: x.capitalize() if x != 'NA' else x)

df.sample(10)

# Find duplicate rows based on 'e_mail'
duplicates = df.duplicated(subset=['e_mail'], keep='first')

# Create a DataFrame of duplicate rows
duplicate_rows = df[duplicates]

# Remove duplicate rows from the original DataFrame
df = df[~duplicates]

# Export duplicate rows to a CSV file
duplicate_rows.to_csv('duplicate_rows.csv', index=False)

# Define a regular expression pattern for valid email addresses
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Find rows with invalid email addresses
invalid_emails_df = df[~df['e_mail'].str.match(email_pattern, na=False)]

# Remove rows with invalid email addresses from the original DataFrame
df_valid_emails = df[df['e_mail'].str.match(email_pattern, na=False)]

# Export the rows with invalid emails to a separate CSV file
invalid_emails_df.to_csv('rows_with_invalid_emails.csv', index=False)

# Load the two CSV files into pandas DataFrames
invalid_emails_df = pd.read_csv('rows_with_invalid_emails.csv')
duplicate_rows_df = pd.read_csv('duplicate_rows.csv')

# Concatenate the two DataFrames
garbage_df = pd.concat([invalid_emails_df, duplicate_rows_df], ignore_index=True)

# Save the merged DataFrame to a new CSV file
garbage_df.to_csv('garbage.csv', index=False)

garbage_df

hautelook_cleaned = df_valid_emails.reset_index(drop=True)
hautelook_cleaned

hautelook_cleaned.to_csv("hautelook_cleaned.csv", index=False)

