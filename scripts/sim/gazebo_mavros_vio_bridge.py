#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped,Quaternion
from nav_msgs.msg import Odometry


class GazeboMavrosVIOAdapter:
    def __init__(self):
        rospy.init_node('camera_pose_publisher')

        self.parent_frame = rospy.get_param('~parent_frame', 'map')

        self.pose_pub = rospy.Publisher('/mavros/vision_pose/pose', PoseStamped, queue_size=1)
        self.gz_ground_truth_sub = rospy.Subscriber('/phoenix_d456/gt_odom', Odometry, self.gz_ground_truth_cb)

    def gz_ground_truth_cb(self, msg):
        pose_msg = PoseStamped()
        pose_msg.header.frame_id = 'map'
        pose_msg.header.stamp = rospy.Time.now()
        pose_msg.pose.position.x = msg.pose.pose.position.x
        pose_msg.pose.position.y = msg.pose.pose.position.y
        pose_msg.pose.position.z = msg.pose.pose.position.z
        pose_msg.pose.orientation.x = msg.pose.pose.orientation.x
        pose_msg.pose.orientation.y = msg.pose.pose.orientation.y
        pose_msg.pose.orientation.z = msg.pose.pose.orientation.z
        pose_msg.pose.orientation.w = msg.pose.pose.orientation.w
        self.pose_pub.publish(pose_msg)


if __name__ == '__main__':
    obj = GazeboMavrosVIOAdapter()
    rospy.spin()
