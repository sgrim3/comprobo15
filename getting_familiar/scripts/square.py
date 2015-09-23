#!/usr/bin/env python

# import all the things
import rospy
from geometry_msgs.msg import Twist

#initalize the node
rospy.init_node('square')

#function that moves the robot forward, and then turns 90 degrees
def mover():
    pub = rospy.Publisher('cmd_vel', Twist)

    #moves robot forward 1 meter ish
    twist = Twist()
    twist.linear.x = .1
    pub.publish(twist)
    rospy.sleep(10)

    #turns robot 90 degrees ish
    twist.angular.z = 1
    pub.publish(twist)
    rospy.sleep(1.5);

#while loop to keep repeating mover until ctrl-c
while not rospy.is_shutdown(): 
    mover()



