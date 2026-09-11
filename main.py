import imapConnection
import emaildb

imap = imapConnection.IMAPClient("config.json")
imap.fetch_credentials()
imap.connect()
imap.fetch_inbox()

db = emaildb.Database()
db.store_emails(imap.fetch_emails())