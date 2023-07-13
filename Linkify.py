from GreetUser import GreetUser
from InstallModules import InstallModules
import importlib


def main_loop():
    while True:
        user_url = input("Enter a valid URL: ")

        if user_url.lower() == "exit":
            return "Enjoy the rest of your day.."
        else:
            try:
                linkify = importlib.import_module("pyshorteners")
                new_link = linkify.Shortener().tinyurl.short(user_url)
                print(new_link)
            except Exception:
                print("Invalid URL..")
            

if __name__ == "__main__":
    InstallModules.install_module("pyshorteners")
    print(GreetUser.greet_user())
    print(main_loop())
