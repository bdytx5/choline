#!/bin/bash
mkdir -p ~/cholineSetupPayload
echo '0' > ~/choline.txt
while [ ! -f ~/cholineSetupPayload/choline_setup.sh ]; do
  sleep 1
done
sleep 5
sh -x ~/cholineSetupPayload/choline_setup.sh