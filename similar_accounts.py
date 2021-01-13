#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
from stdiomask import getpass
import instaloader

# decoration
print(stylize("\n---- | Get similar Instagram accounts | ----\n", fg("red")))

# class
class InstagramAccounts:
    def __init__(self, username, password, target):
        self.username = username
        self.password = password
        self.target = target

    # output magic method
    def __repr__(self):
        self.login(self.username, self.password)
        print(stylize(f"\n5 similar accounts as {self.target}:", fg("red")))
        return f"{self.get_accounts(self.target)}\n"

    # methods
    def login(self, username, password):
        # instagram session
        global session
        session = instaloader.Instaloader()
        session.login(username, password)
        return 0

    def get_accounts(self, target):
        similar_accounts = instaloader.Profile.from_username(session.context, target).get_similar_accounts()
        profiles = []
        for account in similar_accounts:
            profiles.append(account.username)
            if len(profiles) == 5:
                break
        return str(profiles)

# main execution
if __name__ == "__main__":
    # user interaction
    print(stylize("Instagram Login", fg("green")))
    insta_username = input("Username: ").lower()
    # hides password in the terminal
    insta_password = getpass(prompt = "Password: ")
    target = input("\nName of the target: ").lower()

    print(InstagramAccounts(insta_username, insta_password, target))
