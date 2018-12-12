#!/usr/bin/python3

from xmlrpc import client
import os
import sys

HOST=""
USER=""
PASS=""

command = "uname -a"

client = client.Server(HOST)
key = client.auth.login(USER,PASS)
systemlist = client.system.listSystems(key)

output=[]

for system in systemlist:
    systemdetails = client.system.getDetails(token, system['id'])
    ssh = subprocess.Popen(["/usr/bin/ssh", "-q", "-o", "ConnectTimeout 5", "-o", "StrictHostKeyChecking no", "-i", "/root/.ssh/id_rsa", "%s" % system['name'], command], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
    else:
        for line in result:
            systeminfo = system['name']+";"+line.strip().decode()
            output.append(systeminfo)


client.auth.logout(key)


