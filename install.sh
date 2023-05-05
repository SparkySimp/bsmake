#!/usr/bin/env bash

# copies the file bsmake.py as bsmake to /usr/local/bin
cp bsmake.py /usr/local/bin/bsmake

# makes the file executable
chmod +x /usr/local/bin/bsmake

# exits with the status code of the last command
exit $?
