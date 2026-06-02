# Secure MyPass

A lightweight and secure local password manager for Linux/macOS terminals.

Secure MyPass allows you to store and search credentials directly from your terminal using a simple text-based database located in your home directory.

No cloud storage. No external servers. No account required.

## Features

* Store credentials locally in `~/.mypass`
* Fast keyword search from the terminal
* Organize credentials into sections
* Simple and lightweight
* No internet dependency
* No vendor lock-in
* Easy backup and migration
* Linux and macOS friendly

## Installation

```bash
pip install secure-mypass
```

## Create Password Store

Create a file named:

```bash
~/.mypass
```

Example:

```ini
[SSO Login]
Name: Portal SSO
Url: https://abc.com
UserName: ravi
Password: mypassword

Name: Terminal SSO
Command: aws configure sso

[Microsoft Email Services]
Name: Provenio Mail
Email: ravi@example.com
Password: mysecretpassword

Name: Enkefalos Mail
Email: ravi@example.com
Password: anotherpassword
```

## Usage

Search by section name:

```bash
mypass provenio
```

Output:

```text
[Microsoft Email Services]

Name: Provenio Mail
Email: ravi@example.com
Password: ********
```

Search by email:

```bash
mypass ravi@example.com
```

Search by service name:

```bash
mypass enkefalos
```

## File Location

Secure MyPass always reads credentials from:

```bash
~/.mypass
```

This ensures credentials remain under your control and can easily be backed up using Git, Dropbox, OneDrive, rsync, or any preferred method.

## Security Notes

* All data is stored locally on your machine.
* No credentials are transmitted over the internet.
* No external services are used.
* Restrict file access:

```bash
chmod 600 ~/.mypass
```

Recommended permissions:

```text
-rw------- ~/.mypass
```

## Example Alias

Add to your `.bashrc` or `.zshrc`:

```bash
alias mypass="python3 ~/mypass_cli.py"
```

Or install from PyPI and use directly:

```bash
mypass provenio
```

## Use Cases

* AWS SSO accounts
* Email credentials
* Internal portals
* Database logins
* Development environments
* Personal projects
* Infrastructure credentials

## Why Secure MyPass?

Many password managers require cloud synchronization, subscriptions, or browser integrations.

Secure MyPass follows a different philosophy:

* Local-first
* Terminal-first
* Simple
* Fast
* Developer-friendly

Perfect for engineers, DevOps professionals, system administrators, and developers who prefer local credential management.

## License

MIT License

## Author

Ravi K

Lead Software Engineer

Python | Django | FastAPI | AWS | PostgreSQL
