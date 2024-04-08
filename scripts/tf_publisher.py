#!/usr/bin/env python3

import os
import yaml
import tf
import tf2_ros
import geometry_msgs.msg
import rospy
import tf.transformations

class CameraTransformPublisher:
    def __init__(self):
        self.directory = rospy.get_param('~calib_path', '../param/sensors/')
        self.broadcaster = tf2_ros.StaticTransformBroadcaster()
        self.tf_list = []

    def load_and_publish_transforms(self):
        # Loop through each file in the directory
        for filename in os.listdir(self.directory):
            if filename.endswith('.yaml'):
                camera_name = filename.split('.')[0]
                filepath = os.path.join(self.directory, filename)
                with open(filepath, 'r') as file:
                    # Load YAML content
                    data = yaml.safe_load(file)
                    # Assume the first key in the YAML file is the camera name
                    # camera_name = list(data.keys())[0]
                    transform = data['cam0']['T_cam_imu']
                    self.process_transform(camera_name, transform)

        self.broadcaster.sendTransform(self.tf_list)

    def process_transform(self, camera_name, transform):
        t = geometry_msgs.msg.TransformStamped()

        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "imu"
        t.child_frame_id = camera_name

        # invert the transformation matrix
        transform = tf.transformations.inverse_matrix(transform)

        t.transform.translation.x = transform[0][3]
        t.transform.translation.y = transform[1][3]
        t.transform.translation.z = transform[2][3]

        quaternion = tf.transformations.quaternion_from_matrix(transform)
        t.transform.rotation.x = quaternion[0]
        t.transform.rotation.y = quaternion[1]
        t.transform.rotation.z = quaternion[2]
        t.transform.rotation.w = quaternion[3]

        self.tf_list.append(t)

if __name__ == "__main__":
    rospy.init_node('camera_transform_publisher', anonymous=True)
    publisher = CameraTransformPublisher()
    publisher.load_and_publish_transforms()
    rospy.spin()
