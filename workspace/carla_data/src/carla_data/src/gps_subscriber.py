#!/usr/bin/python3

import rospy
from sensor_msgs.msg import NavSatFix
from cv_bridge import CvBridge
import cv2

# GNSS = GPS same thing
class GNSSSubscriber(object):
    def __init__(self):
        # Params
        self.gnss = None
        
        # Node cycle rate (in Hz).
        self.loop_rate = rospy.Rate(30)

        # Subscribers
        rospy.Subscriber("/carla/ego_vehicle/gnss", NavSatFix, self.callback)
    
    def callback(self, gnss):
        rospy.loginfo('GNSS received...')
        self.gnss = gnss
        print(self.gnss.latitude)
        print(self.gnss.longitude)
        print(self.gnss.altitude)


    
    def start(self):
        rospy.loginfo("Timing gnss")
        #rospy.spin()
        while not rospy.is_shutdown():
            rospy.loginfo('publishing gnss')
            #br = CvBridge()
            # if self.gnss is not None:
            #     cv2.waitKey(1)
            self.loop_rate.sleep()
        # cv2.destroyAllWindows()


if __name__ == '__main__':
    rospy.init_node("GNSSTransport", anonymous=True)
    image_subcriber = GNSSSubscriber()
    image_subcriber.start()
