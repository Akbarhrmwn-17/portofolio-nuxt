import paramiko
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

host = "103.253.213.209"
port = 22
username = "root"
password = "Akbar*123"

def execute_command(ssh, command):
    print(f"\n--- Executing: {command} ---")
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read().decode('utf-8', errors='replace').strip()
    err = stderr.read().decode('utf-8', errors='replace').strip()
    if out:
        print(f"STDOUT:\n{out}")
    if err:
        print(f"STDERR:\n{err}")

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password, timeout=10)
    
    execute_command(ssh, "uptime")
    execute_command(ssh, "docker ps -a")
    execute_command(ssh, "pm2 list")
    execute_command(ssh, "ls -la /var/www/")
    execute_command(ssh, "systemctl status nginx --no-pager | head -n 10")
    
    ssh.close()
except Exception as e:
    print(f"Failed to connect or execute: {e}")
