
def ask_user_for_letter():
    "Ask user for URL and a letter for scrapping, return the url and the letter."
    while True:
        letter = input("Please enter the letter we are working with today: ")
        if len(letter) == 1 and letter.isalpha():
            return letter.upper()
        else:
            print("Invalid input. Please enter a single alphabetical character!")


def ask_user_for_domain_name():
    "Ask user to provide the domain name"
    domain_name = input("Please enter the domain name: ")
    if domain_name == "" or domain_name == None:
        return "https://www.helpmefind.com"
    else:
        return domain_name
