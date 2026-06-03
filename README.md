# Secure MyPass

A lightweight, terminal-based password manager that stores credentials securely on your local machine.

Secure MyPass is designed for developers, system administrators, DevOps engineers, and power users who prefer local credential management without cloud synchronization or external services.

## Features

* Local-first password management
* Master password protection
* Encrypted sensitive fields
* Dynamic credential fields
* Organize credentials into sections
* Fast terminal search
* Cross-platform support
* No cloud storage
* No external dependencies beyond Python packages
* Easy backup and migration

---

# Installation

## Recommended Installation

Install using pipx:

```bash
pipx install secure-mypass
```

If pipx is not installed:

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install pipx

pipx ensurepath
```

Restart your terminal and install:

```bash
pipx install secure-mypass
```

---

### Windows

Install:

```powershell
python -m pip install secure-mypass
```

## Alternative: Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate

pip install secure-mypass
```

---
##  Recommended GitHub Structure
```aiignore
secure-mypass/
│
├── docs/
│   └── images/
│       ├── workflow-overview.png
├── mypass/
├── README.md
└── pyproject.toml
```

## Workflow Overview

Figure 1: Complete Secure MyPass workflow — Initialize → Setup Master Password → Add Credentials → List → Search (masked) → Show (decrypted).

![Workflow](https://raw.githubusercontent.com/ravikempanayaka/mypass/main/docs/images/workflow-overview.png)


# First Time Setup

## Step 1: Initialize the Vault

```bash
mypass init
```

This creates:

```text
~/.mypass
```

---

## Step 2: Configure Master Password

```bash
mypass setup
```

Example:

```text
Create Master Password:
Confirm Master Password:
```

The master password is required whenever you:

* Add credentials
* View decrypted credentials
* Delete credentials
* Change the master password

---

# Daily Usage

## Add a Credential

```bash
mypass add
```

Example:

```text
Master Password:

Sections

1. Email Accounts
2. Cloud Accounts
0. New Section

Select: 0

Section Name: Email Accounts

System Name: Personal Mail

Field Name: Email
Email: user@example.com

Field Name: Password
Password:

Field Name:
```

Press Enter on an empty field name to finish.

---

## Search Credentials

Search without revealing secrets:

```bash
mypass search personal
```

Example:

```text
[Email Accounts]

Name: Personal Mail
Email: user@example.com
Password: ********
```

---

## Show Credential

Reveal encrypted values:

```bash
mypass show personal
```

Example:

```text
Master Password:

[Email Accounts]

Name: Personal Mail
Email: user@example.com
Password: MySecretPassword
```

---

## List All Credentials

```bash
mypass list
```

Example:

```text
[Email Accounts]
- Personal Mail

[Cloud Accounts]
- Development Account
```

---

## Delete a Credential

```bash
mypass delete personal
```

---

# Supported Dynamic Fields

You can store any field you want.

Examples:

```text
Email
Username
Password
URL
Token
API Key
Recovery Codes
Access Key
Secret Key
Database Host
Database User
Database Password
```

No predefined schema is required.

---

# Security

Secure MyPass uses a master password to protect sensitive data.

Sensitive fields are encrypted before being stored.

Examples:

```text
Password
Token
API Key
Recovery Codes
Secret Key
```

When searching:

```bash
mypass search personal
```

Sensitive values are hidden:

```text
Password: ********
```

When viewing:

```bash
mypass show personal
```

The master password is required before decryption.

---

# Storage Location

## Linux / macOS

```text
~/.mypass
~/.mypass.key
```

## Windows

```text
C:\Users\<username>\.mypass
C:\Users\<username>\.mypass.key
```

---

# Backup

Backup your vault:

```bash
cp ~/.mypass backup.mypass
cp ~/.mypass.key backup.key
```

To restore:

```bash
cp backup.mypass ~/.mypass
cp backup.key ~/.mypass.key
```

Important:

Both files are required.

Without `.mypass.key`, encrypted credentials cannot be decrypted.

---

# Commands

| Command                   | Description                        |
| ------------------------- | ---------------------------------- |
| `mypass init`             | Create vault file                  |
| `mypass setup`            | Configure master password          |
| `mypass add`              | Add a credential                   |
| `mypass list`             | List credentials                   |
| `mypass search <keyword>` | Search credentials (masked output) |
| `mypass show <keyword>`   | Show decrypted credential          |
| `mypass delete <keyword>` | Delete credential                  |

---

# Supported Platforms

* Ubuntu
* Debian
* Fedora
* CentOS
* macOS
* Windows Command Prompt
* Windows PowerShell

---

# Why Secure MyPass?

Many password managers depend on cloud synchronization, browser extensions, or subscriptions.

Secure MyPass focuses on:

* Local storage
* Terminal workflow
* Simplicity
* Speed
* Developer productivity

Your credentials remain under your control at all times.

---

# License

MIT License

---

# Author

Ravi K
