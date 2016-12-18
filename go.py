#!/usr/bin/python
#-*-coding:utf-8-*-

from iss import get_account_from_iss
import os
import sys

def run_sslocal(idx=0):
    accounts = get_account_from_iss()

    acc = accounts[idx]
    cmd = 'sslocal -s %s -p %s -b 0.0.0.0 -l %s -k %s -m %s -d restart' % (acc['server'],
        acc['port'], '1080', acc['passwd'], acc['encrypt'])
    print cmd
    os.system(cmd)

if __name__ == '__main__':
    print 'sslocal background monitor is running now...'

    idx = 0
    if len(sys.argv) > 1:
        idx = int(sys.argv[1])
        print idx
    run_sslocal(idx)
