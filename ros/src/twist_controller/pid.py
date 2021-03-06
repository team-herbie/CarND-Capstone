MIN_NUM = float('-inf')
MAX_NUM = float('inf')

import rospy


# author: udacity, carstenMIELENZ
class PID(object):


    def __init__(self, kp, ki, kd, mn=MIN_NUM, mx=MAX_NUM):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.min = mn
        self.max = mx

        self.int_val = self.last_int_val = self.last_error = 0.


    def reset(self):
        self.int_val = 0.0
        self.last_int_val = 0.0


    def step(self, error, sample_time):
        self.last_int_val = self.int_val

        integral = self.int_val + error * sample_time
        derivative = (error - self.last_error) / sample_time

        y = self.kp * error + self.ki * self.int_val + self.kd * derivative

        val = max(self.min, min(y, self.max))

        # rospy.logdebug('PID::step y, val, cte (max, min) = %f,  %f,  %f (%f, %f) ',
        #                 y, val, error, self.max, self.min)

        if val > self.max:
            val = self.max
        elif val < self.min:
            val = self.min
        else:
            self.int_val = integral
        self.last_error = error

        # rospy.logdebug('PID::step return %f ',val)
        return val
