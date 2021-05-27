#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    a = msg.pose.pose.position.x
    
    print (a)

rospy.init_node('extract_msg_node')
sub = rospy.Subscriber('odom', Odometry, callback)
rospy.spin()