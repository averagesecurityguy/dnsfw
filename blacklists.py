#!/usr/bin/env python

import requests
import os
import re

# Constants
TEMP_FILE = "/tmp/master.list"
PERM_FILE = "/opt/blacklists/master.list"
WL_FILE = "whitelist.list"
BL_FILE = "blacklist.urls"

# Globals
ip_re = re.compile(r'^[0-9.]+$')
comment_re = re.compile(r'\s*#.*$')
uniq = set()


def load_file(filename):
    items = []

    with open(filename) as f:
        for line in f:
            items.append(line.strip())

    return items


def write(domains):
    with open(TEMP_FILE, "a") as f:
        f.write(domains)


def clean(domains):
    whitelist = load_file(WL_FILE)
    new = []

    for domain in domains:
        # Remove comments and empty lines
        if domain.startswith("#"):
            continue

        if domain == "":
            continue

        # Remove comments at the end of a line
        domain = comment_re.sub("", domain)

        # Get the domain, which should be at the end of the line.
        parts = domain.split()

        if parts == []:
            continue

        parts.reverse()
        domain = parts[0]

        # Remove whitelisted domains
        if domain in whitelist:
            continue

        if domain != "" and domain != "localhost":
            new.append("127.0.0.1 {0}".format(domain))

    return new


def main():
    # Get file list
    urls = load_file(BLURL_FILE)

    # Download, clean, and unique domains.
    for url in urls:
        try:
            resp = requests.get(url)
        except:
            continue

        domains = resp.content.split("\n")
        write('\n'.join(clean(domains)))

    # Move the master.list from /tmp to /opt/blacklists
    os.rename(TEMP_FILE, PERM_FILE)

if __name__ == '__main__':
    main()
