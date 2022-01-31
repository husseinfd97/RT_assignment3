#! /usr/bin/env python

import rospy
from assignment3.srv import keyboard_interface	
import os   #used for write lines on terminal and do them (system )

#get the request (user input) and choose which choice will launch
def handler(req):
    if req.user_input == 2:
    
       print("initializing the teleop keyboard ")
       #launch_file choice 3
       os.system("roslaunch assignment3 choice_two.launch") 
       
    elif req.user_input == 3:
        print("calling teleop twist keyboard with obstacle avoidance control")
        #launch_file choice 3
        os.system("roslaunch assignment3 choice_three.launch")
    else:
        print("wrong input change it please")
    return 0         
   

    
    

#main
if __name__=="__main__":
    rospy.init_node('keyboard_interface')                                      
    a = rospy.Service('keyboard_interface' ,keyboard_interface ,handler)   
    rospy.spin()
