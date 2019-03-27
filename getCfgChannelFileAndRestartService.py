#!/usr/bin/python3

from xmlrpc import client
import os
import sys
import subprocess

# Spacewalk server
HOST=""
USER=""
PASS=""

cmd_get = "rhncfg-client get /etc/postfix/main.cf"

client = client.Server(HOST)
key = client.auth.login(USER,PASS)
systemlist = client.systemgroup.listSystems(key, "Production")

output=[]

for system in systemlist:
    systemdetails = client.system.getDetails(token, system['id'])
    ssh = subprocess.Popen(["/usr/bin/ssh", "-q", "-o", "ConnectTimeout 5", "-o", "StrictHostKeyChecking no", "-i", "/root/.ssh/id_rsa", "%s" % system['name'], cmd_get], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
    else:
        for line in result:
            print(system['name']+" "+line.strip().decode())


    if systemdetails['release'] == "7Server":
        command="systemctl restart postfix.service"
    else:
        command="service postfix restart"

    ssh = subprocess.Popen(["/usr/bin/ssh", "-q", "-o", "ConnectTimeout 3", "-o", "StrictHostKeyChecking no", "-i", "/root/.ssh/id_susemanager", "%s" % system['name'], command], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    for line in result:
        print(line.strip().decode())
    resulterr = ssh.stderr.readlines()
    for line in resulterr:
        print(line.strip().decode())

client.auth.logout(key)


