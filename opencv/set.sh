
apt-get update
apt-get -y upgrade
apt-get -y install build-essential cmake unzip pkg-config
#apt-get install libgtk-3-dev
apt-get -y install libatlas-base-dev gfortran
apt-get -y install python3-dev
apt-get -y install wget
cd /
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.3.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.3.zip
unzip opencv.zip
unzip opencv_contrib.zip
apt-get -y install python3-pip
pip3 install --upgrade pip
pip3 install numpy
#apt-get install build-essential cmake pkg-config
cd /opencv-3.4.3/
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib-3.4.3/modules \
-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
-D BUILD_EXAMPLES=ON ..
make
make install
ldconfig