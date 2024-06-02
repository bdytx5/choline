#!/bin/bash
mkdir -p ~/.choline
echo '0' > ~/choline.txt
while [ ! -f ~/.choline/choline_setup.sh ]; do
  sleep 1
done
sleep 5
echo 'running setup script' > ~/choline.txt
. ~/.choline/choline_setup.sh >> ~/.choline/choline_setup_log.txt 2>&1
sh -x ~/.choline/choline_setup.sh >> ~/.choline/choline_setup_log.txt 2>&1