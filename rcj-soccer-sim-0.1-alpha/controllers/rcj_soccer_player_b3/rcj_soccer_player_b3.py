# rcj_soccer_player controller - ROBOT B3

###### REQUIRED in order to import files from B1 controller
import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
# You can now import scripts that you put into the folder with your
# robot B1 controller
from rcj_soccer_player_b1 import rcj_soccer_robot, utils
######

# Feel free to import built-in libraries
import math

import time

a = 0
buduceX = 0
buduceY = 0
koeficient = 1
loptaX = []
loptaY = []
vr = 0
vl = 0

class MyRobot(rcj_soccer_robot.RCJSoccerRobot):
    def run(self):
        while self.robot.step(rcj_soccer_robot.TIME_STEP) != -1:
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
                
                
                             
                #superova brana je x 70
                #a y je 15 az -15
                
                def buduce_suradnice_lopty():
                    global buduceX, buduceY, loptaX, loptaY, koeficient
                    if len(loptaX) == 2:
                        loptaX.pop(0)
                        loptaY.pop(0)
                        loptaX.append(ball_x)
                        loptaY.append(ball_y)
                        buduceX = loptaX[1] + ((loptaX[1] - loptaX[0])*koeficient)
                        buduceY = loptaY[1] + ((loptaY[1] - loptaY[0])*koeficient)
                    else:
                        loptaX.append(ball_x)
                        loptaY.append(ball_y)
                    
                        
               
                      
                def get_angles(pos1_x, pos1_y):
                    if polovica == 1:
                        pos2_x = -75
                    else:
                        pos2_y = 75
                    pos2_y = 0
                    if pos1_y < 0:
                        pos1_y = pos1_y * (-1)
                    if pos1_x < 0:
                        pos1_x = pos1_x * (-1)
                    a = pos2_x - pos1_x
                    b = pos2_y - pos1_y
                    c = math.sqrt(a**2 + b**2)
                    global alfa
                    alfa = math.degrees(math.asin(a / c))
                    beta = math.degrees(math.asin(b / c))
                    gama = 90
                    return beta
                
                def zisti_ci_mas_loptu():
                    if polovica == -1:
                        if robot_x < ball_x and robot_x + 5 > ball_x and robot_y + 4 > ball_y and robot_y - 4 < ball_y:
                            return 1
                        else:
                            return 0
                    else:
                        if robot_x > ball_x and robot_x - 5 < ball_x and robot_y + 4 > ball_y and robot_y - 4 < ball_y:
                            return 1
                        else:
                            return 0   
                                       
                def navigacia():
                    if robot_y > 0:
                        cielovy_uhol = 90 + get_angles(robot_x, robot_y)
                    else:
                        cielovy_uhol = 90 - get_angles(robot_x, robot_y)
                    global vr, vl
                    if real_robot_angle + 4 >= cielovy_uhol and real_robot_angle - 4 <= cielovy_uhol:
                        vr = 10
                        vl = 10
                    else: 
                        if real_robot_angle < cielovy_uhol:
                            vr = -3
                            vl = 3
                        else:
                            vr = 3
                            vl = -3
                        
                    
                    
                global a
                
                if a == 0:
                    if robot_x < 0:
                        polovica = -1
                    else:
                        polovica = 1
                    start_time = time.time()
                    a = 1
                
                if ball_x > 75 or ball_x < -75:
                    a = 0
                  
                if (time.time() - start_time) < 4:
                    if direction == 0:
                        left_speed = -10
                        right_speed = -10
                    else:
                        left_speed = direction * 5
                        right_speed = direction * -5
                
                
                
                else:         
                    if polovica == 1:                       
                        if robot_x < 20:
                            if zisti_ci_mas_loptu() == 0:
                                if direction == 0:
                                    left_speed = -10
                                    right_speed = -10
                                else:
                                    left_speed = direction * 10
                                    right_speed = direction * -10
                            else:
                                print("mamb3")
                                if ball_y > -10 and ball_y < 10:
                                    navigacia()
                                    left_speed = vl
                                    right_speed = vr
                                else:
                                    if ball_y < 0:
                                        left_speed = -5
                                        right_speed = -10
                                    else:
                                        left_speed = -10
                                        right_speed = -5
                        else:
                            if real_robot_angle <= 274:
                                if real_robot_angle >= 264: 
                                    left_speed = -10
                                    right_speed = -10
                                else:
                                    left_speed = 3
                                    right_speed = -3
                            else:
                                left_speed = -3
                                right_speed = 3
                                
                    else:
                        if robot_x > -25:
                            if zisti_ci_mas_loptu() == 0:
                                if direction == 0:
                                    left_speed = -10
                                    right_speed = -10
                                else:
                                    left_speed = direction * 10
                                    right_speed = direction * -10
                            else:
                                if ball_y > -10 and ball_y < 10:
                                    navigacia()
                                    left_speed = vl
                                    right_speed = vr
                                else:
                                    if ball_y < 0:
                                        left_speed = -5
                                        right_speed = -10
                                    else:
                                        left_speed = -10
                                        right_speed = -5
                        else:
                            if real_robot_angle <= 274:
                                if real_robot_angle >= 264: 
                                    left_speed = 10
                                    right_speed = 10
                                else:
                                    left_speed = 3
                                    right_speed = -3
                            else:
                                left_speed = -3
                                right_speed = 3     
                                         
                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                

my_robot = MyRobot()
my_robot.run()
