![DataCleaning](dataclean.jpg)

# CarOwnersNationwide Data Cleaning Script

## Overview

This data cleaning script processes a dataset of China Car Owners Nationwide (2020). It performs column translation, normalization, missing value handling, and removes invalid entries like duplicate ID cards and invalid email addresses. After cleaning, it exports the processed data into a new file. This guide provides a clear explanation of the steps involved, designed for both beginner analysts and experienced data engineers.

## Prerequisites

Python Environment: Ensure you have Python installed, along with necessary packages like [pandas](https://pypi.org/project/pandas/) and [googletrans](https://pypi.org/project/googletrans/).

Libraries Used:

pandas: for data manipulation and cleaning.
googletrans==4.0.0-rc1: for translating column names from Chinese to English.

re: for validating email addresses using regular expressions.

## Installation

Run the following command to install the required translation library:

```python
pip install googletrans==4.0.0-rc1
```
## Workflow Summary

1. Loading the Data: The dataset is read from a CSV file into a pandas DataFrame.
2. Column Translation: Column headers in Chinese are translated to English using the Google Translate API.
3. Column Normalization: Column names are converted to lowercase and spaces are replaced with underscores.
4. Column Removal: Unnecessary columns (e.g., frame_number, monthly_salary, etc.) are dropped.
5. Handling Missing Values:
 * Missing values in the post_code column are filled with 0.
 * Remaining missing values in other columns are filled with NA.
6. Duplicate Removal: Rows with duplicate id_card entries are removed.
7. Invalid Email Handling: Rows with invalid email addresses are identified and removed.
8. Exporting Results:
 * Cleaned data is exported to cleaned_data.csv.
 * Invalid rows (duplicates and invalid emails) are saved in a garbage.csv file.

## Usage
### 1. Loading the Dataset
```python
df = pd.read_csv('760k-Car-Owners-Nationwide-China-csv-2020.csv', low_memory=False)
```
The dataset is loaded, and basic information about the columns, data types, and memory usage is displayed using df.info().
### 2. Translating Column Headers
Using the googletrans library, each column name is translated from Chinese to English. If a translation fails, the original column name is kept.
```python
translator = Translator()
translated_col = translator.translate(col, dest='en').text
```
### 3. Normalizing Column Names
Column names are standardized by converting them to lowercase and replacing spaces with underscores, ensuring consistency and ease of use in analysis.
```python
def normalize_columns(df):
    new_columns = [column.lower().replace(' ', '_') for column in df.columns]
    df.columns = new_columns
    return df
```
### 4. Dropping Unnecessary Columns
Columns deemed irrelevant for analysis, such as frame_number, monthly_salary, and others, are dropped to reduce data complexity.
```python
df = df.drop(['frame_number', 'monthly_salary', 'educate', ...], axis=1)
```
### 5. Handling Missing Values
Missing post_code values are filled with 0 and converted to string.
Other missing values are replaced with 'NA' across the DataFrame.
```python
df['post_code'] = df['post_code'].fillna(0).astype(int).astype(str)
df.fillna('NA', inplace=True)
```
### 6. Removing Duplicates
Duplicates based on the id_card column are identified, and the first occurrence is retained. Duplicate rows are saved into a separate CSV for review.
```python
df_unique = df.drop_duplicates(subset=['id_card'], keep='first')
duplicates.to_csv('duplicate_id_cards.csv', index=False)
```
### 7. Invalid Email Handling
Invalid email addresses are identified using a regular expression pattern. These rows are removed from the cleaned dataset and exported for further inspection.
```python
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
invalid_emails_df = df_unique[~df_unique['mail'].str.match(email_pattern, na=False)]
invalid_emails_df.to_csv('rows_with_invalid_emails.csv', index=False)
```
### 8. Exporting Cleaned Data
The cleaned dataset is saved as cleaned_data.csv, while rows with duplicates and invalid emails are merged into garbage.csv.
```python
df_indexed.to_csv('cleaned_data.csv')
garbage_df.to_csv('garbage.csv', index=False)
```

## File Outputs
1. cleaned_data.csv: Contains the fully cleaned and validated dataset.
2. garbage.csv: A merged file containing rows with invalid email addresses and duplicate id_card entries.
3. duplicate_id_cards.csv and rows_with_invalid_emails.csv: Intermediate files for identifying specific issues during data cleaning.

## Final Notes
* Ensure you adjust file paths if needed when running the script in a different environment.
* Regular backups of intermediate files (garbage.csv, duplicate_id_cards.csv, etc.) are recommended for audit purposes.

## License

[MIT](https://choosealicense.com/licenses/mit/)
