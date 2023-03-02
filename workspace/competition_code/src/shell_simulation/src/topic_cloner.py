#!/usr/bin/python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String, Float64, Bool
from carla_msgs.msg import CarlaEgoVehicleControl
from cv_bridge import CvBridge
import cv2

class TopicCloner(object):
    def __init__(self):
        # Params
        self.throttle = "/throttle_command"
        self.gear = "/gear_command"
        self.brake = "/brake_command"
        self.steer = "/steering_command"
        self.hand_brake = "/handbrake_command"
        # tbd: self.reverse = ""?

        self.ego_control = "/carla/ego_vehicle/vehicle_control_cmd"
        self.loop_rate = rospy.Rate(30)
        self.ego_sub = rospy.Subscriber("/carla/ego_vehicle/vehicle_control_cmd", CarlaEgoVehicleControl, self.ego_callback)

        self.throttle_pub = rospy.Publisher(self.throttle, Float64, queue_size = 100)
        self.gear_pub = rospy.Publisher(self.gear, String, queue_size = 100)
        self.brake_pub = rospy.Publisher(self.brake, Float64, queue_size = 100)
        self.steer_pub = rospy.Publisher(self.steer, Float64, queue_size = 100)
        self.hand_brake_pub = rospy.Publisher(self.hand_brake, Bool, queue_size = 100)

    def ego_callback(self, msg):
        rospy.loginfo("CarlaEgoVehicleControl received...")

        throttle_msg = Float64()
        throttle_msg.data = msg.throttle
        self.throttle_pub.publish(throttle_msg)

        gear_msg = String()
        if msg.gear == 0:
            gear_msg.data = "forward"
        else:
            gear_msg.data = "backward"

        self.gear_pub.publish(gear_msg)

        brake_msg = Float64()
        brake_msg.data = msg.brake
        self.brake_pub.publish(brake_msg)

        steer_msg = Float64()
        steer_msg.data = msg.steer
        self.steer_pub.publish(steer_msg)

        hand_brake_msg = Bool()
        hand_brake_msg.data = msg.hand_brake
        self.hand_brake_pub.publish(hand_brake_msg)


    def start(self):
        rospy.loginfo("Timing")

        #rospy.spin()
        while not rospy.is_shutdown():
            # rospy.loginfo('publishing')
            #br = CvBridge()
            # if self.image is not None:
            #     cv2.imshow('image', self.image)
            #     cv2.waitKey(1)
            self.loop_rate.sleep()
        #cv2.destroyAllWindows()

    

    

if __name__ == '__main__':
    rospy.init_node("ImageTransport", anonymous=True)
    image_subcriber = TopicCloner()
    image_subcriber.start()