import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

from parse_pages import URLPages
from user_interaction import ask_user_for_letter, ask_user_for_domain_name



# Prompt user to enter the letter to work with and obtain the url to parse
letter_input = ask_user_for_letter()
url_pages = URLPages()
url = url_pages.get_letter_pages(letter_input)

if url:
    print(f"The URL for pages starting with '{letter_input}' is: {url}")
else:
    print(f"No URL found for the letter '{letter_input}'.")

# Parse the pages for articles starting from this letter and 
# obtain the title of the articles and the url of the article.
# After short exploration we noticed that the articles "href" atribute contains only 
# shortend path, without domain,
# therefore we define domain name to add to the shortened URL path.
# domain = ask_user_for_domain_name()
domain = "https://www.helpmefind.com"
# the results of parsing will be stored in the dictionary
articles = {}

# Parse the URL for the articles
while True:
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.content, "html.parser")
    results = soup.find_all("div", class_="bg bgA plant")

    for job_element in results:
        links = job_element.find_all("a")
        for link in links:
            link_url = domain + link["href"]
        # add article title and URL    
        articles[link.string] = link_url
    
    # Check if there are next page with the articles, and if
    # there are such next pages continue parsing else end parsing
    next_buton = soup.find("a", string="MORE  »")
    sleep(4)
    if next_buton:
        url = domain + next_buton["href"]
    else:
        break


# Create a DataFrame from the dictionary
df = pd.DataFrame(list(articles.items()), columns=["Rose Name", "URL"])

# Save the DataFrame to an Excel file
excel_file_path = "roses_data_" + letter_input + ".xlsx"
df.to_excel(excel_file_path, index=False)

print(f"Data has been saved to {excel_file_path}")
