#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

def publish_markers():
    rospy.init_node('marker_array_publisher', anonymous=True)
    pub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)

    marker_array = MarkerArray()

    # Create multiple markers
    # for i in range(5):  # Change this range to create more or fewer markers
    #     marker = Marker()
    #     marker.header.frame_id = "map"
    #     marker.header.stamp = rospy.Time.now()

    #     marker.type = Marker.CUBE
    #     marker.id = i

    #     # Set the scale of each marker
    #     marker.scale.x = 0.5
    #     marker.scale.y = 0.5
    #     marker.scale.z = 0.5

    #     # Set a different color for each marker (you can customize as needed)
    #     marker.color.r = (i + 1) * 0.2
    #     marker.color.g = 1.0 - (i * 0.2)
    #     marker.color.b = 0.5
    #     marker.color.a = 1.0  # Alpha (opacity)

    #     # Set the position of each marker
    #     marker.pose.position.x = i  # Arrange them along the x-axis
    #     marker.pose.position.y = i  # Arrange them diagonally
    #     marker.pose.position.z = 0.0

    #     # Set orientation (all markers with the same orientation)
    #     marker.pose.orientation.x = 0.0
    #     marker.pose.orientation.y = 0.0
    #     marker.pose.orientation.z = 0.0
    #     marker.pose.orientation.w = 1.0

    #     # Add marker to the marker array
    #     marker_array.markers.append(marker)

    
    ###########################################################################################
    ##################################create the world boundary################################
    ###########################################################################################

    boundary = Marker()

    boundary.header.frame_id = "map"
    boundary.header.stamp = rospy.Time.now()

    boundary.type = Marker.LINE_STRIP  # Line strip marker type
    boundary.id = 0

    # Set the scale of the line width
    boundary.scale.x = 0.05  # Width of the line

    # Set the color of the line
    boundary.color.r = 0.0
    boundary.color.g = 1.0  # Green color
    boundary.color.b = 0.0
    boundary.color.a = 1.0  # Alpha (opacity)

    # Define the points for the line (as Point objects)
    corner_one = Point()
    corner_one.x = 22.0
    corner_one.y = 9.0
    corner_one.z = 0.0

    corner_two = Point()
    corner_two.x = 22.0
    corner_two.y = -9.0
    corner_two.z = 0.0

    corner_three = Point()
    corner_three.x = -2.0
    corner_three.y = -9.0
    corner_three.z = 0.0

    corner_four = Point()
    corner_four.x = -2.0
    corner_four.y = 9.0
    corner_four.z = 0.0

    corner_five = corner_one


    # Add points to the marker's points list (this defines the shape of the line)
    boundary.points.append(corner_one)
    boundary.points.append(corner_two)
    boundary.points.append(corner_three)
    boundary.points.append(corner_four)
    boundary.points.append(corner_five)


    ###########################################################################################
    ##############################create the exploration boundary##############################
    ###########################################################################################

    exploration_area = Marker()

    exploration_area.header.frame_id = "map"
    exploration_area.header.stamp = rospy.Time.now()

    exploration_area.type = Marker.LINE_STRIP  # Line strip marker type
    exploration_area.id = 1

    # Set the scale of the line width
    exploration_area.scale.x = 0.05  # Width of the line

    # Set the color of the line
    exploration_area.color.r = 1.0
    exploration_area.color.g = 0.0  # Green color
    exploration_area.color.b = 0.0
    exploration_area.color.a = 1.0  # Alpha (opacity)

    # Define the points for the line (as Point objects)
    corner_one = Point()
    corner_one.x = 11.0
    corner_one.y = 9.0
    corner_one.z = 0.0

    corner_two = Point()
    corner_two.x = 11.0
    corner_two.y = -9.0
    corner_two.z = 0.0


    # Add points to the marker's points list (this defines the shape of the line)
    exploration_area.points.append(corner_one)
    exploration_area.points.append(corner_two)


    marker_array.markers.append(exploration_area)



    marker_array.markers.append(boundary)


    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
        for marker in marker_array.markers:
            marker.header.stamp = rospy.Time.now()

        pub.publish(marker_array)

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_markers()
    except rospy.ROSInterruptException:
        pass
