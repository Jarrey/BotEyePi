# ~ZXING Code Information~ #

**ZXING** library dependency with Java runtime, and standard I/O with data transformation. So when we integrate with current source code (base on **zbar** lib), we need to to change the image data format; **zbar** can support python stream data, but for std I/O, we cannot transfer stream, so in **zxing** case, we use temporary image file.

* To capture image from camera and convert to gray level by **PIL** (python image library)
* To save the bar-code image as file in temporary format
* To call **zxing** command line tool and transfer the file path
* To get the **zxing** data result by std IO, and convert to our bar code result data


## Source Code Files ##

- **[src/bar.py](../src/bar.py)**: the original bar class, to handle and detect the bar-code image (or stream) by **zbar** library.
- **[src/bar_zxing.py](../src/bar_zxing.py)**: the bar class same as [src/bar.py](../src/bar.py), but it was base on **zxing** module.
- **[src/zxing.py](../src/zxing.py)**: a python version of **zxing** library, use standard input/ouput to invoke **zxing** APIs. It contains a bar code result class that including the data and format for several bar-code formats. Can refer to official python-zxing site: [https://github.com/oostendo/python-zxing](https://github.com/oostendo/python-zxing) 

## Settings ##

There are two settings about **zxing** component (in [src/setting.py](../src/setting.py)):

1. **`zxing_lib_loc`**: specify the **zxing** component location in runtime.
1. **`zxing_ver`**: specify the version of **zxing** component, 2.2 is for Java 6; 3.2.x is for Java 7 or newer.


## Build and Deploy Scripts ##

- **[src/build.py](../src/build.py)**: a python script to build and compile all python script to binary format. To protect the source code in product environment (except [src/setting.py](../src/setting.py)).
- **[src/build.sh](../src/build.sh)**: a shell script to deploy the compiled files into `/src/bin` folder. For **zxing** components, it will copy all **zxing** versions in `/lib` folder.


## Test ZXING Component Code ##

**[src/bar_zxing.py](../src/bar_zxing.py)** file contains one self-test method to test the **zxing** library in python runtime. Please manually copy **`/lib/zxing2.2`** or **`/lib/zxing3.2.X`** to the same folder as `bar_zxing.py` script. Then in shell or command line to type `python bar_zxing.py` to test.

It will read and detect the sample bar-code images through parameter. You could modify source code (in the end of **`src/bar_zxing.py`**):

    if __name__ == '__main__':
    	if len(argv) < 2:
    		exit(1)
    
    	barreader = BarReader(None)
    	print barreader.getSymbol(argv[1])
    	del barreader

to test other bar-code samples. 

Example: **`python bar_zxing.py '../test/barcode.png'`**