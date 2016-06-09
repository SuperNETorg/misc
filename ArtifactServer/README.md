### ARTIFACT SERVER SETUP USING NGINX
Steps to setup artifact server using NGINX and Letsencrypt on Ubuntu 14.04.
Assumption artifact server address is `artifacts.supernet.org`

Step 1. Install nginx server

`sudo apt-get install nginx -y`

Step 2. Copy `default` file from this repo to `/etc/nginx/sites-available/`

`sudo cp default /etc/nginx/sites-available`

Step 3. Install letsencrypt 
- `sudo mkdir -p /usr/share/nginx/html/.well-known`
- `sudo apt-get update`
- `sudo apt-get -y install git bc`
- `sudo git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt`
- `cd /opt/letsencrypt`
- `./letsencrypt-auto certonly -a webroot --webroot-path=/usr/share/nginx/html -d "artifacts.supernet.org"`
- Follow the onscreen option of letsencrypt to complete the setup
- `sudo ls -l /etc/letsencrypt/live/artifacts.supernet.org`

Step 4. Generate Strong Diffie-Hellman Group

`sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048`

Step 5. Reload NGINX configs

`sudo service nginx reload`

if all above steps are executed without any problem then artifact server should start without any problem.

Location where all files reside is /usr/share/nginx/html/
Make sure to copy all artefacts to this location
