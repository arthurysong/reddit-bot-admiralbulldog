#!/bin/bash

# this script will pull changes in ec2 instance and restart bot with changes.

# this doesn't work yet
ssh -i '~/.ssh/arthurec2.pem' ubuntu@13.57.195.73 /bin/bash <<EOT
  # update and restart should
  cd reddit-bot-admiralbulldog
  git pull 
  echo "test"
  echo $BOT_ID
  kill -9 $BOT_ID
  python3 -u main.py >> output.txt &
  BOT_ID=$! # set BOT_ID equal to process running
EOT