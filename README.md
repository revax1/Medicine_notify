# เริ่มต้น Project
```bash
git clone https://github.com/revax1/Medicine_notify.git
```
# PyQt
## ขั้นตอนการติดตั้ง

```bash
sudo apt-get update
sudo apt-get install python3.6
pip3 install PyQt5
sudo apt-get install python3-pyqt5
sudo apt-get install python3-pyqt5.qtsql
sudo install sqlite3
```

# Camera
## ขั้นตอนการติดตั้ง
```bash
sudo apt install fswebcam
cd src
chmod +x capture_image.sh
```

# Servo Driver
## ขั้นตอนการติดตั้ง
```bash
sudo apt-get install git build-essential python-dev
cd ~
git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
cd Adafruit_Python_PCA9685
sudo pip install adafruit-pca9685
sudo raspi-config
```
ใช้คำสั่ง sudo raspi-config และเปิดใช้งาน I2C

# Virtual Keyboard
## ขั้นตอนการติดตั้ง
```bash
sudo apt-get update
sudo apt install git build-essential
sudo apt-get install qt5-qmake
sudo apt-get install python3-pyqt5 qtbase5-dev qtdeclarative5-dev libqt5svg5-dev qtbase5-private-dev qml-module-qtquick-controls2 qml-module-qtquick-controls qml-module-qt-labs-folderlistmodel
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
git clone -b 5.15 https://github.com/qt/qtvirtualkeyboard.git
cd qtvirtualkeyboard
qmake 
sudo make
sudo make install
```
# Ngrok
## ขั้นตอนการติดตั้ง
```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm.tgz
sudo tar xvzf ./ngrok-v3-stable-linux-arm.tgz -C /usr/local/bin
ngrok config add-authtoken <NGROK_AUTHTOKEN>
sudo apt-get install apache2
cd src
chmod +x server.sh
```