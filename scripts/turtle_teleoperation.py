#!/usr/bin/ env python3
import rospy
import getch
from geometry_msgs.msg import Twist

#This is my node

def initialise():
	# init node here
	# init publisher here
	rospy.rate(10)
	move_message = Twist()
	while not rospy.is_shutdown():
	key = ord(getch.getch())
	if key==65:
		rospy.loginfo("Up key pressed")
		move_message.linear.x = 1.0
		move_message.angular.z = 0.0
		pub.publish(move_message)
		# move turtle forward here
	elif key==66:
		rospy.loginfo("Down key pressed")
		# move turtle backwards here

if '__name__' == '__main__':
	initialise()