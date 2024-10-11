![DataCleaning](DataCleaning.png)

This program cleans and prepares a dataset named "Lifebear.com - Largest Notebook App UsersDB" stored in a CSV file. Here's a breakdown of the steps:

**1. Library Imports:**

- `boto3` and `mysql-connector-python` (not used in this script, likely for optional database access).
- `pandas` for data manipulation.
- `numpy` (potentially unused here).
- `os`, `csv`, and `re` for file system and regular expression operations.
- `json`, `random`, `datetime`, `dateutil`, and `matplotlib` (potentially unused here).
- `mysql.connector` (potentially unused here).

**2. Data Loading and Initial Cleaning:**

- Reads the CSV file using `pandas.read_csv` with `;` as the delimiter and disables memory optimization (`low_memory=False`).
- Prints the number of missing values per column using `isnull().sum()`.
- Fills missing values in specific columns:
    - `login_id`: Replaced with "NA".
    - `gender`: Replaced with -1.0 (might indicate unknown).
    - `birthday_on`: Replaced with "NA".

**3. Duplicate Removal:**

- Identifies duplicate rows based on a combination of `login_id` and `mail_address` using `duplicated`.
- Saves duplicate rows to a separate CSV named "lifebear_dup_garbage.csv".
- Drops duplicate rows from the original dataframe using `drop_duplicates`.

**4. "created_at" Cleaning:**

- Assumes "created_at" contains datetime values.
- Converts "created_at" to date format only by extracting the date part using `pd.to_datetime().dt.date`.

**5. Column Renaming:**

- Renames specific columns using `rename` with `inplace=True` to modify the original dataframe.
  - `mail_address` to `e_mail_address`.
  - `created_at` to `created_on`.
  - `birthday_on` to `birthdate`.

**6. Invalid Email Handling:**

- Defines a function `is_valid_email` using regular expressions to validate email format.
- Filters rows with invalid emails using `~` (not) operator on the function applied to the `e_mail_address` column.
- Removes rows with invalid emails from the main dataframe.
- Saves those rows to a separate CSV named "invalid_email_addresses.csv".

**7. Merging Garbage Files:**

- Reads the two previously created CSV files containing duplicates and invalid emails.
- Concatenates them into a single dataframe using `pd.concat`.
- Saves the merged dataframe to a new CSV named "garbage.csv".

**8. Dataframe Reset and Text Cleaning:**

- Resets the index of the dataframe, effectively removing the previous row numbers.
- Converts all text in the `login_id` column to lowercase using `str.lower`.
- Removes leading and trailing whitespaces from the `login_id`, `password`, and `salt` columns using `str.strip`.

**9. Exporting Cleaned Data:**

- Saves the final cleaned dataframe to a CSV named "cleaned_lifebear_dataset.csv" using `to_csv` (without the index).

**Overall, this program cleans the "Lifebear.com" user dataset by handling missing values, removing duplicates, fixing date format, renaming columns, validating and removing invalid emails, merging temporary garbage files, cleaning text data, and finally exporting the cleaned data to a new CSV file.**
