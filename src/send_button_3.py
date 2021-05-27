#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtCore import pyqtSlot

import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


def main():
    global x
    global y
    global z
    global label3
    PENDING = 0
    ACTIVE = 1
    DONE = 2
    WARN = 3
    ERROR = 4

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
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = z

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    state_result = client.get_state()


    rospy.loginfo("state_result " + str(state_result))

    while state_result < DONE:
        rospy.loginfo("Doing Stuff while waiting for the server to give a result...")
        state_result = client.get_state()
        rospy.loginfo("state_result: " + str(state_result))
        label3.setHidden(False)
        widget.setEnabled(False)

    rospy.loginfo("[Result] State: " + str(state_result))
    if state_result == ERROR:
        rospy.logerr("Something went wrong in the server side")
        label3.setHidden(True)
        widget.setEnabled(True)
        fail()
    if state_result == WARN:
        rospy.logwarn("There is a warning in the Server Side")
        label3.setHidden(True)
        widget.setEnabled(True)
        fail()
    if state_result == DONE:
        rospy.loginfo('Succeeded')
        label3.setHidden(True)
        widget.setEnabled(True)
        succeed()
    

def fail():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Failed Goal")
    msg.setInformativeText("Try Again Please")
    msg.setWindowTitle("Information")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

def succeed():
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Information)
    msg1.setText("Succeeded Goal")
    msg1.setWindowTitle("Information")
    msg1.setInformativeText("Good Job!!!")
    msg1.setStandardButtons(QMessageBox.Ok)
    msg1.exec_()

def boton1():
    global x
    global y
    global z
    x = 6.0
    y = 8.0
    z = 0.0
    main()

def boton2():
    global x
    global y
    global z
    x = 0.0
    y = 0.0
    z = 0.0
    main()

def boton3():
    global x
    global y
    global z
    x = 8.5
    y = -6.0
    z = 0.0
    main()

def boton4():
    global x
    global y
    global z
    x = 6.35
    y = -1.5
    z = 0.0
    main()

def boton5():
    global x
    global y
    global z
    x = 20.0
    y = -6.2
    z = 0.0
    main()

def boton7():
    global x
    global y
    global z
    x = 13.29
    y = 2.17
    z = 0.0
    main()

def boton8():
    global x
    global y
    global z
    x = 15.0
    y = 6.5
    z = 0.0
    main()

def boton9():
    global x
    global y
    global z
    x = 9.0
    y = -7.7
    z = 0.0
    main()

def boton10():
    global x
    global y
    global z
    x = 22.0
    y = -2.0
    z = 0.0
    main()

def window():
   global widget
   app = QApplication(sys.argv)
   widget = QWidget()
   
   button1 = QPushButton(widget)
   button1.setText("Carga de Bateria")
   button1.setIcon(QIcon('charge.png'))
   button1.move(120,580)
   button1.clicked.connect(boton1)

   button2 = QPushButton(widget)
   button2.setText("Entrada 1")
   button2.setIcon(QIcon('in_1.png'))
   button2.move(360,760)
   button2.clicked.connect(boton2)

   button3 = QPushButton(widget)
   button3.setText("Dinamometro de Chasis")
   button3.setIcon(QIcon('car.png'))
   button3.move(520,600)
   button3.clicked.connect(boton3)

   button4 = QPushButton(widget)
   button4.setText("DMU")
   button4.setIcon(QIcon('dmu_torno.JPEG'))
   button4.move(400,600)
   button4.clicked.connect(boton4)

   button5 = QPushButton(widget)
   button5.setText("Haas")
   button5.setIcon(QIcon('haas.jpeg'))
   button5.move(570,70)
   button5.clicked.connect(boton5)

   button7 = QPushButton(widget)
   button7.setText("Microscopios")
   button7.setIcon(QIcon('microscope.png'))
   button7.move(310,150)
   button7.clicked.connect(boton7)

   button8 = QPushButton(widget)
   button8.setText("Dinamometro de Motor")
   button8.setIcon(QIcon('motor.jpg'))
   button8.move(100,100)
   button8.clicked.connect(boton8)

   button9 = QPushButton(widget)
   button9.setText("Entrada 2")
   button9.setIcon(QIcon('in_1.png')) 
   button9.move(600,470)
   button9.clicked.connect(boton9)

   button10 = QPushButton(widget)
   button10.setText("Inyectora")
   button10.setIcon(QIcon('inyectora.jpeg'))
   button10.move(430,100)
   button10.clicked.connect(boton10)

   label1 = QLabel(widget)
   label1.setText("Laboratorio del CIMA")
   label1.move(300,10)
   
   global label3
   movie = QMovie('wait.gif')
   label3 = QLabel(widget)
   label3.setMovie(movie)
   label3.move(85,355)
   label3.resize(510,60)
   label3.setHidden(True)
   movie.start()

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