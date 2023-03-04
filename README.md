# A concise and robust multi-RealSense control library

## Features

- **Easy-to-use** Pythonic interface:
   - Encapsulated in object-oriented design for convenient multi-camera management
   - Supports `with` syntax for invocation: `with MultiRealsenseManager() as cams:`
   - Data is in Python and numpy data formats
- Good robustness for RealSense
    - Can handle common errors and automatically hardware_reset when encountering special exceptions
    - If USB is unplugged, the program will block, and when the USB is reinserted, the program will continue to run
- Easy-to-use configuration interface
    - Implemented control interface based on override method
    - Due to the complexity of the RealSense configuration options themselves, it is difficult to make them simpler
- Supports multiprocessing for multiple RealSense devices
    - On low-end Celeron CPUs or Raspberry Pis, the latency can be reduced by 50%

## Usage


1. Install:
```
pip install multi_realsense_manager
```
2. Demo:
```
python multi_realsense_manager/multi_realsense_manager.py
```
See comments in ["multi_realsense_manager/multi_realsense_manager.py"](multi_realsense_manager/multi_realsense_manager.py#L317-371) for usage instructions.

3. Check the number of RealSense devices and their SN/ID:
```
python -c 'print(__import__("multi_realsense_manager").MultiRealsenseManger.get_all_snids())'
