#!/usr/bin/python3
# Copyright 2022 Stogl Robotics Consulting UG (haftungsbeschränkt)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Denis Štogl, Lovro Ivanov
#


import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import time

from control_msgs.action import FollowJointTrajectory

from sensor_msgs.msg import JointState

class FJTS(Node):

    def __init__(self):
        super().__init__('ruka_arm_controller')
        print("as init")
        self.i = 0
        self.goal = FollowJointTrajectory.Goal()

        self._action_server = ActionServer(
            self,
            FollowJointTrajectory,
            'ruka_arm_controller/follow_joint_trajectory',
            self.execute_callback)
        
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)

        print("as init done")

    def execute_callback(self, goal_handle):
        #feedback_msg = FollowJointTrajectory.Feedback()

        self.goal = goal_handle
        print("cb")
        """
        print(self.goal._goal_request.trajectory.points[0])
        print(len(goal._goal_request.trajectory.points))

        for i in range(1, len(goal._goal_request.trajectory.points)):
            feedback_msg.actual = goal._goal_request.trajectory.points[i]
            goal_handle.publish_feedback(feedback_msg)
            print(goal._goal_request.trajectory.points[i])
            time.sleep(0.1) 

        """

        msg = JointState()
        for i in range(1, len(self.goal._goal_request.trajectory.points)):
            msg.position = self.goal._goal_request.trajectory.points[self.i].position
            self.publisher_.publish(msg)
            print(msg)
            time.sleep(0.1) 
        print("for")

        result = FollowJointTrajectory.Result()
        return result
    


rclpy.init()

fjtserver = FJTS()
print("init done")

rclpy.spin(fjtserver)
