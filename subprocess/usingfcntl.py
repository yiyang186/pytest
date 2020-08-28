#!/usr/bin/python                                                                                                                                                      
# -*- coding: utf-8 -*-
# author: 
from subprocess import Popen, PIPE
import select
import fcntl, os
import time

class Server(object):
  def __init__(self, args, server_env = None):
    if server_env:
      self.process = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, env=server_env)
    else:
      self.process = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    flags = fcntl.fcntl(self.process.stdout, fcntl.F_GETFL)
    fcntl.fcntl(self.process.stdout, fcntl.F_SETFL, flags | os.O_NONBLOCK)

  def send(self, data, tail = b'\n'):
    self.process.stdin.write(data + tail)
    self.process.stdin.flush()

  def recv(self, t=.1, stderr=0):
    r = ''
    pr = self.process.stdout
    if stderr:
      pr = self.process.stdout
    while True:
      if not select.select([pr], [], [], 0)[0]:
        time.sleep(t)
        continue
      r = pr.read()
      return r.rstrip()
    return r.rstrip()

if __name__ == "__main__":
  ServerArgs = ['/usr/bin/python3', '/home/pyy/codes/pytest/subprocess/test.py']
  server = Server(ServerArgs)

  test_data = b'bas', b'sdfasd'
  for x in test_data:
    print('send', x)
    server.send(x)
    print('recv', server.recv())
