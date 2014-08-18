#!/usr/bin/env bash

# this wget / dpkg is for 14.04 trusty ONLY -- modify as needed
wget http://apt.puppetlabs.com/puppetlabs-release-trusty.deb
sudo dpkg -i puppetlabs-release-trusty.deb

# now install the puppet version from apt-get to ensure 
# we have the latest version installed (it will update otherwise)
sudo apt-get update
sudo apt-get -y install puppet
puppet --version
