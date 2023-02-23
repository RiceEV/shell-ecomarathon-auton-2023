#!/usr/bin/python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String, Float64, Bool
from cv_bridge import CvBridge
import cv2

class TopicCloner(object):
    def __init__(self):
        # Params
        self.throttle = "/throttle_command"
        self.gear = "/gear_command"
        self.brake = "/brake_command"
        self.steering = "/steering_command"
        self.handbrake = "/handbrake_command"

        self.ego_control = "/carla/ego_vehicle/"

        # Subscribers
        rospy.Subscriber(self.throttle, Float64, self.throttle_callback)
        rospy.Subscriber(self.gear, String, self.gear_callback)
        rospy.Subscriber(self.brake, Float64, self.brake_callback)
        rospy.Subscriber(self.steering, Float64, self.steering_callback)
        rospy.Subscriber(self.handbrake, Bool, self.handbrake_callback)

        # Publisher
        self.pub = rospy.Publisher('chatter', String, queue_size=10)

    def throttle_callback(self, msg):
        rospy.loginfo('Throttle received...')
        self.pub()

    def gear_callback(self, msg):
        rospy.loginfo('Gear received...')
        self.image = self.br.imgmsg_to_cv2(msg)

    def brake_callback(self, msg):
        rospy.loginfo('Brake received...')
        self.image = self.br.imgmsg_to_cv2(msg)

    def steering_callback(self, msg):
        rospy.loginfo('Steering received...')
        self.image = self.br.imgmsg_to_cv2(msg)

    def handbrake_callback(self, msg):
        rospy.loginfo('Handbrake received...')
        self.image = self.br.imgmsg_to_cv2(msg)

    def start(self):
        rospy.loginfo("Timing images")
        #rospy.spin()
        while not rospy.is_shutdown():
            rospy.loginfo('publishing image')
            #br = CvBridge()
            if self.image is not None:
                cv2.imshow('image', self.image)
                cv2.waitKey(1)
            self.loop_rate.sleep()
        cv2.destroyAllWindows()

    

    

if __name__ == '__main__':
    rospy.init_node("ImageTransport", anonymous=True)
    image_subcriber = TopicCloner()
    image_subcriber.start()