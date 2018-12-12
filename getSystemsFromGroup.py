#!/usr/bin/python3

from xmlrpc import client
import os
import sys

HOST=""
USER=""
PASS=""

client = client.Server(HOST)
key = client.auth.login(USER,PASS)

systemlist = client.systemgroup.listSystems(key, "CentOS7")

client.auth.logout(key)

