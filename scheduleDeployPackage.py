#!/usr/bin/python3

from xmlrpc import client
import os
import sys
import datetime

HOST=""
USER=""
PASS=""

command = "puppet agent -t"
when = "2018-12-11 20:46:00"

client = client.Server(HOST)
key = client.auth.login(USER,PASS)

systemlist = client.systemgroup.listSystems(key, "Ubuntu")
pkglist = client.packages.findByNvrea(key, 'puppet', '5.4.0', '2ubuntu3', '', 'all')

systemsid = []

for system in systemlist:
    systemsid.append(system['id'])

client.system.scheduleScriptRun(key, systemsid, "root", "root", 300, command, when)
client.system.schedulePackageInstall(key, 1000000001, package_list[0]['id'], earliest_occurrence)

client.auth.logout(key)

