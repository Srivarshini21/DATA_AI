import subprocess

servers = ["8.8.8.8", "google.com"]

for server in servers:
    subprocess.run(["ping", "-n", "1", server])
