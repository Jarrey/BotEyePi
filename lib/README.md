# Referenced Libraries #


### zxing ###

web site: [https://github.com/zxing/zxing](https://github.com/zxing/zxing "https://github.com/zxing/zxing")

**zxing** ("Zebra Crossing") is an open-source, multi-format 1D/2D barcode image processing library implemented in Java.

Our project references zxing as barcode decoder. There are two versions of zxing:

* **zxing2.2**: this version support JavaSE 6 (1.6.*). Can be used in current Raspberry Pi environment. Current Rasbian official provides JavaSE 6, not the latest version. So we only choose this version for our project at runtime.

* **zxing3.2.1**: the latest version. Cannot support JavaSE 6 environment. Please manually upgrade your Raspberry Pi Java runtime to 7+ then we can use this version.

**USAGE**:

Project contains one python wrapped module that provides zxing barcode detection API. It dependent with standard I/O in command line. In the background, python module will launch a hidden command line zxing process and transfer parameters to zxing process via stdIn. Then invoke specific zxing API (in Java runtime) and get the return value via stdOut.

Please refer to `../src/zxing.py`