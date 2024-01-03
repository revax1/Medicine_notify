# PyQt
## ขั้นตอนการติดตั้ง

```bash
sudo apt-get update
sudo apt-get install python3.6
pip install pyqt5
```

# Camera
## ขั้นตอนการติดตั้ง
```bash
sudo apt install fswebcam
```

# Servo Driver
## ขั้นตอนการติดตั้ง
```bash
sudo apt-get install git build-essential python-dev
cd ~
git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
cd Adafruit_Python_PCA9685
sudo python setup.py install
```

# Virtual Keyboard
## ขั้นตอนการติดตั้ง
```bash
sudo apt-get update
sudo apt install git build-essential
sudo apt-get install python3-pyqt5 qt5-default qtdeclarative5-dev libqt5svg5-dev qtbase5-private-dev qml-module-qtquick-controls2 qml-module-qtquick-controls qml-module-qt-labs-folderlistmodel
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
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
sudo tar xvzf ./ngrok-v3-stable-linux-arm64.tgz -C /usr/local/bin
ngrok authtoken <NGROK_AUTHTOKEN>
```