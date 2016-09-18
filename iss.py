#!/usr/bin/python
#-*-coding:utf-8-*-

from soup import SoupX
import re


def get_account_from_iss():

    url = 'http://www.ishadowsocks.org/#free'
    soup = SoupX(url, 'utf-8').get()

    ips = []
    ports = []
    passwds = []
    encrypts = []
    
    links = soup.find_all(text=re.compile(u'服务器地址:'))
    for link in links:
        ips.append(link.split(':')[1].strip())
    
    links = soup.find_all(text=re.compile(u'端口:'))
    for link in links:
        ports.append(link.split(':')[1].strip())
    
    links = soup.find_all(text=re.compile(u'密码:'))
    for link in links:
        passwds.append(link.split(':')[1].strip())
    
    links = soup.find_all(text=re.compile(u'加密方式:'))
    for link in links:
        encrypts.append(link.split(':')[1].strip())

    accounts = []
    for i in range(len(ips)):
        acc = {}
        acc['server'] = ips[i]
        acc['port'] = ports[i]
        acc['passwd'] = passwds[i]
        acc['encrypt'] = encrypts[i]
        accounts.append(acc)
    return accounts

if __name__ == '__main__':
    get_account_from_iss()

