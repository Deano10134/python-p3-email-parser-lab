# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        """
        Find email addresses in the provided text and return them sorted alphabetically.
        Matches emails like: local@domain.tld
        Local part must start with a letter and can contain letters, digits and ._%+-.
        """
        pattern = re.compile(r'[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
        matches = pattern.findall(self.text)
        # remove duplicates and return sorted list
        return sorted(set(matches))

# (optional) retained fallback regex if other code expects this name
email_regex = re.compile(r'^[a-z][a-z0-9._%+-]*@[a-z0-9.-]+\.[a-z]{2,}$')
