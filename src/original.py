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

    ch1 = VoltageInput()
    ch2 = VoltageInput()
    
#Set the channels as analog channels O and 1 of Phidgets Interface Kit.   
    ch1.setChannel(0)
    ch2.setChannel(1)
    
    msg1 = DeviceInfo()
    msg2 = DeviceInfo()
    
#Create a publish to each channel
    pub = rospy.Publisher('ANALOG0', DeviceInfo, queue_size=10)
    pub2 = rospy.Publisher('ANALOG1', DeviceInfo, queue_size=10)

#Initialize the node voltage_read    
    rospy.init_node('voltage_read', anonymous=True)
    
   
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
        #print("Library Version: %s" % attached.getLibraryVersion())
        #print("Serial Number: %d" % attached.getDeviceSerialNumber())
        print("Channel: %d" % attached.getChannel())
        print("Channel Class: %s" % attached.getChannelClass())
        print("Channel Name: %s" % attached.getChannelName())
        print("Device ID: %d" % attached.getDeviceID())
        #print("Device Version: %d" % attached.getDeviceVersion())
        print("Device Name: %s" % attached.getDeviceName())
        print("Device Class: %d" % attached.getDeviceClass())
        print("\n")
        
        msg1.lib_version = attached.getLibraryVersion()
        msg1.serial_num = attached.getDeviceSerialNumber()
        msg1.channel = attached.getChannel()
        msg1.channel_class = str(attached.getChannelClass())
        msg1.channel_name = attached.getChannelName()
        msg1.device_id = attached.getDeviceID()
        msg1.device_version = attached.getDeviceVersion()
        msg1.device_name = "EZ1"
        msg1.device_class = attached.getDeviceClass()

    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)   
        
        
def VoltageInputAttached2(self):
    try:
        attached2 = self
        print("\nAttach Event Detected (Information Below)")
        print("===========================================")
        #print("Library Version: %s" % attached2.getLibraryVersion())
        #print("Serial Number: %d" % attached2.getDeviceSerialNumber())
        print("Channel: %d" % attached2.getChannel())
        print("Channel Class: %s" % attached2.getChannelClass())
        print("Channel Name: %s" % attached2.getChannelName())
        print("Device ID: %d" % attached2.getDeviceID())
        #print("Device Version: %d" % attached2.getDeviceVersion())
        print("Device Name: %s" % attached2.getDeviceName())
        print("Device Class: %d" % attached2.getDeviceClass())
        print("\n")
        
        msg2.lib_version = attached2.getLibraryVersion()
        msg2.serial_num = attached2.getDeviceSerialNumber()
        msg2.channel = attached2.getChannel()
        msg2.channel_class = str(attached2.getChannelClass())
        msg2.channel_name = attached2.getChannelName()
        msg2.device_id = attached2.getDeviceID()
        msg2.device_version = attached2.getDeviceVersion()
        msg2.device_name = "SensorAmarelo"
        msg2.device_class = attached2.getDeviceClass()

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

def VoltageInputDetached2(self):
    detached2 = self
    try:
        print("\nDetach event on Port %d Channel %d" % (detached2.getHubPort(), detached2.getChannel()))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)
        
def ErrorEvent(self, eCode, description):
    print("Error %i : %s" % (eCode, description))

def VoltageChangeHandler(self, voltage):
    #print("Voltage1: %f" % voltage)
    msg1.voltage = voltage
    pub.publish(msg1)
  
def VoltageChangeHandler2(self, voltage):
    #print("Voltage2: %f" % voltage)
    msg2.voltage = voltage
    pub2.publish(msg2)

def SensorChangeHandler(self, sensorValue, sensorUnit):
    print("Sensor Value: %f" % sensorValue)

try:
    ch1.setOnAttachHandler(VoltageInputAttached)
    ch2.setOnAttachHandler(VoltageInputAttached2)
    
    ch1.setOnDetachHandler(VoltageInputDetached)
    ch2.setOnDetachHandler(VoltageInputDetached2)
    
    ch1.setOnErrorHandler(ErrorEvent)
    ch2.setOnErrorHandler(ErrorEvent)

    ch1.setOnVoltageChangeHandler(VoltageChangeHandler)
    ch2.setOnVoltageChangeHandler(VoltageChangeHandler2)
    
    ch1.setOnSensorChangeHandler(SensorChangeHandler)
    ch2.setOnSensorChangeHandler(SensorChangeHandler)



    print("Waiting for the Phidget VoltageInput Object to be attached...")
    ch1.openWaitForAttachment(5000)
    ch2.openWaitForAttachment(5000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

print("Gathering data for 10 seconds...")

time.sleep(10)

try:
    ch1.close()
    ch2.close()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1) 
print("Closed VoltageInput device")
exit(0)

