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
        proxy_pass http://localhost:8080;
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
    
    # Wait for the command to finish
    exit_status = stdout.channel.recv_exit_status()
    out = stdout.read().decode('utf-8', errors='replace')
    err = stderr.read().decode('utf-8', errors='replace')
    if out:
        print(f"STDOUT:\n{out}")
    if err:
        print(f"STDERR:\n{err}")
    
    if exit_status != 0:
        print(f"Command failed with exit status {exit_status}")

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password, timeout=10)
    
    # 1. Install Docker
    execute_command(ssh, "curl -fsSL https://get.docker.com | sh")
    
    # 2. Stop and remove existing container if any
    execute_command(ssh, "docker stop portofolio-app || true")
    execute_command(ssh, "docker rm portofolio-app || true")
    
    # 3. Pull image
    execute_command(ssh, "docker pull akbarhrmwn/portofolio:latest")
    
    # 4. Run image
    execute_command(ssh, "docker run -d --name portofolio-app --restart always -p 8080:80 akbarhrmwn/portofolio:latest")
    
    # 5. Update Nginx configuration
    sftp = ssh.open_sftp()
    with sftp.file('/etc/nginx/sites-available/bukutamu', 'w') as f:
        f.write(nginx_conf)
    sftp.close()
    
    # 6. Reload Nginx
    execute_command(ssh, "nginx -t && systemctl reload nginx")
    
    ssh.close()
except Exception as e:
    print(f"Failed: {e}")
