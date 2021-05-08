#!/bin/bash

# remote update script
# script that updates and restarts bot from local dev environment

ssh -i '~/.ssh/arthurec2.pem' ubuntu@54.215.178.93 /bin/bash <<EOT
  echo "test"
  cd reddit-bot-admiralbulldog
  ./update.sh
EOT