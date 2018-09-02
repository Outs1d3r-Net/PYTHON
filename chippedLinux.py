#!/usr/bin/python
# coding: latin-1

#LIBRARIES
import os
import sys
import crypt

#USAGE: 
os.system("clear")
if len(sys.argv) != 2:
    print "\033[1;33m##################################\n###### Desec - ChippedLinux ######\n#########   by: Init-0   #########\n## USAGE: ChippedLinux wordlist ##\n##################################\033[0m\n"
    exit(1)

#INFORMATION GATHERING
print "\033[0;34m##################################\n###### Desec - ChippedLinux ######\n#########   by: Init-0   #########\n##################################\033[0m\n"
quebra = raw_input("Enter the hash: ")
salt = raw_input("Enter the salt: ")
f = open(sys.argv[1], 'r')
os.system("clear")

#CODE
for palavra in f:
    palavra = palavra.strip("\n")
    trinca = crypt.crypt(palavra, salt)
    if trinca == quebra:
        os.system("clear")
        print "\033[0;34m##################################\n###### Desec - ChippedLinux ######\n#########   by: Init-0   #########\n##################################\033[0m\n"
        print "\033[1;34mhash cracked: \033[0m",trinca+"\033[1;32m ",palavra+"\033[0m\n"
        exit(0)
    else:
        print "\033[1;34mTrying...  \033[0m",trinca
exit(0)
