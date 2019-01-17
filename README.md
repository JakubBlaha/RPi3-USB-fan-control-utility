# Temperature control utility for *Raspberry Pi 3*

This utility is made for cases when one has an USB fan that he wants to use for *RPi 3* cooling. The utility is made possible by the fact 
that the USB hub's power in *RPi 3* is switchable. Unfortunately *RPi 3* does not support individual port power control, therefore no other 
usb devices can be used simultaneously with the fan as this utility would turn the power off for all of them. The Ethernet port should remain 
working in most cases, but there is a chance that the power will also turn off for this port, since it's a part of the USB hub. This 
software will NOT harm your USB hub permanently. As soon as the utility is killed, the power is restored.

## Usage
The utility is made for *Python 3*. Can be ran by typing
```python3 temp_ctrl.py```
into the terminal.

### Config
The utility provides a possibility to configure the control values. Samle of the `config` file is shown below.
```
max_temp=60  # Fan turns on at this temperature
cool_by=5  # Fan will keep running until the temperature is decreased by the given value. 60 - 5 = 55
temp_check_interval=1  # The update interval in which the temperature will be checked

```

*Note that the `config` file has no extension.*

If you want to control the fan only when needed, set the `cool_by` option to `0`.

### Terminal
The terminal does not provide any options. 

### Output
The utility will show some system status when running. Example below.
```
  Min    Max    Curr    Load %    Mem %    Temp 'C    Fan  
-----  -----  ------  --------  -------  ---------  -----  
  600   1300    1300       100     15.1       68.2      1  
```
