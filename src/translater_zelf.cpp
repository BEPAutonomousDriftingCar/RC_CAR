#include "ros/ros.h"
#include <string>
#include "sensor_msgs/Imu.h"
#include "sensor_msgs/MagneticField.h"
#include "geometry_msgs/QuaternionStamped.h"
#include "geometry_msgs/PoseStamped.h"
#include "nav_msgs/Odometry.h"
#include "donutdevice/Steer.h"
#include "donutdevice/IntWheels.h"
#include "donutdevice/Donut.h"
#include <sstream>

class Translater
{
  public:
  Translater()
  {
  ROS_INFO("Starting translater node"); //Message to terminal
  imu_pub = n.advertise<sensor_msgs::Imu>("imu/data_raw", 10);
  mag_pub = n.advertise<sensor_msgs::MagneticField>("imu/mag", 10);
  wheels = n.advertise<geometry_msgs::QuaternionStamped>("wheels", 10);
  steer = n.advertise<donutdevice::Steer>("steer", 10);
  vo = n.advertise<nav_msgs::Odometry>("vo", 10);

  donutsub = n.subscribe("donut", 1, &Translater::donutCallback, this);
  mocapsub = n.subscribe("ground_pose", 1, &Translater::mocapCallback, this);
  }
  
  void donutCallback(const donutdevice::Donut::ConstPtr& msg)
  {

    imu_msg.linear_acceleration.x = msg->mpu.linear_acceleration.x;
    imu_msg.linear_acceleration.y = msg->mpu.linear_acceleration.y;
    imu_msg.linear_acceleration.z = msg->mpu.linear_acceleration.z;
        
    imu_pub.publish(imu_msg);
    
  }
  private:
  std::string base_footprint = "DonutDevice/base_link";

  const double pi = 0.26179938779;

  float cov_x =  999;
  float cov_y =  999;
  float cov_z = 999;

  double inttoangle(int intangle){
    double angle;
    angle = (intangle-511)*(0.24719101123);
    return angle;
  }
  int inttoload(int intload){
    if(intload >= 1023){
      intload = intload - 1023;
    }
    return intload;
  }
  ros::NodeHandle n;
  ros::Publisher imu_pub;
  ros::Publisher mag_pub;
  ros::Publisher wheels;
  ros::Publisher steer;
  ros::Publisher vo;

  ros::Subscriber donutsub;
  ros::Subscriber mocapsub;

  nav_msgs::Odometry odom_msg;
  sensor_msgs::Imu imu_msg;
  sensor_msgs::MagneticField mag_msg;
  geometry_msgs::QuaternionStamped w_msg;
  donutdevice::Steer s_msg;
  donutdevice::Donut donut_msg;


};


int main(int argc, char **argv)
{
  /**
   * The ros::init() function needs to see argc and argv so that it can perform
   * any ROS arguments and name remapping that were provided at the command line.
   * For programmatic remappings you can use a different version of init() which takes
   * remappings directly, but for most command-line programs, passing argc and argv is
   * the easiest way to do it.  The third argument to init() is the name of the node.
   *
   * You must call one of the versions of ros::init() before using any other
   * part of the ROS system.
   */
  ros::init(argc, argv, "donutdevice");

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */

  Translater Translater;
  ros::spin();
  return 0;
}
