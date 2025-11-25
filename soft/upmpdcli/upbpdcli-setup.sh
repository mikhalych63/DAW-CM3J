#!/bin/sh
wget https://www.lesbonscomptes.com/pages/lesbonscomptes.gpg
sudo cp ./lesbonscomptes.gpg /usr/share/keyrings/
wget https://www.lesbonscomptes.com/upmpdcli/pages/upmpdcli-rbookworm.list
sudo cp ./upmpdcli-rbookworm.list /etc/apt/sources.list.d
sudo apt update
sudo apt install upmpdcli
# Optional Songcast gateway
#sudo apt install sc2mpd