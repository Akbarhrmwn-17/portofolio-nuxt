import paramiko
import sys
import time
import io

# Fix windows stdout encoding issues for unicode characters like those npm prints
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

host = "103.253.213.209"
port = 22
username = "root"
password = "Akbar*123"

def execute_command(ssh, command):
    print(f"Executing: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    out = stdout.read().decode('utf-8', errors='replace')
    err = stderr.read().decode('utf-8', errors='replace')
    if out:
        print(f"STDOUT:\n{out}")
    if err:
        print(f"STDERR:\n{err}")
    return exit_status, out, err

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password, timeout=10)
    print("Connected successfully!")
    
    dir_path = "/var/www/portofolio-nuxt"
    print(f"Using project at: {dir_path}")
    
    # Run the deployment commands
    commands = [
        f"cd {dir_path} && git stash",
        f"cd {dir_path} && git pull origin main",
        f"cd {dir_path} && npm install --no-fund",
        f"cd {dir_path} && npm run build",
        f"cd {dir_path} && pm2 restart all"
    ]
    
    for cmd in commands:
        execute_command(ssh, cmd)
        
    ssh.close()
    print("Deployment finished successfully!")
    
except Exception as e:
    print(f"Failed: {e}")
    sys.exit(1)
