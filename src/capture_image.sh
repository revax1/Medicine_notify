#!/bin/bash
fswebcam -r 1280x720 --no-banner /home/pi/Documents/Medicine_notify/src/image.jpg
sudo mv /home/pi/Documents/Medicine_notify/src/image.jpg /var/www/html