#!/bin/python3
inp = open('password.lst','r')
out = open('pass_payload.lst','w')
for line in inp:
    out.write('peter\n')
    out.write(line)
