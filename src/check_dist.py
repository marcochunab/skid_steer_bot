#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from math import pi

def callback(msg):
  print msg.ranges[360]
  #!move.linear.x = 0.1
  #!if msg.ranges[360] < 2:
      #!move.linear.x = 0
      #!move.angular.z = pi*2/4/10
  #!pub.publish(move)

rospy.init_node('sub_node')
sub = rospy.Subscriber('/skid_steer_bot/laser/scan', LaserScan, callback)
#!pub = rospy.Publisher('/cmd_vel', Twist)
#!move = Twist()

rospy.spin()