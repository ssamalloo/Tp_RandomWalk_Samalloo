# Tp_RandomWalk_Samalloo

## Description
The package marker_visualizer contains three nodes, that is, publish_marker.py, publish_marker_array.py and random_walk.py.

## To install the package
git clone the repository Tp_RandomWalk_Samalloo
cd ~/random_walk_ws/src
catkin build
source ~/random_walk_ws/devel/setup.bash

## To run the nodes
roscore

rosrun marker_visualizer publish_marker.py

rosrun marker_visualizer publish_marker_array.py

rosrun marker_visualizer random_walk.py

## To view the markers
rosrun rviz
