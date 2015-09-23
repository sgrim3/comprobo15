#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class WallApproach(object):
    """ A ROS node that implements a proportional controller to approach an obstacle
        immediately in front of the robot """
    def __init__(self, target_distance):
        """ Initialize a node with the specified target distance
            from the forward obstacle """
        rospy.init_node('wall_approach')
        self.sub=rospy.Subscriber('/scan', LaserScan, self.processScan)
        self.pub=rospy.Publisher("cmd_vel",Twist, queue_size=10)
        self.target_distance=target_distance
        self.currentDistance=0
    
    def processScan(self, msg):
    	self.currentDistance=msg.ranges[0]  	


    def run(self):
        """ Our main 5Hz run loop """
        r = rospy.Rate(5)
        while not rospy.is_shutdown():
        	if self.currentDistance!=0:
		    	self.twist=Twist()
		    	self.twist.linear.x=(self.currentDistance-self.target_distance)*.5
		    	self.pub.publish(self.twist)
			r.sleep()

if __name__ == '__main__':
    node = WallApproach(1.0)
    node.run()