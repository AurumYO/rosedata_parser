import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

from utils_parse_page import get_availability, get_synonyms,\
    get_rating, get_other_names

# Insert here the path to the file with data to parse
excel_file_path = 'roses_data_M.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Display the DataFrame
# print(df)

# Access columns
selected_rows = df[['Rose Name', 'URL']].iloc[5000:8000]

# Store the parsed data to the roses_data directory
base_directory = 'roses_data/'
## Create the directory if it doesn't exist
# os.makedirs(excel_file_path, exist_ok=True)

for index, row in selected_rows.iterrows():
    rose_name = row['Rose Name']
    url = row['URL']
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "html.parser")

    if row['Rose Name'] == None or row['Rose Name'] == '':
        # Get the title of the article
        page_title = soup.select('div#title')
        for element in page_title:
            span_element = element.find("span")
            if span_element is not None:
                raw_title = span_element.text
                # Extract text between single quotes and remove registered symbol
                try:
                    rose_name = raw_title.replace(" ®", "")
                except IndexError:
                    rose_name = raw_title
                # print("Title text", title_text)
            else:
                print("No span element found within div#title.")

    print("Parsing page ", rose_name, " .....")

    # Find all div class="row" witch contain information about specific field
    # Create lists to store the data
    headings = []
    descriptions = []
    # Find all <div class="row"> elements
    article_content = soup.find_all("div", class_="row")

    for row in article_content:
        heading = row.find('div', class_='hdg').text.strip()
        # Get commercial availability of the variety
        if heading == "Availability:":
            description = get_availability(row)
        # Get the list of all alternative names of the variety
        if heading == "Synonyms:":
            description = get_synonyms(row)
        # Obtain overal rating of the variety 
        if heading == "HMF Ratings:":
            description = get_rating(row)
        if heading == "ARS:":
            description  = get_other_names(row)    
        else:
            description = row.find('div', class_='dsc').text.strip()
            # print(description)
        # Append the values to the lists
        headings.append(heading)
        descriptions.append(description)

    # Create a DataFrame using pandas
    data = {'Heading': headings, 'Description': descriptions}
    df = pd.DataFrame(data)
    # print(df)


    # Save the DataFrame to an Excel file
    rose_name = rose_name.replace('/', '-')
    rose_name = rose_name.replace('"', '')
    rose_name = rose_name.replace(' ', '_')
    excel_file_path = os.path.join(base_directory, f"rose_{rose_name}.xlsx")
    # print(excel_file_path)
    df.to_excel(excel_file_path, index=False)

    print(f"Data has been saved to {excel_file_path}")

