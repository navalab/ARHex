#!/usr/bin/env python

import rospy
import math
import angles

from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from math import sin,cos,atan2,sqrt,fabs


#Define a RRBot joint positions publisher for joint controllers.
def arhex_joint_positions_publisher(pub1,pub2,pub3,pub4,pub5,pub6):

    #Initiate node for controlling joint1 and joint2 positions.
    #Define publishers for each joint position controller commands.
    rate = rospy.Rate(3)
    #While loop to have joints follow a certain position, while rospy is not shutdown.
    #i = 0
    support = angles.pi*135/180
    stand = angles.pi*45/180
    pub1.publish(stand)
    pub2.publish(support)
    pub3.publish(support)
    pub4.publish(stand)
    pub5.publish(stand)
    pub6.publish(support)
    while not rospy.is_shutdown():
        #msg = rospy.wait_for_message('/arhex/joint_states', JointState)
        #stand = angles.pi*90/180
        for i in range(6):
            #support = angles.pi*i/180
            stand = stand + angles.pi*15/180
            support = support + angles.pi*45/180
            pub1.publish(stand)
            pub2.publish(support)
            pub3.publish(support)
            pub4.publish(stand)
            pub5.publish(stand)
            pub6.publish(support)
            #i = i+1 #increment i
            if support == angles.pi*2:
                support = 0
            rate.sleep()
        for j in range(6):
            #support = angles.pi*i/180
            stand = stand + angles.pi*15/180
            support = support + angles.pi*45/180
            pub1.publish(support)
            pub2.publish(stand)
            pub3.publish(stand)
            pub4.publish(support)
            pub5.publish(support)
            pub6.publish(stand)
            #i = i+1 #increment i
            if support == angles.pi*2:
                support = 0
            rate.sleep()
        #stand, support = support, stand

#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
    try:
        rospy.init_node('joint_positions_node', anonymous=True)
        pub1 = rospy.Publisher('/arhex/joint1_position_controller/command', Float64, queue_size=10)
        pub2 = rospy.Publisher('/arhex/joint2_position_controller/command', Float64, queue_size=10)
        pub3 = rospy.Publisher('/arhex/joint3_position_controller/command', Float64, queue_size=10)
        pub4 = rospy.Publisher('/arhex/joint4_position_controller/command', Float64, queue_size=10)
        pub5 = rospy.Publisher('/arhex/joint5_position_controller/command', Float64, queue_size=10)
        pub6 = rospy.Publisher('/arhex/joint6_position_controller/command', Float64, queue_size=10)
        #msg = rospy.wait_for_message('/arhex/joint_states', JointState)
        arhex_joint_positions_publisher(pub1,pub2,pub3,pub4,pub5,pub6)
    except rospy.ROSInterruptException: pass
