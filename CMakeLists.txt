cmake_minimum_required(VERSION 2.8.3)
project(phidgets_interface)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

 add_message_files(
   FILES
   DeviceInfo.msg
 )
 
 add_service_files(
  FILES
  ProximityStatus.srv
)

 generate_messages(
   DEPENDENCIES std_msgs
 )

catkin_package(
  #INCLUDE_DIRS include
  LIBRARIES phidgets_interface
  CATKIN_DEPENDS rospy std_msgs message_runtime
  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)




