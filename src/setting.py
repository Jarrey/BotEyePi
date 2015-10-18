########################################################################
#
#  Created by Jarrey (jar_bob@163.com) for Speedpro Inc.
#  Copyright by Speedpro Inc. 2015
#
########################################################################

# Global setting
debug_mode = False

# Log file
log_file = 'speedpro_log.log'

# Serial port settings
ser_dev_name = "/dev/ttyAMA0"
ser_bps = 9600

# GPIO settings
gpio_warining = False
switchInPin = 16 # GPIO 16, to control camera capture
outputPin = 18 # GPIO 18, output control for next device
lightPin = 12  # GPIO Pin 12, for camera lights


# Serial command setting
ser_start_char = '\x02'
ser_end_char = '\x03'
ser_get_jigid = 'JIGID'

signal_control = 0 # 1: HIGH  0: LOW
                   
# Camera capture image resolution
resolution = (1024, 768)

# The format of image camera capture
capture_format = "jpeg"

# The bar region in captured image
bar_region = (120, 150, 900, 350)

# Marker settings
left_marker_region = (0, 0, 1024, 768)
right_marker_region = (0, 0, 1024, 768)

# zxing library settings
zxing_lib_loc = "zxing"
zxing_ver = "2.2"
