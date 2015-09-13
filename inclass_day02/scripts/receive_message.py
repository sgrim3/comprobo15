#!/usr/bin/env python

""" This script explores subscripbinc to topics using Python """

import rospy
from geometry_msgs.msg import PointStamped

def process_stamped_point(msg):
	print msg.point

rospy.init_node('receive_message')
rospy.Subscriber("/my_point", PointStamped, process_stamped_point)

r=rospy.Rate(10)
while not rospy.is_shutdown():
	r.sleep()