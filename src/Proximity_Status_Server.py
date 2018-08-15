#!/usr/bin/env python
# license removed for brevity

#Import Python module, Phidgets library and the DeviceInfo message. 


import rospy
import sys
import time 

from std_msgs.msg import Float32
from phidgets_interface.msg import DeviceInfo
from phidgets_interface.srv import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

class PhidgetMonitor:
    
    def __init__(self,channel,sensor_name,topic_name,modo):
        self.channel = channel
        self.sensor_name = sensor_name
        self.topic_name = topic_name
        self.modo = modo
        #self.pub = rospy.Publisher(self.topic_name, DeviceInfo, queue_size=10)
        self.serv = rospy.Service(self.topic_name, ProximityStatus, self.ReturnStatus)
        self.msg = DeviceInfo()
        self.modo = modo
        if modo == 'ANALOG':
            self.ch = VoltageInput()
        elif modo == 'DIGITAL':
            self.ch = DigitalInput()
            
             
    
    def setup(self):
        
        self.msg.channel = self.channel
        self.msg.device_name = self.sensor_name
        self.ch.setChannel(self.channel)   
        self.ch.setOnAttachHandler(self.VoltageInputAttached)
        self.ch.setOnDetachHandler(self.VoltageInputDetached)
        self.ch.setOnErrorHandler(self.ErrorEvent)
        if self.modo == 'ANALOG':
            self.ch.setOnVoltageChangeHandler(self.VoltageChangeHandler)
        elif self.modo == 'DIGITAL':
            self.ch.setOnStateChangeHandler(self.VoltageChangeHandler)
        
        print("Waiting for the Phidget VoltageInput Object to be attached...")
        self.ch.openWaitForAttachment(5000)
        
    def close(self):
        self.ch.close()
        print("Closed VoltageInput device")   
        
    def VoltageInputAttached(self,attached):

        print("\nAttach Event Detected (Information Below)")
        print("===========================================")
        print("Channel: %d" % attached.getChannel())
        print("Channel Name: %s" % attached.getChannelName())
        print("Device ID: %d" % attached.getDeviceID())
        print("Device Name: %s" % attached.getDeviceName())
        print("Mode: %s" %self.modo)
        print("\n")   
            
    def VoltageInputDetached(self,detached):
        print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))   
             
    def ErrorEvent(self, subject, eCode, description):
        print("Error %i : %s" % (eCode, description))

    def VoltageChangeHandler(self, subject, voltage):
        self.msg.voltage = voltage
        #self.pub.publish(self.msg)
        
    def ReturnStatus(self,req):
        return self.msg.voltage

if __name__ == '__main__':

    rospy.init_node('voltage_read', anonymous=True)
# PhidgetMonitor(Channel number, Sensor Name, Topic Name, Channel Mode)
    monitor_0 = PhidgetMonitor(0, 'Proximity Sensor','DIGITAL0','DIGITAL')
    monitor_0.setup()
    rospy.spin()







        


        
     
    
        
        
        


