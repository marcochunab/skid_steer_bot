#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    
    b = msg.pose.pose.position.y
    print (b)

rospy.init_node('extract_msg_node_2')
sub = rospy.Subscriber('odom', Odometry, callback)
rospy.spin()