#! /bin/bash

sudo apt update
sudo apt upgrade -y
sudo apt install apache2 -y
sudo mkdir /helloapp
sudo echo "Hello world!" > /var/www/html/index.html
curl localhost > /helloapp/index.html
