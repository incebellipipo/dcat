#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import docker

class DCat:
    def __init__(self, catkin_src="", image_name="", rosdistro="kinetic"):
        self.catkin_src = catkin_src
        self.image_name = image_name
        self.rosdistro = rosdistro

        self.docker_client = docker.from_env()


    def __str__(self):
        return "Container name: %s, Catkin Source Dir: %s" % (self.image_name, self.catkin_src)

    def image_check(self, tag=None):
        """
        Checks if base image of ROS pulled in the system
        :return: True if pulled, otherwise false
        """
        images = self.docker_client.images.list()
        for image in images:
            if not tag:
                if image.tags[0] == ("ros:" + self.rosdistro):
                    return True
            else:
                if image.tags[0] == tag:
                    return True
        return False

    def image_pull(self, tag=None):
        """
        Pulls ROS docker container from docker hub
        :return:
        """
        if not tag:
            for distro in self.rosdistro:
                self.docker_client.images.pull("ros:" + distro)
        else:
            self.docker_client.images.pull(tag)



    def delete_image(self, image_name=None):
        """
        Deletes an image with given name
        :param image_name:
        :return:
        """
        image_name = self.image_name if image_name is None else image_name
        return self.docker_client.images.remove(image_name)