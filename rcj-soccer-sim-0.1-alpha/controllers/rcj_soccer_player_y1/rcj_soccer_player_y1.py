# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math

# You can also import scripts that you put into the folder with controller
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import utils

import time
a = 0
e = 0
f = 0
g = 0

k = 0

robotX = []
robotY = []
global vl,vr
vl = 0
vr = 0
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
                
                global a
                if a == 0:
                    if robot_x < 0:
                        polovica = -1
                    else:
                        polovica = 1
                    a = 1
                
                
                def get_angles(pos1_x, pos1_y):
                    if polovica == 1:    
                        pos2_x = 75
                    else:
                        pos2_x = -75
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
               
                def novy_uhol():
                    if robot_y < 0:
                        u = 90 + get_angles(robot_x, robot_y)
                    else:
                        u = 90 - get_angles(robot_x, robot_y)
                    return u
                
                #def sanca():
                #    if ball_x < 1 and ball_x > -1 and ball_y < 1 and ball_y > -1:
                #        if direction == 0:
                #            vl = -8
                #            vr = -8
                #        else:
                #            vl = direction * 8
                #            vr = direction * -8
                
                def lokalizacia():
                    if ball_y < 15 and ball_y > -15:
                        lokalita = "stred"
                    else:
                        if polovica == 1:
                            if ball_x > 35: 
                                if ball_y < 0:
                                    lokalita = "vpravo"
                                else:
                                    lokalita = "vlavo"
                            else:
                                lokalita = "stoj"
                        else:
                            if ball_x > 35: 
                                if ball_y < 0:
                                    lokalita = "vpravo"
                                else:
                                    lokalita = "vlavo"
                            else:
                                lokalita = "stoj"
                    return lokalita
                        
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
                    global uhol
                    uhol = novy_uhol()
                
            
                def cakaj():
                   global e, f, g
                   g = 1 
                   if e == 0:
                       global start_time, v
                       start_time = time.time()
                       e = 1
                       v = 0
                   else:
                       if f == 1:
                           if (time.time() - start_time) > 3:
                               if polovica == 1:
                                   if robot_x < 78 and robot_x > 72:
                                       g = 0
                                       e = 0
                                       f = 0
                                       v = 0
                                   else:    
                                       v = 6
                               else:
                                   if robot_x > -78 and robot_x < -72:
                                       g = 0
                                       e = 0
                                       f = 0
                                       v = 0
                                   else:    
                                       v = 6
                       else:
                           if (time.time() - start_time) > 5:
                               if polovica == 1:
                                   if robot_x > 48:
                                       v = -6
                                   else:
                                       if f == 0:
                                           start_time = time.time()
                                           v = 0
                                           f = 1
                               else:
                                   if robot_x < -48:
                                       v = -6
                                   else:
                                       if f == 0:
                                           start_time = time.time()
                                           v = 0
                                           f = 1    
                           else:
                               v = 0
                   
                def domov():
                    global uhol, vl, vr
                    if k == 1:
                        if robotX[0] == robotX[1] and robotY[0] == robotY[1]:
                            if real_robot_angle - 2 <= uhol and real_robot_angle + 2 >= uhol:
                                vl = -7
                                vr = -7
                            else:
                                rozdiel = real_robot_angle - uhol
                                if rozdiel > 0:
                                    vl = -2
                                    vr = 2
                                else:
                                    vl = 2
                                    vr = -2
                        else:       
                            uhol = novy_uhol()
            
                
                if polovica == 1:
                    if ball_x < 25:
                        global g
                        if robot_x > 0 and g == 1:
                            cakaj()
                            left_speed = v
                            right_speed = v
                        else:
                            g = 0
                            if robot_x < 78 and robot_x > 72:
                                if robot_y < 5 and robot_x > -5:
                                    if real_robot_angle < 275 and real_robot_angle > 265:
                                        cakaj()
                                        left_speed = v
                                        right_speed = v
                                    else:
                                        left_speed = -3
                                        right_speed = 3
                                else:
                                    if g == 0:
                                        domov()
                                        left_speed = vl
                                        right_speed = vr
                            else:       
                                if g == 0:
                                    domov()
                                    left_speed = vl
                                    right_speed = vr  
                                            
                    else:
                        g = 0
                        if lokalizacia() == "stred":
                            if direction == 0:
                                left_speed = -8
                                right_speed = -8
                            else:
                                left_speed = direction * 8
                                right_speed = direction * -8
                        else:
                            if lokalizacia() == "vpravo":
                                left_speed = -10
                                right_speed = -5
                            else:
                                left_speed = -5
                                right_speed = -10
                    
                else:
                    if ball_x > -25:
                        if robot_x < 0 and g == 1:
                            cakaj()
                            left_speed = v
                            right_speed = v
                        else:
                            g = 0
                            if robot_x > -78 and robot_x < -72:
                                if robot_y < 5 and robot_x > -5:
                                    if real_robot_angle < 275 and real_robot_angle > 265:
                                        cakaj()
                                        left_speed = v
                                        right_speed = v
                                    else:
                                        left_speed = -3
                                        right_speed = 3
                                else:
                                    if g == 0:
                                        domov()
                                        left_speed = vl
                                        right_speed = vr
                            else:       
                                if g == 0:
                                    domov()
                                    left_speed = vl
                                    right_speed = vr  
                                            
                    else:
                        g = 0
                        if lokalizacia() == "stred":
                            if direction == 0:
                                left_speed = -8
                                right_speed = -8
                            else:
                                left_speed = direction * 8
                                right_speed = direction * -8
                        else:
                            if lokalizacia() == "stoj":
                                left_speed = 0
                                right_speed = 0
                            else:
                                if lokalizacia() == "vpravo":
                                    left_speed = -10
                                    right_speed = -5
                                else:
                                    left_speed = -5
                                    right_speed = -10        
                                    
                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                
                
my_robot = MyRobot()
my_robot.run()