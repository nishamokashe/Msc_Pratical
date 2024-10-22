''' Write a program to create login id password using parser command line argument. '''

import sys
import argparse
users = {'Nisha' : 'NI23' , 'nisha93' : 'ni93', 'NISHA':'0756', 'nisha88':'0570'}
parser = argparse.ArgumentParser(description = 'Example script using argparse')

parser.add_argument('-u', '--user', help = 'User name')
parser.add_argument('-p', '--password', help = ' Password')

args = parser.parse_args()

if(args.user):
    if args.user in users.keys():
        pw = users[args.user]
        if(args.password and args.password == pw):
            print("you have been logged in successully.")
        else:
            print("Password is incorrect.")
    else:
        print("User '{}' not registered.".format(args.user))
else:
    print("Empty user name.")

