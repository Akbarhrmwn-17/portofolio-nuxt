import paramiko
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

host = "103.253.213.209"
port = 22
username = "root"
password = "Akbar*123"

def execute_command(ssh, command):
    print(f"Executing: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read().decode('utf-8', errors='replace')
    err = stderr.read().decode('utf-8', errors='replace')
    if out:
        print(f"STDOUT:\n{out}")
    if err:
        print(f"STDERR:\n{err}")

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password, timeout=10)
    
    # 1. List sites-enabled
    execute_command(ssh, "ls -la /etc/nginx/sites-enabled/")
    
    # 2. Cat the config for theoverseer.cloud
    execute_command(ssh, "grep -rn 'theoverseer.cloud' /etc/nginx/sites-enabled/")
    
    # 3. Check pm2 list
    execute_command(ssh, "pm2 list")
    
    ssh.close()
except Exception as e:
    print(f"Failed: {e}")
