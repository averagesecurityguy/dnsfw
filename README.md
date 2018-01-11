# DNSFW
A simple DNS firewall.

## Installation

* Install dnsmasq on your favorite Linux computer (I built my DNS firewall on a RaspberryPi).
* Clone this repo to your home directory.
* Replace the default dnsmasq config file /etc/dnsmasq.conf with the one in this repo.
* Edit the dnsmasq.conf file to specify your upstream DNS server.
* Create the directory /opt/blacklists.
* Create the file /opt/blacklists/custom.list. Add to this file any custom domains you would like to block.
* Edit the blacklist.urls file with links to the blacklist files you want to download.
* Setup a cron job to run the update_bl.sh script as often as you like (I run it once a month).
* Configure your computer to use the new DNS server.
* Enjoy your Internet again.
