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
    print("Connected successfully!")
    
    # Check nginx config for portofolio
    execute_command(ssh, "cat /etc/nginx/sites-enabled/portofolio* || grep -rn 'portofolio.theoverseer.cloud' /etc/nginx/")
    
    # Check directory contents
    execute_command(ssh, "ls -la /var/www/portofolio-nuxt")
    
    ssh.close()
except Exception as e:
    print(f"Failed: {e}")
