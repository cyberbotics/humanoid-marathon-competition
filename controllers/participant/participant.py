"""Simple robot controller."""

from controller import Robot

angle = 0.0
delta_angle = 0.03

robot = Robot()
time_step = int(robot.getBasicTimeStep())

robot.getDevice("ArmLowerL").setPosition(angle)
robot.getDevice("ArmLowerR").setPosition(angle)

while robot.step(time_step) != -1:
    if angle >= 1.0 or angle <= -1.0:
        delta_angle *= -1
    angle += delta_angle

    robot.getDevice("ArmLowerL").setPosition(angle)
    robot.getDevice("ArmLowerR").setPosition(angle)
