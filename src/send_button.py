#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


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
    goal.target_pose.pose.position.x = 6.0
    goal.target_pose.pose.position.y = 8.0
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')


def main2():

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
    goal.target_pose.pose.position.x = 0.0
    goal.target_pose.pose.position.y = 0.0
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')


def main3():

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
    goal.target_pose.pose.position.x = 8.5
    goal.target_pose.pose.position.y = -6.0
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')

def main4():

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
    goal.target_pose.pose.position.x = 6.35
    goal.target_pose.pose.position.y = -1.5
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')

def main5():

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
    goal.target_pose.pose.position.x = 20.0
    goal.target_pose.pose.position.y = -6.2
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')


def main7():

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
    goal.target_pose.pose.position.x = 13.29
    goal.target_pose.pose.position.y = 2.17
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')


def main8():

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
    goal.target_pose.pose.position.x = 15.0
    goal.target_pose.pose.position.y = 6.5
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')


def main9():

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
    goal.target_pose.pose.position.x = 9.0
    goal.target_pose.pose.position.y = -7.7
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')


def main10():

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
    goal.target_pose.pose.position.x = 22.0
    goal.target_pose.pose.position.y = -2.0
    goal.target_pose.pose.position.z = 0.0

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result')
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded')
    else:
        rospy.loginfo('Failed')



def cancel():
    serial.write('\x03')


def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   button1 = QPushButton(widget)
   button1.setText("Carga de Bateria")
   button1.setIcon(QIcon('charge.png'))
   button1.move(120,580)
   button1.clicked.connect(main)

   button2 = QPushButton(widget)
   button2.setText("Entrada 1")
   button2.setIcon(QIcon('in_1.png'))
   button2.move(360,760)
   button2.clicked.connect(main2)

   button3 = QPushButton(widget)
   button3.setText("Dinamometro de Chasis")
   button3.setIcon(QIcon('car.png'))
   button3.move(520,600)
   button3.clicked.connect(main3)

   button4 = QPushButton(widget)
   button4.setText("DMU")
   button4.setIcon(QIcon('dmu_torno.JPEG'))
   button4.move(400,600)
   button4.clicked.connect(main4)

   button5 = QPushButton(widget)
   button5.setText("Haas")
   button5.setIcon(QIcon('haas.jpeg'))
   button5.move(570,70)
   button5.clicked.connect(main5)

   button6 = QPushButton(widget)
   button6.setText("Cancel")
   button6.setIcon(QIcon('cancel.png'))
   button6.move(10,10)
   button6.clicked.connect(cancel)

   button7 = QPushButton(widget)
   button7.setText("Microscopios")
   button7.setIcon(QIcon('microscope.png'))
   button7.move(310,150)
   button7.clicked.connect(main7)

   button8 = QPushButton(widget)
   button8.setText("Dinamometro de Motor")
   button8.setIcon(QIcon('motor.jpg'))
   button8.move(100,100)
   button8.clicked.connect(main8)

   button9 = QPushButton(widget)
   button9.setText("Entrada 2")
   button9.setIcon(QIcon('in_1.png')) 
   button9.move(600,470)
   button9.clicked.connect(main9)

   button10 = QPushButton(widget)
   button10.setText("Inyectora")
   button10.setIcon(QIcon('inyectora.jpeg'))
   button10.move(430,100)
   button10.clicked.connect(main10)

   label1 = QLabel(widget)
   label1.setText("Laboratorio del CIMA")
   label1.move(300,10)

   label2 = QLabel(widget)
   label2.setStyleSheet("background-image : url(cima_2.jpg)")
   label2.resize(50,40)
   label2.move(450,0)
  
   widget.setStyleSheet("background-image : url(lab_cima.png)")

   widget.setGeometry(50,50,740,830)
   widget.setFixedSize(740,830)
   widget.setWindowTitle("Centro de Investigacion de Mecatronica Automotriz")
   widget.show()
   sys.exit(app.exec_())
   
   
if __name__ == '__main__':
   window()