# CIS-117 Lab3
# Write a description of your module here
# Rhea Misra
import csv
import re
from collections import defaultdict

INPUT_FILE = "country_full.csv"

def read_countries(filename):
  """
  Read the input CSV and group country names by region. 
  Returns a dictionary.
  """
  countries_by_region = {}
  try:
    with open(filename, "r", newline="", encoding="utf-8") as input_file:
      reader = csv.DictReader(input_file)
      if reader.fieldnames is None:
        raise ValueError("The CSV file does not have headers.")
      if "region" not in reader.fieldnames:
        raise ValueError("The CSV file is missing the 'region' column.")
      for row in reader:
        country_name = row("name").strip()
        region = row("region").strip()
        if country_name == "" or region == "":
          continue
        if region not in countries_by_region:
          countries_by_region[region] = []
        countries_by_region[region].append(country_name)
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

def write_region_files(countries_by_region):
  """
  Write one CSV file for each region."""
  for region, country_names in countries_by_region.items():
    output_filename = clean_filename(region)

    try:
      with open(
        output_filename,
        "w",
        newline="",
        encoding="utf-8"
      ) as output_file:
        writer = csv.writer(output_file)
        for country_name in country_names:
          writer.writerow([country_name, region])
        print(f"Created: {output_filename}")
    except PermissionError:
      print(
        f"Error: Permission denied when writing "
        f"'{output_filename}'."
      )
    except IOError as error:
      print(f"I/O error while writing '{output_filename}': {error}")
  
def main():
  """Run the program."""
  countries_by_region = read_countries(INPUT_FILE)
  if countries_by_region:
    write_region_files(countries_by_region)
    print("Finished creating the regional files.")
  else:
    print("No regional files were created.")
  
main()
