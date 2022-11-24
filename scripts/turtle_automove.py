#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import turtlesim.srv

rospy.wait_for_service('spawn')
spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
spawner(1,1,0,"turtle2")

rospy.wait_for_service('spawn')
spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
spawner(1,8,0,"turtle3")

rospy.wait_for_service('spawn')
spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
spawner(7,2,0,"turtle4")

rospy.wait_for_service('spawn')
spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
spawner(1,3,0,"turtle5")

def callback5(data): #for 5th turtle
	#TURTLE 5
	pub=rospy.Publisher('/turtle5/cmd_vel', Twist, queue_size=10) # init publisher here
	rate=rospy.Rate(80)
	move_message = Twist()
	rospy.loginfo("x = %f" % data.x)
	rospy.loginfo("y =  %f" % data.y )
	move_message.linear.x = 0.4

	if data.x < 1 or data.x > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
		#turtle.kill()

	if data.y < 1 or data.y > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
	
	pub.publish(move_message)


def callback4(data): #for 4th turtle
	#TURTLE 4
	pub=rospy.Publisher('/turtle4/cmd_vel', Twist, queue_size=10) # init publisher here
	rate=rospy.Rate(80)
	move_message = Twist()
	rospy.loginfo("x = %f" % data.x)
	rospy.loginfo("y =  %f" % data.y )
	move_message.linear.x = 0.4

	if data.x < 1 or data.x > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
		#turtle.kill()

	if data.y < 1 or data.y > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
	
	pub.publish(move_message)


def callback3(data): #for 3rd turtle
	#TURTLE 3
	pub=rospy.Publisher('/turtle3/cmd_vel', Twist, queue_size=10) # init publisher here
	rate=rospy.Rate(50)
	move_message = Twist()
	rospy.loginfo("x = %f" % data.x)
	rospy.loginfo("y =  %f" % data.y )
	move_message.linear.x = 0.4

	if data.x < 1 or data.x > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
		#turtle.kill()

	if data.y < 1 or data.y > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
	
	pub.publish(move_message)


def callback2(data): #for 2nd turtle
	#TURTLE 2
	pub=rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10) # init publisher here
	rate=rospy.Rate(50)
	move_message = Twist()
	rospy.loginfo("x = %f" % data.x)
	rospy.loginfo("y =  %f" % data.y )
	move_message.linear.x = 0.4

	if data.x < 1 or data.x > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
		#turtle.kill()

	if data.y < 1 or data.y > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
	
	pub.publish(move_message)



def callback(data):
	pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) # init publisher here
	rate=rospy.Rate(50)
	move_message = Twist()
	rospy.loginfo("x = %f" % data.x)
	rospy.loginfo("y =  %f" % data.y )
	move_message.linear.x = 0.4

	if data.x < 1 or data.x > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
		#turtle.kill()

	if data.y < 1 or data.y > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
	
	pub.publish(move_message)







	'''
	elif (( data.x > 11.0 or data.y < 0.5)):
		move_message.linear.x = 2.0
		move_message.angular.z = 0.0
		pub.publish(move_message)
		#turtle.kill()
		rospy.loginfo("hittng the wall")
	elif (data.x == 0.015857 and data.y == 0.052203):
		move_message.linear.x = 2.0
		move_message.angular.z = 0.0
		pub.publish(move_message)

	elif (data.x > 11.0 and data.y > 11.0):
		move_message.linear.x = 2.0
		move_message.angular.z = 0.0
		pub.publish(move_message)
	'''	

		#rospy.loginfo("Turtle is in he left half of the screen.")

def readTurtlemovement():
	
	rospy.init_node('turtle_automove', anonymous=True)
	rospy.Subscriber("/turtle1/pose", Pose, callback)

	rospy.Subscriber("/turtle2/pose", Pose, callback2)
	rospy.Subscriber("/turtle3/pose", Pose, callback3)
	rospy.Subscriber("/turtle4/pose", Pose, callback4)
	rospy.Subscriber("/turtle5/pose", Pose, callback5)

	rospy.spin()

	
		
if __name__ == '__main__':
	readTurtlemovement()
	
