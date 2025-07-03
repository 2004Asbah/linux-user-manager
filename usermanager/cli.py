import subprocess
import typer
from rich import print

app = typer.Typer()

def run(cmd: list[str], dry: bool = False):
    """Execute shell commands with optional dry run."""
    cmd_str = ' '.join(cmd)
    if dry:
        print(f"[yellow]DRY RUN:[/yellow] {cmd_str}")
    else:
        print(f"[green]$ {cmd_str}[/green]")
        subprocess.run(cmd, check=True)

@app.command()
def add_user(username: str, sudo: bool = False, dry: bool = False):
    """Add a new user and optionally grant sudo."""
    run(["sudo", "useradd", "-m", username], dry)

    if sudo:
        sudo_line = f"{username} ALL=(ALL) NOPASSWD:ALL\n"
        run(["sudo", "bash", "-c", f"echo '{sudo_line}' > /etc/sudoers.d/{username}"], dry)
        run(["sudo", "visudo", "-c", "-f", f"/etc/sudoers.d/{username}"], dry)

@app.command()
def delete_user(username: str, dry: bool = False):
    """Delete a user and their home directory."""
    run(["sudo", "userdel", "-r", username], dry)

@app.command()
def add_to_group(username: str, group: str, dry: bool = False):
    """Add user to a group."""
    run(["sudo", "usermod", "-aG", group, username], dry)

@app.command()
def set_permissions(path: str, perms: str, dry: bool = False):
    """Set permissions on a path (e.g., 755)."""
    run(["sudo", "chmod", perms, path], dry)

@app.command()
def list_users():
    """List all system users."""
    with open("/etc/passwd") as f:
        for line in f:
            print(line.split(":")[0])

@app.command()
def list_sudoers():
    """List members of the 'wheel' group (sudo)."""
    run(["getent", "group", "wheel"])


