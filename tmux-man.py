#! /bin/python3

import os
from sys import argv
import subprocess

# Session creation
# tmux new-session -c <name> -s <starting-dir>
# == tm new <name> / tm new <name> <dir>
#
# Session deletion
# tmux kill-session -t <session-name>
# == tm kill <session-name>
# tmux kill-session -a -t <session-name>
# == tm kill -x <session-name>

argc = len(argv)
flags = [arg for arg in argv if arg.startswith("-")]
current_path = os.getcwd()

def new() -> int:
    if argc == 2:
        session_name = current_path.split("/")[-1]
        command = subprocess.run(f"tmux new-session -d -s {session_name} -c {current_path}".split())
        subprocess.run(f"tmux switch-client -t {session_name}".split())
    elif argc == 3:
        command = subprocess.run(f"tmux new-session -d -s {argv[2]} -c {current_path}".split())
        subprocess.run(f"tmux switch-client -t {argv[2]}".split())
    elif argc == 4:
        command = subprocess.run(f"tmux new-session -d -s {argv[2]} -c {argv[3]}".split())
        subprocess.run(f"tmux switch-client -t {argv[2]}".split())
    else:
        return 1
    return command.returncode

def kill() -> int:
    sessions = subprocess.getoutput("tmux list-sessions").split("\n")
    session_name = [session for session in sessions if session.endswith("(attached)")][0].split(":")[0]
    flag = "-a " if "-x" in flags else ""
    if argc == 2:
        command = subprocess.run(f"tmux kill-session {flag}-t {session_name}".split())
        return command.returncode
    elif argc == 3:
        session_name = argv[2]
        command = subprocess.run(f"tmux kill-session {flag}-t {session_name}".split())
        return command.returncode
    return 1

def main() -> int:
    if argv[1] == "new":
        return new()
    elif argv[1] == "kill":
        return kill()
    return 1

if __name__ == "__main__":
    if main() == 1:
        print("wrong command, buddy.")
