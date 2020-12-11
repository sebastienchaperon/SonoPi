# SonoPi alpha
Lecture de fichiers audio localement stocké sur un raspberry en fonction d'un tag NFC. 

-Matériel nécessaire :

Raspberry pi 3 ou + connecté au réseau 

2020-08-20-raspios-buster-armhf-full

Penser à activer le SPI dans raspi-config->interfaces

3 LED

4 boutons poussoir

MFRC522

Plan de câblage dans le git (bouton pause à supprimer)

L'interface graphique est inutile donc vous pouvez booster directement en console

update & upgrade

cd ~
git clone https://github.com/lthiery/SPI-Py.git

cd ~/SPI-Py

git checkout 8cce26b9ee6e69eb041e9d5665944b88688fca68

sudo python3 setup.py install

git clone https://github.com/sebastienchaperon/SonoPi.git

 
Envoyer les fichiers en FTP dans /home/pi/Music/---artiste---/---album---/

Le répertoire ne doit contenir que des fichiers audio. 

cd SonoPi

sudo python3 new_tag.py

Vous devez enregistrer au moins un tag avant de commencer 

Suivre les instructions 

sudo python3 main.py

Si tout fonctionne ctrl+c

  
sudo mv /home/pi/SonoPi/musique.service /etc/systemd/system/musique.service

sudo systemctl start musique.service

ok ---- sudo systemctl enable musique.service

Sudo reboot

Enjoy

