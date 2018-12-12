#!/usr/bin/python3

from xmlrpc import client
import os
import sys
import datetime

HOST=""
USER=""
PASS=""

command = "puppet agent -t"
when = "2018-12-11 21:00:00"

client = client.Server(HOST)
key = client.auth.login(USER,PASS)

systemlist = client.systemgroup.listSystems(key, "CentOS7")

systemsid = []

for system in systemlist:
    systemsid.append(system['id'])

client.system.scheduleScriptRun(key, systemsid, "root", "root", 300, command, when)

client.auth.logout(key)

