import json
import imaplib as imap
from email.header import decode_header
from pathlib import Path
import Email
import email
from email.policy import default

#TODO def read_email() => based on fetch_email_data() get the contents of the email

class IMAPClient:

    SECURE_PORT = 993 
    ENCRYPTION = imap.IMAP4_SSL

    # If you use a different email client, please enter put into this hash map
    VALID_DOMAINS = {"yahoo": "imap.mail.yahoo.com" , "outlook": "outlook.office365.com", "gmail": "imap.gmail.com"}

    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.username = None
        self.password = None
        self.client = None
        self.connection = None

    def fetch_credentials(self):
        if self.config_path.is_file():
            try:
                with open(self.config_path, "r", encoding="utf-8") as file:
                    credentials = json.load(file)
                    
                if "username" not in credentials or "password" not in credentials or "client" not in credentials:
                    print("Error: Username or Password or client is missing from config.json")
                    return None

                if credentials["client"] not in self.VALID_DOMAINS:
                    print("Error: invalid email client")
                    return None
                    
                self.username = credentials["username"]
                self.password = credentials["password"]
                self.client = self.VALID_DOMAINS[credentials["client"]]
                print("No errors were found when fecthing credentials")

            except json.JSONDecodeError:
                print("Error: fetching credentials. File not properly formatted")
        else:
            print("Error: 'config.json' is not found")

    def fetch_emails(self) -> list:
        emails = []
        if self.connection:
            try:
                self.connection.select('INBOX', readonly=True)
                status, searched_data = self.connection.search(None, "ALL")
                if status != "OK":
                    print("Error: Emails couldnt be fetched properly")
                    return emails
                email_ids = searched_data[0].split()
                email_ids.reverse() # Reversing so newest emails are first
                for id in email_ids:
                    # email data is not human readable so it needs to be parsed
                    status, email_data  = self.connection.fetch(id, "(BODY.PEEK[HEADER.FIELDS (SUBJECT DATE FROM)])")
                    if status != "OK":
                        print(f"Email {id} couldnt be retrieved")
                        continue

                    email_in_bytes = b""
                    for response_part in email_data:
                        if isinstance(response_part, tuple):
                            email_in_bytes = response_part[1]
                            break # Found the headers, move on

                    parsed_email = email.message_from_bytes(email_in_bytes, policy=default)

                    email_obj = Email.Email(
                            id = id.decode("utf-8"),
                            subject = parsed_email.get("Subject", ""),
                            sender = parsed_email.get("From", ""),
                            date = parsed_email.get("Date", "")
                        )  
                    emails.append(email_obj)
                return emails
            except Exception as e:
                print(f"Error: {e}")
                return emails


    def connect(self):
        if not self.username or not self.password or not self.client:
            print("Error: no username, password, or client found")
            return False

        try:
            print("Connecting...")
            mail = imap.IMAP4_SSL(self.client, self.SECURE_PORT)
            if mail.state == "NONAUTH":
                print("Successful Connection")

            print("Logging in...")
            status, _ = mail.login(self.username, self.password) 
            if status == "OK":
                print("Successful login")
                self.connection = mail
                return True
            else:
                print("Unsuccessful login")
                return False
        
        except Exception as e:
            print(f"An error occured: {e}")
            return False

    def read_email(self):
        # Go into the database and fetch the email, query by sender, date, id, etc
        # store this function in the Email body attribute: Email.body = read_email( arguments )
        print("todo")
