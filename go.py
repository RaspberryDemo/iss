#!/usr/bin/python
#-*-coding:utf-8-*-

from iss import get_account_from_iss
import os
import schedule
import time

def run_sslocal():
    accounts = get_account_from_iss()

    for acc in accounts:
        cmd = 'sslocal -s %s -p %s -b 0.0.0.0 -l %s -k %s -m %s -d restart' % (acc['server'],
            acc['port'], '1080', acc['passwd'], acc['encrypt'])
        print cmd
        os.system(cmd)
        break

if __name__ == '__main__':
    print 'sslocal background monitor is running now...'

    run_sslocal()
    schedule.every().hour.do(run_sslocal)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    while True:
        schedule.run_pending()
        time.sleep(1)
