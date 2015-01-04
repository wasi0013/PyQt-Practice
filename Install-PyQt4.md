###Install PyQt4:    
 
#####Install Python 3.4.2 (If necessary :wink:)
```
sudo apt-get install libssl-dev openssl
wget python.org/ftp/python/3.4.2/Python-3.4.2.tgz
tar -xzvf Python-3.4.2.tgz
cd Python-3.4.2/
./configure
make
sudo make install
```

#####Install SIP:
```
sudo apt-get update
wget http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.5/sip-4.16.5.tar.gz
tar -xzvf sip-4.16.5
cd sip-4.16.5
./configure
make
sudo make install
```
#####Install PyQt4:
```
sudo apt-get update
sudo apt-get install qt4-qmake libqt4-dev pkg-config
wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.3/PyQt-x11-gpl-4.11.3.tar.gz
tar -xzvf PyQt-x11-gpl-4.11.3
cd PyQt-x11-gpl-4.11.3
./configure
make
sudo make install
```
