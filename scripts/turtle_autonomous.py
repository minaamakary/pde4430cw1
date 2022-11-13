#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def movetoPosition():
	rospy.init_node('turtle_autonomous.py', anonymous=False)
	mypub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	move_message = Twist()
	while not rospy.is_shutdown():
		move_message.linear.x = 20
		move_message.angular.z = 0.0
		
		move_message.linear.x = 0.0
		move_message.angular.z = -20

		move_message.linear.x = -20.0
		move_message.angular.z = 0.0
			
		move_message.linear.x = 0.0
		move_message.angular.z = 20.0
			
		
			
		mypub.publish(move_message)
		rate.sleep()

if __name__ == '__main__':
	movetoPosition()