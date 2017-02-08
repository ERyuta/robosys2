#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import Int32

def cb(message):
    #rospy.loginfo(message.data*2)
    if message.data == 100:
	os.system('cowsay Mr.Ueda')
    if message.data == 150:
	os.system('cowsay Lecture')
    if message.data == 200:
	os.system('cowsay was')
    if message.data == 250:
	os.system('cowsay fun!!')
    if message.data == 300:
	os.system('cowsay -b Thank you!!')

if __name__ == '__main__': 
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb) 
    rospy.spin()
