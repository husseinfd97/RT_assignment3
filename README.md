# RT_assignment3

## Project Description
This project consist of main program which control a robot moving in a map , the robot scan this map while it's moving and do the localization and then plan the motion .
The robot has three modes: 
1) autonomously reach a x,y coordinate inserted by the user
2) let the user drive the robot with the keyboard
3) let the user drive the robot assisting them to avoid collisions

## How to run the project 
First , run the launch file simulation_gmapping and move_base

```
roslaunch final_assignment simulation_gmapping.launch
```
```
roslaunch final_assignment move_base.launch
```

Then run the project launch file
```
roslaunch assignment3 main_launcher.launch
```
### Note:
To make the scripts excutable in the direction of scripts run 
```
bash run.sh
```

## Pseudo code

![Screenshot from 2022-01-31 21-07-30](https://user-images.githubusercontent.com/94136236/151873594-f5a15bf6-b8af-4921-a433-d2c6a2a95b94.png)

       

  
  

    




