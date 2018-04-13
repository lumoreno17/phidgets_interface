#!/usr/bin/env python
# license removed for brevity

#Import Python module, Phidgets library and the DeviceInfo message. 

import rospy
import sys
import time 

from std_msgs.msg import Float32
from phidgets_interface.msg import DeviceInfo
from Phidget22.Devices.VoltageInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

try:
    
#Declare two channels as Voltage Input

    ch0 = VoltageInput()
    ch1 = VoltageInput()
    
#Set the channels as analog channels O and 1 of Phidgets Interface Kit.   
    ch0.setChannel(0)
    ch1.setChannel(1)
    
    msg0 = DeviceInfo()
    msg1 = DeviceInfo()
    

#Initialize the node voltage_read    
    rospy.init_node('voltage_read', anonymous=True)  
    
#Create a publish to each channel
    pub0 = rospy.Publisher('ANALOG0', DeviceInfo, queue_size=10)
    pub1 = rospy.Publisher('ANALOG1', DeviceInfo, queue_size=10)
 
   
except RuntimeError as e:
    print("Runtime Exception %s" % e.details)
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

def VoltageInputAttached(self):
    try:
        attached = self
        print("\nAttach Event Detected (Information Below)")
        print("===========================================")
        print("Channel: %d" % attached.getChannel())
        print("Channel Name: %s" % attached.getChannelName())
        print("Device ID: %d" % attached.getDeviceID())
        print("Device Name: %s" % attached.getDeviceName())
        print("\n")
        
        if attached.getChannel() == 0:
            
            msg0.channel = attached.getChannel()
            msg0.device_name = str("Sharp")
            
        
        elif attached.getChannel() == 1:
            
            msg1.channel = attached.getChannel()
            msg1.device_name = "LM35"
        

    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)   
        
    
def VoltageInputDetached(self):
    detached = self
    try:
        print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)   

        
def ErrorEvent(self, eCode, description):
    print("Error %i : %s" % (eCode, description))

def VoltageChangeHandler(self, voltage):
    
    attached = self
    if attached.getChannel() == 0:
        msg0.voltage = voltage
        pub0.publish(msg0)
    elif attached.getChannel() == 1:
        msg1.voltage = voltage
        pub1.publish(msg1)
        

try:
    ch0.setOnAttachHandler(VoltageInputAttached)
    ch1.setOnAttachHandler(VoltageInputAttached)
    
    ch0.setOnDetachHandler(VoltageInputDetached)
    ch1.setOnDetachHandler(VoltageInputDetached)
    
    ch0.setOnErrorHandler(ErrorEvent)
    ch1.setOnErrorHandler(ErrorEvent)

    ch0.setOnVoltageChangeHandler(VoltageChangeHandler)
    ch1.setOnVoltageChangeHandler(VoltageChangeHandler)
    

    print("Waiting for the Phidget VoltageInput Object to be attached...")
    ch0.openWaitForAttachment(5000)
    ch1.openWaitForAttachment(5000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

print("Gathering data for 100 seconds...")

time.sleep(100)

try:
    ch0.close()
    ch1.close()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1) 
print("Closed VoltageInput device")
exit(0)



