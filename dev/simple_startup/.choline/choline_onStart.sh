#!/bin/bash
mkdir -p ~/.choline
echo '0' > ~/choline.txt
while [ ! -f ~/.choline/choline_setup.sh ]; do
  sleep 1
done
sleep 5
echo 'running setup script' > ~/choline.txt
sh -x ~/.choline/choline_setup.sh