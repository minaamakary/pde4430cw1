#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


move_message = Twist()
pubTwo=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) # init publisher here
def callback(data):
	rospy.loginfo("trial")
	
	if (data.x or data.y):
		move_message.linear.x = 1.0
		pubTwo.publish(move_message)

	if (data.x <1 or data.x >10 or data.y < 1 or data.y > 10.0):
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
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