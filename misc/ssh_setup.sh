#!/usr/bin/env bash

# this will work with apt-get distros
sudo apt-get install openssh-server

# ensure the ssh service is started and default port (22) allowed
sudo service ssh start
sudo ufw allow 22
sudo ufw enable
