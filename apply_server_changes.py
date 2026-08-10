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

    root /var/www/portofolio-nuxt/.output/public;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
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
    
    # 1. Stop PM2 process
    execute_command(ssh, "pm2 stop BukuTamuKobar && pm2 save")
    
    # 2. Write new nginx config
    sftp = ssh.open_sftp()
    with sftp.file('/etc/nginx/sites-available/bukutamu', 'w') as f:
        f.write(nginx_conf)
    sftp.close()
    print("Nginx config updated successfully.")
    
    # 3. Reload Nginx
    execute_command(ssh, "nginx -t && systemctl reload nginx")
    
    ssh.close()
except Exception as e:
    print(f"Failed: {e}")
