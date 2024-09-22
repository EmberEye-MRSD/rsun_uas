# rsun_uas

Houses all utils and launches for overall system bringup on the physical/simulated UAS.

## Simulation Setup

We use PX4 SITL (v1.14.3) along with Gazebo. We assume that the use has a working setup for the same.

``` bash
# Step 1: Clone the repo
cd <path_to_your_ws>/src
git clone https://github.com/EmberEye-MRSD/rsun_uas.git

# Step 2: Update submodules
cd rsun_uas
git submodule update --init --recursive

# Step 3: Build the package
cd <to_workspace_root>
catkin build rsun_uas

# Step 4: Add the following lines to your .bashrc (assumes that you have already added the workspace source command)
export GAZEBO_MODEL_PATH=$(rospack find rsun_uas)/models:${GAZEBO_MODEL_PATH}
export GAZEBO_RESOURCE_PATH=$(rospack find rsun_uas)/worlds:${GAZEBO_RESOURCE_PATH}

# Step 5: Source .bashrc
source ~/.bashrc

# Step 6: Start the simulation
roslaunch rsun_uas mavros_posix_sitl.launch


```



## Docker Instructions

### Building the Docker Image

The running "*rsun_fire_mapping" can be run directly by building it under the docker container.

###### Docker Containter

    Install docker using https://docs.docker.com/engine/install/

```
cd ~/rsun_uas
sudo docker-compose up
```

- Copy all the repositories inside your ros workspace and mount the volume by providing the directory name in the ./run_docker.sh (-v variable)

### Running the Code

#### Run the docker container

```
cd ~/rsun_uas
sudo ./run_docker.sh
```

This will run the docker container and set the variables for gpu access and will mount volumes

#### Build the Code

Inside the docker container

```
cd <ros_ws>
catkin_make
```

 Run all the launch files and nodes.


**Note:** Currently MSO and the Sensor Drivers are a part of the Airlab stack and their dockers and thus are not commited in this workspace.
