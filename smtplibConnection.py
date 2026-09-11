import smtplib
from email.message import EmailMessage
import json

class SMTPClient:

    def __init__(self, config_path):
        self.config_path = config_path
        self.username = None
        self.password = None

    def fetch_credentials(self):
        if self.config_path.is_fike():
            try:
                with open(self.config_path, "r", encoding="utf-8") as file:
                    credentials = json.load(file)

                if "username" not in credentials or "password" not in credentials or "client" not in credentials:
                    print("Error: Username or Password or client is missing from config.json")
                    return None          

                self.username = credentials["username"]
                self.password = credentials["password"]

                print("No errors were found when fetching credentials")
            except json.JSONDecodeError:
                print("Error: fetching credentials. File not properly formatted")
        else:
            print("Error: 'config.json' is not found")
            