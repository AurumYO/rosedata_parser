
class URLPages:
    """Class to store URLs with letters as keys and URLs as values."""
    def __init__(self):
        "Initiate dictionary with lettes and URLs to pages starting from this letter."
        self.pages = {
            "A": "https://www.helpmefind.com/rose/plants.php?grp=A&t=2",
            "B": "https://www.helpmefind.com/rose/plants.php?grp=B&t=2",
            "C": "https://www.helpmefind.com/rose/plants.php?grp=C&t=2",
            "D": "https://www.helpmefind.com/rose/plants.php?grp=D&t=2",
            "E": "https://www.helpmefind.com/rose/plants.php?grp=E&t=2",
            "F": "https://www.helpmefind.com/rose/plants.php?grp=F&t=2",
            "G": "https://www.helpmefind.com/rose/plants.php?grp=G&t=2",
            "H": "https://www.helpmefind.com/rose/plants.php?grp=H&t=2",
            "I": "https://www.helpmefind.com/rose/plants.php?grp=I&t=2",
            "J": "https://www.helpmefind.com/rose/plants.php?grp=J&t=2",
            "K": "https://www.helpmefind.com/rose/plants.php?grp=K&t=2",
            "L": "https://www.helpmefind.com/rose/plants.php?grp=L&t=2",
            "M": "https://www.helpmefind.com/rose/plants.php?grp=M&t=2",
            "N": "https://www.helpmefind.com/rose/plants.php?grp=N&t=2",
            "O": "https://www.helpmefind.com/rose/plants.php?grp=O&t=2",
            "P": "https://www.helpmefind.com/rose/plants.php?grp=P&t=2",
            "Q": "https://www.helpmefind.com/rose/plants.php?grp=Q&t=2",
            "R": "https://www.helpmefind.com/rose/plants.php?grp=R&t=2",
            "S": "https://www.helpmefind.com/rose/plants.php?grp=S&t=2",
            "T": "https://www.helpmefind.com/rose/plants.php?grp=T&t=2",
            "U": "https://www.helpmefind.com/rose/plants.php?grp=U&t=2",
            "V": "https://www.helpmefind.com/rose/plants.php?grp=V&t=2",
            "W": "https://www.helpmefind.com/rose/plants.php?grp=W&t=2",
            "X": "https://www.helpmefind.com/rose/plants.php?grp=X&t=2",
            "Y": "https://www.helpmefind.com/rose/plants.php?grp=Y&t=2",
            "Z": "https://www.helpmefind.com/rose/plants.php?grp=Z&t=2"
        }


    def get_letter_pages(self, letter):
        "Return the URL with pages starting from the specific letter."
        return self.pages.get(letter, None)
