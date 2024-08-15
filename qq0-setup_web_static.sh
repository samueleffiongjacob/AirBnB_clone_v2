#!/usr/bin/env bash
# Sets up a web server for the deployment of web_static.

# Exit on any error
set -e

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Function to print messages in green for success
function success_message() {
    echo -e "${GREEN}$1${NC}"
}

# Function to print messages in red for errors
function error_message() {
    echo -e "${RED}$1${NC}"
}

# Trap any error and print an error message
trap 'error_message "An error occurred. Exiting..."' ERR

# Install Nginx if it's not already installed
echo "Installing Nginx if not already installed..."
if ! dpkg -l | grep -q nginx; then
    apt-get update
    apt-get install -y nginx
fi
success_message "Nginx installed."

# Create the required directories
echo "Creating directories..."
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
success_message "Directories created."

# Create a fake HTML file to test the configuration
echo "Creating fake HTML file..."
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
success_message "Fake HTML file created."

# Create the symbolic link, ensuring it's recreated if it already exists
echo "Creating symbolic link..."
ln -sf /data/web_static/releases/test/ /data/web_static/current
success_message "Symbolic link created."

# Give ownership of the /data/ directory to the ubuntu user and group recursively
echo "Setting ownership of /data/ to ubuntu user and group..."
chown -R ubuntu:ubuntu /data/
success_message "Ownership set."

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
echo "Updating Nginx configuration..."
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;

    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-available/default
success_message "Nginx configuration updated."

# Restart Nginx to apply the new configuration
echo "Restarting Nginx..."
service nginx restart
success_message "Nginx restarted. Setup complete."
