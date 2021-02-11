#!/bin/bash

sudo "$HOME/blocklists.py"
sudo service dnsmasq restart
