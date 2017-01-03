#!/usr/bin/python2

import sys

#Le linha port lina de stdin
#Mantem '\n' ao fim da linha
#Faz o processamento apenas quando EOF e alcancado
def read_from_stdin():
    for line in sys.stdin:
        print line

#Main
if __name__ == '__main__':
    
    read_from_stdin()
