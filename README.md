# linux-user-manager
# Linux User Manager (CLI Tool)

This is a Python-based CLI tool to manage users, groups, sudo access, and permissions on a Red Hat Linux system.

## Features

- Add/delete users
- Add to groups
- Grant/revoke sudo access
- Set file permissions
- Dry-run mode for testing

## Usage

```bash
sudo python3 main.py add-user myuser --sudo
sudo python3 main.py delete-user myuser
sudo python3 main.py list-users
