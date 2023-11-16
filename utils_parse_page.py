# Get text from <div class="dsc">
def get_availability(row):
    return row.find('div', class_='dsc').text.strip()

# Get article title alternative titles
def get_synonyms(row):
    alt_names = row.find_all('a')
    names_list = []
    for alt_name in alt_names:
        if alt_name:
            name_text = alt_name.text.strip()
            name_href = alt_name.get('href')
            names_list.append([alt_name.text.strip(), alt_name.get('href')])
        else:
            name_text = None
            name_href = None
    return names_list

def get_rating(row):
    description = row.find("div", class_="dsc").text.strip().replace("\n", " ")
    return description if description else None


def get_other_names(row):
    description = {}  # Initialize an empty list to store the extracted data
    description['Description'] = row.find('div', class_='dsc').text.strip().split('\n')[0]   # Add the first line of the description
    # print(description)
    div_dsc = row.find('div', class_='dsc')
    # Extract the text content of the div and split it into lines
    lines = div_dsc.text.strip().split('\n')
    # Loop through each line to extract the information
    for i in range(len(lines) - 1):
        if "Registration name:" in lines[i]:
            registration_name = lines[i+1].strip()
            description["Registration Name"] = registration_name
        elif "Exhibition name:" in lines[i]:
            exhibition_name = lines[i+1].strip()
            description["Exhibition Name"] = exhibition_name
    
    return description

