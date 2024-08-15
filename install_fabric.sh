#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting the installation of Fabric 1.14.post1 for Python 3..."

# Check if pip3 is installed, if not, install it
if ! command -v pip3 &> /dev/null; then
    echo "pip3 could not be found. Installing pip3..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Uninstall any existing Fabric installation
echo "Uninstalling any existing Fabric version..."
pip3 uninstall -y Fabric || echo "Fabric not installed, skipping uninstallation."

# Install necessary dependencies
echo "Installing required dependencies..."
sudo apt-get update
sudo apt-get install -y libffi-dev libssl-dev build-essential python3.8-dev

# Install Python packages
echo "Installing Python packages..."
pip3 install pyparsing appdirs setuptools==40.1.0
pip3 install cryptography==2.8 bcrypt==3.1.7 PyNaCl==1.3.0

# Install Fabric 1.14.post1
echo "Installing Fabric 1.14.post1..."
pip3 install Fabric3==1.14.post1

# Update PATH to include local bin directory
echo 'export PATH=$PATH:$HOME/.local/bin' >> ~/.bashrc
source ~/.bashrc

# Verify installation
echo "Verifying Fabric installation..."
fab --version || echo "Failed to find 'fab' command. Check PATH or installation."

# Optionally clean up unused packages
echo "Cleaning up unused packages..."
sudo apt autoremove -y

echo "Fabric 1.14.post1 installation completed successfully."
