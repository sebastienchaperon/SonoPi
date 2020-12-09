# SonoPi
2020-08-20-raspios-buster-armhf-full
interfacing option
SPI
I2C
Serial
1-Wire

boot console auto login
update & upgrade

cd ~
git clone https://github.com/lthiery/SPI-Py.git
cd ~/SPI-Py
git checkout 8cce26b9ee6e69eb041e9d5665944b88688fca68
sudo python3 setup.py install

 git clone https://github.com/sebastienchaperon/SonoPi.git
  
 filezilla envoyer dans /Music

 cd SonoPi
 sudo python3 new_tag.py
 sudo python3 main.py
 
 
 sudo mv /home/pi/SonoPi/musique.service /etc/systemd/system/musique.service
 sudo systemctl start musique.service
 ok ---- sudo systemctl enable musique.service
