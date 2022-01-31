#! /usr/bin/env python

import rospy
from assignment3.srv import keyboard_interface	
from assignment3.srv import robot_coordinates	

def choice_one():
    print("choice one is chosen")
    x = float(input("enter x position: "))
    y = float(input("enter y position: "))
    rospy.wait_for_service('robot_coordinates')
    Robot_coordinates = rospy.ServiceProxy('robot_coordinates', robot_coordinates)
    rt = Robot_coordinates(x , y)
    if rt.return_ == 1:
        print("target reached successfully!")
    else:
      	print("target not reached")


def choice_two():
    print("choice two is chosen")
    rospy.wait_for_service('keyboard_interface')
    Keyboard_interface = rospy.ServiceProxy('keyboard_interface', keyboard_interface)
    Keyboard_interface(2)


def choice_three():
    print("choice three is chosen")
    rospy.wait_for_service('keyboard_interface')
    Keyboard_interface = rospy.ServiceProxy('keyboard_interface', keyboard_interface)
    Keyboard_interface(3)


 
if __name__=="__main__":
    
    rospy.init_node('user_controller')

    
    while(1):
        
        print("choice one  : autonomously reach a x,y coordinate inserted by the user")
        print("Choice two  : user drive the robot with the keyboard")
        print("Choice three: drive the robot using the keyboard while avoiding obstacles avoidance")        
        ans=input("select an action: ")
        
        
        if ans.isnumeric(): # error checking if the input by user is character or number (true always if it's number)
            ans = int(ans) 
            if (ans == 1):
                
                choice_one()

            elif (ans == 2):
                
                choice_two() 

            elif (ans == 3):
                  
                choice_three()

            else:
                
                print("incorrect number ,not from choices")
        else:
            
            print("input value is not a number!")
           
