#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from docker_manager import DockerManager

class DCat:
    def __init__(self, catkin_src=None, rosdistro="kinetic", container_tag="dcat"):
        """
        Initialization of DCat managed catkin container
        Container name'll be :
            ${container_tag}:${rosdistro}
        :param catkin_src: Source directory of catkin workspace
        :param rosdistro: Name of ros distro
        :param container_tag: Tag of the container
        """
        self.catkin_src = catkin_src
        self.container_tag = container_tag
        self.rosdistro = rosdistro


        self.image_name = self.container_tag + ":" + self.rosdistro

        self.docker_manager = DockerManager()

