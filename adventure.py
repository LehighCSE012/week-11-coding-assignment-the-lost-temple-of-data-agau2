"""
Week 11 Coding Assignment: The Lost Temple of Data
"""

import re
import pandas as pd

def load_artifact_data(excel_filepath):
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    """
    # Hint: Use pd.read_excel, specify sheet_name and skiprows
    # Replace 'pass' with your code
    artifact_data = pd.read_excel(excel_filepath, sheet_name = 'Main Chamber', skiprows = 3)

    # return the resulting DataFrame
    return artifact_data

def load_location_notes(tsv_filepath):
    """
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    """
    # Hint: Use pd.read_csv, specify the separator for tabs ('\t')
    # Replace 'pass' with your code
    location_data = pd.read_csv(tsv_filepath, sep='\t')

    # return the resulting DataFrame
    return location_data

def extract_journal_dates(journal_text):
    """
    Extracts all dates in MM/DD/YYYY format from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of date strings found in the text.
    """
    # Hint: Use re.findall with a raw string pattern for MM/DD/YYYY format.
    # Pattern idea: r"\d{2}/\d{2}/\d{4}"
    # Replace 'pass' with your code
    date_pattern = r'[01]\d/(?:[0-2]\d|3[01])/\d{4}'
    dates_list = re.findall(date_pattern, journal_text)

    # return the list of found dates
    return dates_list

def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    """
    # Hint: Use re.findall with a raw string pattern for AZMAR- followed by 3 digits.
    # Pattern idea: r"AZMAR-\d{3}"
    # Replace 'pass' with your code
    code_pattern = r'AZMAR-\d{3}'
    secret_codes_list = re.findall(code_pattern, journal_text)

    # return the list of found codes
    return secret_codes_list
