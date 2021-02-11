#!/bin/bash

sudo "$HOME/dnsfw/blocklists.py"
sudo service dnsmasq restart
