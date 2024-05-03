FROM osrf/ros:noetic-desktop-full

# So disable permissions required for further installations
ENV DEBIAN_FRONTEND noninteractive 
# Test
SHELL ["/bin/bash", "-c"]

RUN apt-get update \
    && apt-get install -y \
    python3-pip \
    python3-catkin-tools \
    git \
    tmux \
    vim \
    ros-noetic-husky-simulator \
    ros-noetic-turtlebot3-msgs \
    ros-noetic-turtlebot3 \
    ros-noetic-joy ros-noetic-teleop-twist-joy \
    && rm -rf /var/lib/apt/lists/*       #remove package lists that were downloaded


# Install required Python packages
RUN pip install opencv-python==4.8.0.74 \
                scikit-image \
                pillow==10.2.0 \
                tensorboard \
                matplotlib \
                tqdm \
                timm==0.5.4 \
                torch torchvision torchaudio


RUN mkdir -p /home/development
RUN mkdir -p /home/data
WORKDIR /home/


# Let's make a new user only if required

# ARG USER_ID=1000
# ARG GROUP_ID=1000    

# ARG USERNAME=embereye

# # Create user and group
# RUN groupadd -g ${GROUP_ID} ${USERNAME} \
#     && useradd -u ${USER_ID} -g ${GROUP_ID} -ms /bin/bash ${USERNAME}

# # Add user to sudo and dialout groups
# RUN usermod -aG sudo,dialout ${USERNAME}

# # Grant sudo privileges without password prompt
# RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# USER $USERNAME

# # Run rosdep update, add ROS, Gazebo, and colcon setup to ros user's .bashrc
# RUN sudo apt-get update \
#     && rosdep update \
#     && echo 'source /opt/ros/noetic/setup.bash' >> /home/$USERNAME/.bashrc

# # Create a workspace

# # Copy code into workspace, run rosdep install for workspace, build, and source setup in ros user's
# COPY --chown=$USERNAME ./src src
# RUN source /opt/ros/noetic/setup.bash \
#     && sudo rosdep install --from-paths . --ignore-src -r -y --rosdistro=noetic \
#     && catkin_make \
#     && echo 'source ~/workspace/install/local_setup.bash' >> /home/$USERNAME/.bashrc \
#     && echo 'source ~/workspace/devel/setup.bash' >> /home/$USERNAME/.bashrc
