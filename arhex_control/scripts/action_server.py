#! /usr/bin/env python

import rospy

import actionlib

import control_msgs.msg

import trajectory_msgs.msg

class ArmTrajectoryFollower(object):
    # create messages that are used to publish feedback/result
    _feedback = control_msgs.msg.FollowJointTrajectoryFeedback()
    _result = control_msgs.msg.FollowJointTrajectoryResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, control_msgs.msg.FollowJointTrajectoryAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
        #create pub object for sending command to controller
        self.pub_controller = rospy.Publisher('robot_arm_controller/command', trajectory_msgs.msg.JointTrajectory, queue_size=10)
    def callback(self,feedback_msg):
        #send the state to feedback
        self._trajectory.header.stamp = rospy.get_rostime()
        #trajectory.header.frame_id = 'frame'
        self._feedback.joint_names = feedback_msg.joint_names
        self._feedback.desired = feedback_msg.joint_names
        self._feedback.actual = feedback_msg.joint_names
        self._feedback.error = feedback_msg.joint_names
        self._as.publish_feedback(self._feedback)
        rospy.sleep(2.)
        #goal condition
        flag = 0
        for i in range (len(self.goal.goal_tolerance.positions))    :
            if self.goal.goal_tolerance.positions[i] > self._feedback.error.positions[i]:
                flag = 1
            else:
                flag = 0
        if flag == 1:
            return (True)
        else:
            return (False)

    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True
        self.goal = goal
        #len(goal.trajectory.points)
        #send command to controller
        self.pub_controller.publish(goal.trajectory)

        # publish info to the console for the user
        # rospy.loginfo('%s: Executing, creating fibonacci sequence of order %i with seeds %i, %i' % (self._action_name, goal.order, self._feedback.sequence[0], self._feedback.sequence[1]))

        # start executing the action
        while not rospy.is_shutdown(): #replace with while
            # check that preempt has not been requested by the client
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
                break
            #subcribe to state from controller
            success = rospy.Subscriber('/robot_arm_controller/state', control_msgs.msg.JointTrajectoryControllerState, self.callback)

            if success: #result criteria
                self._result.error_code = self._result.SUCCESSFUL
                rospy.loginfo('%s: Succeeded' % self._action_name)
                self._as.set_succeeded(self._result)
                break
            r.sleep()

if __name__ == '__main__':
    rospy.init_node('action_server')
    server = ArmTrajectoryFollower("robot_arm_controller/follow_joint_trajectory")
    rospy.spin()
