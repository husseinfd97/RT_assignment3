#! /usr/bin/env python

import rospy
import numpy
from geometry_msgs.msg import Twist, Vector3    
from sensor_msgs.msg import LaserScan 

#min distance between the robot and the obstacle
min_dist = 0.5

init = Vector3(0, 0, 0)
assigned = Twist( init, init)


def find_min_dist(ranges):

    dist_all_directions = [0,0,0]
    #Make direction for each range
    right_range = ranges[0:240]
    front_range = ranges[240:480]
    left_range  = ranges[480:721]
    #compute and store the min dist_all_directions
    dist_all_directions[0] = min(right_range)
    dist_all_directions[1] = min(front_range)
    dist_all_directions[2] = min(left_range)
    return dist_all_directions
        
  

def callback_scan(data):
    global assigned
    
    pub = rospy.Publisher('cmd_vel',Twist, queue_size=10)
    #Calculate the minimun obstacle distances in the whole directions (right , left and front)
    dist_all_directions = find_min_dist(data.ranges)

    if dist_all_directions[0] < min_dist :
        if assigned.angular.z < 0 :
            #don't turn right  
            assigned.angular.z = 0    
    if dist_all_directions[1] < min_dist:
        if assigned.linear.x > 0 :
            #dont' go forward to the obstacle
            assigned.linear.x = 0
    if dist_all_directions[2] < min_dist :
        if assigned.angular.z > 0 :
            #don't move left
            assigned.angular.z = 0
    pub.publish(assigned)




#copy rmap udate from cmd_vel in the global variable which is modified by the controller 

def callback_map_update(data):
    global assigned
    #update the global variable with new controller input 
    
    assigned = data        
  
    
    
#main 
if __name__=="__main__":
    rospy.init_node('keyboard_interface_node')
    #subscriber to topic map_update_cmd_vel    
    rospy.Subscriber("/map_update_cmd_vel", Twist, callback_map_update)
    #subscriber to topic scan
    rospy.Subscriber("/scan", LaserScan, callback_scan)
    rospy.spin()
