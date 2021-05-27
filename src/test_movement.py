#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def my_callback(msg):

    distance_moved = msg.data
    rospy.loginfo(msg.data)
    """if msg.data < 3:
        rospy.loginfo(msg.data)

    if msg.data > 3:
        

        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = 6
        goal.target_pose.pose.position.y = 8
        goal.target_pose.pose.orientation.w = 1.0

        client.send_goal(goal)
        wait = client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return client.get_result()
        
        

    pub.publish(move)"""

rospy.init_node('test_movement')

sub = rospy.Subscriber('/moved_distance', Float64, my_callback)
"""pub = rospy.Publisher('/cmd_vel', Twist, queue_size="1")
move = Twist()"""

rospy.spin()