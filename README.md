# MFRC522-AccessManager

This Access Manager system has been tested on the Raspberry PI 3 Model B+ running Apache with CGI execution allowed.



![alt text](https://github.com/CLStrike/MFRC522-AccessManager/raw/main/accessmanager_mainmenu.png)

Please check out the following guide to setup the sensor this AccessManager requires:
https://pimylifeup.com/raspberry-pi-rfid-rc522/

This AccessManager is assuming that you have installed:
- Apache2
- SimpleMFRC522
- python3-dev
- python3-pip
- spidev (pip3 install spidev)
- mfrc522 (pip3 install mfrc522)

Please move the files in the CGI-bin directory to the cgi-bin directory of your webserver.
Move the Index.html file to the /var/www/html. (default directory for index.html file)


That's all!

