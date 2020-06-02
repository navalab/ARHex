#!/usr/bin/env python

import rospy
import math
import angles
import pylab as pl

from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from math import sin,cos,atan2,sqrt,fabs


#Define a RRBot joint positions publisher for joint controllers.
def arhex_joint_positions_publisher(pub1,pub2,pub3,pub4,pub5,pub6,pub7,pub8,pub9,pub10,pub11,pub12,pub13,pub14,pub15):

    #Initiate node for controlling joint1 and joint2 positions.


    #Define publishers for each joint position controller commands.
    rate = rospy.Rate(100)
    #While loop to have joints follow a certain position, while rospy is not shutdown.
    i = 0
    #stand = 0.01
    #support = angles.pi*40/180
    still = 0
    stand = angles.pi*90/180
    while not rospy.is_shutdown():
        #msg = rospy.wait_for_message('/arhex/joint_states', JointState)
        #stand = angles.pi*90/180
        i = 135
        j = 45.3
        pub7.publish(still)
        pub8.publish(still)
        pub9.publish(still)
        pub10.publish(still)
        pub11.publish(still)
        pub12.publish(still)
        pub13.publish(still)
        pub14.publish(still)
        pub15.publish(still)
        rate.sleep()
        # for count in range (0,540):
        #     if count<270:
        #         support = angles.pi*i/180
        #         stand = angles.pi*j/180
        #         pub1.publish(stand)
        #         pub2.publish(support)
        #         pub3.publish(support)
        #         pub4.publish(stand)
        #         pub5.publish(stand)
        #         pub6.publish(support)
        #         i = i + 1
        #         j = j + 0.333
        #         if i == 360:
        #             i = 0
        #         rate.sleep()
        #
        #     elif count == 270:
        #         j = 135
        #         i = 45.3
        #         support = angles.pi*i/180
        #         stand = angles.pi*j/180
        #         pub1.publish(stand)
        #         pub2.publish(support)
        #         pub3.publish(support)
        #         pub4.publish(stand)
        #         pub5.publish(stand)
        #         pub6.publish(support)
        #         j = 136
        #         i = i + 0.333
        #         rate.sleep()
        #
        #     else:
        #         support = angles.pi*i/180
        #         stand = angles.pi*j/180
        #         pub1.publish(stand)
        #         pub2.publish(support)
        #         pub3.publish(support)
        #         pub4.publish(stand)
        #         pub5.publish(stand)
        #         pub6.publish(support)
        #         j = j + 1
        #         i = i + 0.333
        #         if j == 360:
        #             j = 0
        #         rate.sleep()
        #     pub7.publish(still)
        #     pub8.publish(still)
        #     pub9.publish(still)
        #     pub10.publish(still)
        #     pub11.publish(still)
        #     pub12.publish(still)
        #     pub13.publish(still)
        #     pub14.publish(still)
        #     pub15.publish(still)
        #


#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
    try:
        rospy.init_node('gait_control_node', anonymous=True)
        pub1 = rospy.Publisher('/arhex/L_FL_position_controller/command', Float64, queue_size=10)
        pub2 = rospy.Publisher('/arhex/L_FR_position_controller/command', Float64, queue_size=10)
        pub3 = rospy.Publisher('/arhex/L_ML_position_controller/command', Float64, queue_size=10)
        pub4 = rospy.Publisher('/arhex/L_MR_position_controller/command', Float64, queue_size=10)
        pub5 = rospy.Publisher('/arhex/L_RL_position_controller/command', Float64, queue_size=10)
        pub6 = rospy.Publisher('/arhex/L_RR_position_controller/command', Float64, queue_size=10)
        pub7 = rospy.Publisher('/arhex/torso_position_controller/command', Float64, queue_size=10)
        pub8 = rospy.Publisher('/arhex/shoulder_1_position_controller/command', Float64, queue_size=10)
        pub9 = rospy.Publisher('/arhex/shoulder_2_position_controller/command', Float64, queue_size=10)
        pub10 = rospy.Publisher('/arhex/elbow_position_controller/command', Float64, queue_size=10)
        pub11 = rospy.Publisher('/arhex/wrist_1_position_controller/command', Float64, queue_size=10)
        pub12 = rospy.Publisher('/arhex/wrist_2_position_controller/command', Float64, queue_size=10)
        pub13 = rospy.Publisher('/arhex/wrist_3_position_controller/command', Float64, queue_size=10)
        pub14 = rospy.Publisher('/arhex/ef_1_position_controller/command', Float64, queue_size=10)
        pub15 = rospy.Publisher('/arhex/ef_2_position_controller/command', Float64, queue_size=10)
        #msg = rospy.wait_for_message('/arhex/joint_states', JointState)
        arhex_joint_positions_publisher(pub1,pub2,pub3,pub4,pub5,pub6,pub7,pub8,pub9,pub10,pub11,pub12,pub13,pub14,pub15)
    except rospy.ROSInterruptException: pass
