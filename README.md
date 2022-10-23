# hidden-markov-model
### Reference: This is a school homework. Below explanation is made by the instructor of CmpE 540 in Bogazici University 2021-2022 Spring
Hidden markov model is applied as a solution to problem below.
Take the sequence of sensor measurements from the user and print out the probability distribution of robot’s location at the last time-step.  
Input: on on off off  
Output: Print out the probability distribution P(X4|on1,on2,off3,off4) as a list of values.  
![image](https://user-images.githubusercontent.com/81170575/197388855-e1b8cbe6-c77f-4864-9aa0-5aceaa78219b.png)
- The robot might be in one of the three grids. The map of the environment is known.
- The robot has a short-range distance sensor directed towards right/east direction. The
distance sensor detects whether there is a wall or not on the right with some noise. If there is
a wall on its immediate right, the sensor measures ON with 60%. If there is not wall on its
immediate right grid, the sensor signals ON with 10%.
- At each step the robot executes move-to-the-right action. This action is successful (moves
the robot to the grid on the right) with 80% success, i.e. the robot does not move with 0.2
probability. If the robot is in the right-most grid, move-to-the-right action does not change
the robot’s location.
- The initial whereabouts of the robot is completely unknown, i.e. the robot can be placed in
any grid initially.
