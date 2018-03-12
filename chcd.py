#!/usr/bin/python

# CHCD by Johan Rasten

import os
import os.path

import getpass
USERNAME = getpass.getuser()


def meFirstGen(iterable):
    if USERNAME in iterable:
        yield USERNAME
    for item in iterable:
        if item != USERNAME:
            yield item


def recfind(curpath, dirs, lastdir):
    print(curpath, dirs, lastdir)
    try:
        files = os.listdir(curpath)
    except OSError:
        return None
    if not dirs:
        if lastdir in files:
            finalpath = os.path.join(curpath, lastdir)
            if os.path.isdir(finalpath):
                return finalpath
    else:
        for filename in meFirstGen(files):
            if filename.startswith(dirs[0]):
                nextpath = os.path.join(curpath, filename)
                if os.path.isdir(nextpath):
                    res = recfind(nextpath, dirs[1:], lastdir)
                    if res:
                        return res

    return None

def chcd(shortpath):
    dirs = shortpath.split('/')
    lastdir = dirs[-1]
    dirs = dirs[:-1]

    if not dirs:
        return os.getcwd()
    elif not dirs[0]:
        curpath = '/'
        dirs = dirs[1:]
    elif dirs[0] == '~':
        curpath = os.path.expanduser(dirs[0])
        dirs = dirs[1:]
    elif dirs[0] == '.':
        curpath = os.getcwd()
        dirs = dirs[1:]
    else:
        curpath = os.getcwd()
    return recfind(curpath, dirs, lastdir)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('')
    else:
        print(chcd(sys.argv[1]))

