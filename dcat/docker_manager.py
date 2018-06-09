#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import docker

class DockerManager():
    def __init__(self, container_id=None, image=None, command=None, ports=None,  names=None, docker_params=None):

        self.container_id=container_id
        self.image = image
        self.command = command
        self.ports = ports
        self.names = names
        self.docker_params = docker_params

        self.docker_client = docker.from_env()


    def image_check(self, image_name=None):
        """
        Checks if base image of ROS pulled in the system
        :return: True if pulled, otherwise false
        """
        images = self.docker_client.images.list()
        for image in images:
            if image.tags[0] == image_name:
                    return True
        return False

    def image_pull(self, image_name=None):
        """
        Pulls ROS docker container from docker hub
        :return:
        """
        image = self.image_name if image_name is None else image_name
        self.docker_client.images.pull(image)

    def delete_image(self, image_name=None):
        """
        Deletes an image with given name
        :param image_name:
        :return:
        """
        image = self.image_name if image_name is None else image_name
        return self.docker_client.images.remove(image)

    def run_image(self):
        self.docker_client.run(self.image, **self.docker_params)