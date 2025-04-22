import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/schaefm2/ros2_ws/src/lab2/install/lab2'
