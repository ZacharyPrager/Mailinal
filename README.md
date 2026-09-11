# Terminal Mail Client (In Progress) 🛠️

A minimal terminal-based mail client that transforms your email inbox into a local, searchable **email file system**. Instead of a messy list, your emails are dynamically organized by **sender into directories**, allowing you to navigate your inbox using native terminal commands.

---

## 🚀 The Core Idea

This client syncs with your IMAP server and maps your inbox directly into a structured folder hierarchy. 

📂 **How your inbox looks on your machine:**
```text
🗁 mail_root/
├── 🗁 support@://github.com
│   ├── 📄 2026-09-10_security_alert.eml
│   └── 📄 2026-09-01_weekly_digest.eml
├── 🗁 boss@://company.com
│   ├── 📄 2026-09-11_urgent_meeting.eml
│   └── 📄 2026-09-05_project_update.eml
└── 🗁 newsletter@://tech.com
    └── 📄 2026-08-30_ai_trends.eml
```

Instead of using a clunky UI, you manage your mail using commands you already know:
* `cd support@github.com` to view your history with GitHub.
* `cat 2026-09-10_security_alert.eml` to read the email body.
* `grep -r "invoice" .` to search for keywords across all senders.

---

## ✨ Features (Current & Planned)

* **Directory-per-Sender Organization** – Automatic sorting of incoming mail into human-readable sender folders.
* **On-Demand Body Fetching** – Lazy loading that pulls the full email text only when you explicitly open/read the file.
* **Multi-Folder Support** – Modular mapping for `INBOX`, `Sent`, `Drafts`, and custom provider folders.
* **Pure Terminal Workflow** – Zero reliance on heavy graphical interfaces or web browsers.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **Core Libraries:** `smtplib`, `imaplib`, `email`
* **Authentication:** Requires an **App Password** from your email provider (Gmail, Outlook, Yahoo, etc.) with IMAP access enabled.

---

## 🏗️ Project Status

> [!NOTE]  
> This project is currently **in progress**. The core IMAP connection, header fetching, and modular folder selection mechanisms are implemented. Next steps include perfecting the local virtual file system wrapper and handling multi-part attachment rendering.
