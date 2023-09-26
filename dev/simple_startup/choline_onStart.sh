echo '0' > ~/choline.txt
while [ ! -f ~/cholineSetupPayload/choline_setup.sh ]; do
  sleep 1
done
sleep 5
bash choline_setup.sh