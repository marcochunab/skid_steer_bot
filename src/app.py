#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from time import time
import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
#from test_movement import distance_moved

PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   button1 = QPushButton(widget)
   button1.setText("Button1")
   button1.move(64,32)
   button1.clicked.connect(button1_clicked)

   button2 = QPushButton(widget)
   button2.setText("Button2")
   button2.move(64,64)
   button2.clicked.connect(button2_clicked)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("PyQt5 Button Click Example")
   widget.show()
   sys.exit(app.exec_())


def button1_clicked():

    rospy.init_node('send_goal_python', 'extract_msg_node')

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    rospy.loginfo('Waiting for the action server to start')
    client.wait_for_server()

    rospy.loginfo('Action server started, sending the goal')
    goal = MoveBaseGoal()
    goal.target_pose.header.stamp = rospy.Time.now()

    # set frame
    goal.target_pose.header.frame_id = 'map'

    # set position
    goal.target_pose.pose.position.x =34.308149
    goal.target_pose.pose.position.y =-14.321036
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = -1.0
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    state_result = client.get_state()
    
    rospy.loginfo("state_result: "+str(state_result))
    start_time = time()

    while state_result < DONE:
        #rospy.loginfo("Doing stuff while waiting for the ")
        state_result = client.get_state()
        #rospy.loginfo("state_result: "+str(state_result))
        elapsed_time = time() - start_time
        
    
    rospy.loginfo("[Result] State: "+str(state_result))
    if state_result == DONE:
        print("Elapsed time: %.10f seconds." % elapsed_time)
        
        print(a)
        
    if state_result == ERROR:
        rospy.logerr("Something went wrong in the server side")
        print("Elapsed time: %.10f seconds." % elapsed_time)
    if state_result == WARN:
        rospy.logwarn("There is a warning in the Server Side")
        print("Elapsed time: %.10f seconds." % elapsed_time)


def button2_clicked():

    rospy.init_node('send_goal_python', 'extract_msg_node')

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    rospy.loginfo('Waiting for the action server to start')
    client.wait_for_server()

    rospy.loginfo('Action server started, sending the goal')
    goal = MoveBaseGoal()
    goal.target_pose.header.stamp = rospy.Time.now()

    # set frame
    goal.target_pose.header.frame_id = 'map'

    # set position
    goal.target_pose.pose.position.x = 10.028757
    goal.target_pose.pose.position.y = -14.626811
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)
    state_result = client.get_state()
    
    rospy.loginfo("state_result: "+str(state_result))
    start_time = time()

    while state_result < DONE:
        #rospy.loginfo("Doing stuff while waiting for the ")
        state_result = client.get_state()
        #rospy.loginfo("state_result: "+str(state_result))
        elapsed_time = time() - start_time
        
    
    rospy.loginfo("[Result] State: "+str(state_result))
    if state_result == DONE:
        print("Elapsed time: %.10f seconds." % elapsed_time)
        
        print(a)
        
    if state_result == ERROR:
        rospy.logerr("Something went wrong in the server side")
        print("Elapsed time: %.10f seconds." % elapsed_time)
    if state_result == WARN:
        rospy.logwarn("There is a warning in the Server Side")
        print("Elapsed time: %.10f seconds." % elapsed_time)
   
if __name__ == '__main__':
   window()