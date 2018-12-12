#!/usr/bin/python3

from xmlrpc import client
import os
import sys

HOST=""
USER=""
PASS=""

client = client.Server(HOST)
key = client.auth.login(USER,PASS)
systemlist = client.system.listSystems(key)

client.auth.logout(key)


