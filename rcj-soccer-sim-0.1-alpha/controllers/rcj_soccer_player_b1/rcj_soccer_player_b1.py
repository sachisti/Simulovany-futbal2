# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math

# You can also import scripts that you put into the folder with controller
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import utils

import time


k = 0


robotX = []
robotY = []

class MyRobot(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()

                # Get the position of our robot
                robot_pos = data[self.name]
                # Get the position of the ball
                ball_pos = data['ball']

                # Get angle between the robot and the ball
                # and between the robot and the north
                ball_angle, robot_angle = self.get_angles(ball_pos, robot_pos)

                # Compute the speed for motors
                direction = utils.get_direction(ball_angle)

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                #if direction == 0:
                #    left_speed = -5
                #    right_speed = -5
                #else:
                #    left_speed = direction * 4
                #    right_speed = direction * -4

                real_robot_angle = robot_angle*57
                
                robot_x = robot_pos["x"]*100
                robot_y = robot_pos["y"]*100
                
                ball_x = ball_pos["x"]*100
                ball_y = ball_pos["y"]*100
                
                branaX = 75
                branaY = 0
                
                def get_angles(pos1_x, pos1_y):
                    pos2_x = 75
                    pos2_y = 0 
                    a = pos2_x - pos1_x
                    b = pos2_y - pos1_y
                    c = math.sqrt(a**2 + b**2)
                    alfa = math.degrees(math.asin(a / c))
                    gama = 90
                    return alfa
                  
                if len(robotX) == 2:
                    robotX.pop(0)
                    robotY.pop(0)
                    robotX.append(int(robot_x))
                    robotY.append(int(robot_y))
                    
                    global k
                    k = 1
                else:
                    robotX.append(int(robot_x))
                    robotY.append(int(robot_y))
                    left_speed = 0
                    right_speed = 0
                    if robot_y < 0:
                        uhol = real_robot_angle + 180 - get_angles(robot_x, robot_y)
                    else:
                        uhol = real_robot_angle - 180 + get_angles(robot_x, robot_y)
                    print("prepocitavam")
                   
                if k == 1:
                    if robotX[0] == robotX[1] and robotY[0] == robotY[1]:
                        if real_robot_angle - 2 <= uhol and real_robot_angle + 2 >= uhol:
                            left_speed = -5
                            right_speed = -5
                            print("ideme")
                        else:
                            if real_robot_angle < uhol:
                                left_speed = 1
                                right_speed = -1
                                print("dolava")
                            else:
                                left_speed = -1
                                right_speed = 1
                                print("doprava")
                            print("tocime sa a nevieme preco")
                        print(uhol)
                        print(real_robot_angle)
                        
                    else:        
                        if robot_y < 0:
                            uhol = real_robot_angle + 180 - get_angles(robot_x, robot_y)
                        else:
                            uhol = real_robot_angle - 180 + get_angles(robot_x, robot_y)
                        print("prepocitavam")
                
               
                                                
                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                
                
my_robot = MyRobot()
my_robot.run()
