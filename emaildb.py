import sqlite3
import Email

class Database:

    def __init__(self, db_name: str= "email.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS emails(
                    id TEXT PRIMARY KEY,
                    subject TEXT,
                    sender TEXT,
                    date TEXT
                
                )
            '''
        )
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_sender ON emails(sender)')
        self.connection.commit()   

    def store_emails(self, emails: list[Email.Email]):
        for email in emails:
            self.cursor.execute(
                '''
                    INSERT OR REPLACE INTO emails (id, sender, subject, date)
                    VALUES(?, ?, ?, ?)
                '''
            , (email.id, email.sender, email.subject, email.date))
            self.connection.commit()
        print("Emails added")

    