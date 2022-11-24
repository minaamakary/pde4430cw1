#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
#move turtle to any given co-ordination on the world
#def class
#define position of turtle
#if turtle is in the centre - move it to point x,y
move_message = Twist()
pubTwo=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) # init publisher here
def callback(data):
	rospy.loginfo("trial")
	if ((data.x == 5.544444561004639 and data.y == 5.544444561004639)):
		move_message.linear.x = 1.0
		move_message.angular.z = 0.0
		pubTwo.publish(move_message) 
		



def goToLocation():
	rospy.init_node('turtlegoTo', anonymous=True)
	rospy.Subscriber("/turtle1/pose", Pose, callback)
	rospy.spin()
	rate=rospy.Rate(50)
	#while not rospy.is_shutdown():



	rate.sleep()


if __name__ == '__main__':
	goToLocation()