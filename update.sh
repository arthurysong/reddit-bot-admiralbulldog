#!/bin/bash

# script that will pull from remote repo and restart python bot, this script should should be ran only in prod environment

git pull 
kill -9 $(cat pid.txt)
python3 -u main.py >> output.txt &
echo $! > pid.txt