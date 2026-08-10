import paramiko
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

host = "103.253.213.209"
port = 22
username = "root"
password = "Akbar*123"

nginx_conf = """server {
    server_name theoverseer.cloud;

    location / {
        proxy_pass http://localhost:8081;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/theoverseer.cloud/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/theoverseer.cloud/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}
server {
    if ($host = theoverseer.cloud) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    listen 80;
    server_name theoverseer.cloud;
    return 404; # managed by Certbot
}
"""

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

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password, timeout=10)
    
    # 1. Clean up failed container
    execute_command(ssh, "docker rm -f portofolio-app")
    
    # 2. Run container on port 8081 instead
    execute_command(ssh, "docker run -d --name portofolio-app --restart always -p 8081:80 akbarhrmwn/portofolio:latest")
    
    # 3. Update Nginx configuration to point to 8081
    sftp = ssh.open_sftp()
    with sftp.file('/etc/nginx/sites-available/bukutamu', 'w') as f:
        f.write(nginx_conf)
    sftp.close()
    
    # 4. Reload Nginx
    execute_command(ssh, "nginx -t && systemctl reload nginx")
    
    ssh.close()
except Exception as e:
    print(f"Failed: {e}")
