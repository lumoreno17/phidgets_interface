# phidgets_interface
A package to read the voltage on Phidgets's channels and publish on ROS enviroment.

Requirements:
---------------------
Phidgets lib: https://www.phidgets.com/docs/OS_-_Linux#Quick_Downloads

Phidgets Python module: https://www.phidgets.com/docs/Language_-_Python

How it works
----------------------

Edit the src/Phidgets_Interface.py  to specify the channel number, sensor name, desired topic name and the channel mode.
On Phidgets_Interface.py in the end of the code you will find an example: 

```
monitor_0 = PhidgetMonitor(0, 'SENSOR_NAME','ANALOG0','ANALOG') 
monitor_0.setup()
```

Copy and Paste these two lines to each sensor you want to attach on Phidgets. In the example a above, the first parameter is the channel number which is 0. The second element is the name of the sensor that you will attach on Phidgets, the third parameter is the name of the topic to publish the data, and the last parameter specifies if the channel is a Digital Input or an Analog Input. 

Don't forget to do this for each sensor attached. Save the changes and you will be able to run it. 

Run it!
-------------------------
```
:~/catkin_ws$ rosrun phidgets_interface Phidgets_Interface.py
```
