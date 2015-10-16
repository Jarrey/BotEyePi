# Environment Setup
## --python-zxing development and runtime setup

`python-zxing` github page: [https://github.com/oostendo/python-zxing](https://github.com/oostendo/python-zxing)

# Install `maven` (Java package repository solution)
	sudo apt-get update
	sudo apt-get maven # about 200MB size used

# Install `python-zxing` on Raspberry Pi #

    # get code of zxing library
	git clone https://github.com/zxing/zxing.git
	
	# get code of python-zxing
    git clone git://github.com/oostendo/python-zxing.git
    
	# install python-zxing module
	cd python-zxing
	sudo python setup.py build
	sudo python setup.py install
	
	# install zxing library
	cd ../zxing
	mvn install

    cd core
    wget http://central.maven.org/maven2/com/google/zxing/core/2.2/core-2.2.jar -O core.jar
    mvn install

	# setup java runtime
    cd ../javase
    wget http://central.maven.org/maven2/com/google/zxing/javase/2.2/javase-2.2.jar -O javase.jar
    mvn install

# Test `python-zxing` module #