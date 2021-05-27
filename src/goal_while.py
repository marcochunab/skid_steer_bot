#!/usr/bin/env python

from time import time
import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

def main():

    rospy.init_node('send_goal_python')

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    rospy.loginfo('Waiting for the action server to start')
    client.wait_for_server()

    rospy.loginfo('Action server started, sending the goal')
    goal = MoveBaseGoal()
    goal.target_pose.header.stamp = rospy.Time.now()

    # set frame
    goal.target_pose.header.frame_id = 'map'

    # set position
    goal.target_pose.pose.position.x = 5.9739529175
    goal.target_pose.pose.position.y = -2.0571417299
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)

    state_result = client.get_state()
    rospy.loginfo("state_result: "+str(state_result))
    start_time = time()

    while state_result < DONE:
        rospy.loginfo("Doing stuff while waiting for the ")
        state_result = client.get_state()
        rospy.loginfo("state_result: "+str(state_result))
        elapsed_time = time() - start_time

    rospy.loginfo("[Result] State: "+str(state_result))
    if state_result == DONE:
        print("Elapsed time: %.10f seconds." % elapsed_time)
    if state_result == ERROR:
        rospy.logerr("Something went wrong in the server side")
        print("Elapsed time: %.10f seconds." % elapsed_time)
    if state_result == WARN:
        rospy.logwarn("There is a warning in the Server Side")

if __name__ == '__main__':
    main()