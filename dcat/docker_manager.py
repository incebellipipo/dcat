#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import docker
from docker.models import containers

class DockerManager():
    def __init__(self, container_id=None, image=None, command=None, ports=None,  names=None, docker_params=None):

        self.container_id=container_id
        self.image = image
        self.command = command
        self.ports = ports
        self.names = names
        self.docker_params = docker_params



        self.docker_client = docker.from_env()
        self.container = containers.Container()


    def image_check(self, image_name=None):
        """
        TODO, it'll be cool if i set those methods to be static
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
        TODO, it'll be cool if i set those methods to be static
        Pulls ROS docker container from docker hub
        :return:
        """
        img = self.image if image_name is None else image_name
        self.docker_client.images.pull(img)

    def delete_image(self, image_name=None):
        """
        TODO, it'll be cool if i set those methods to be static
        Deletes an image with given name
        :param image_name:
        :return: Nothing
        """
        image = self.image if image_name is None else image_name
        self.docker_client.images.remove(image)

    def is_running(self, image_name=None):
        """
        TODO, how the f$!@ i can check? or should i get state
        Checks if managers container is running, checks if there is any container running with given image name
        :return:
        """
        print "Not implemented yet"
        return False

    def run_container(self, image_name=None):
        """
        Sets image name of docker container if not set, changes it if its set.
        Runs an image with objects docker_params
        :param image_name: Name of the image that'll be run
        :return: nothing
        """
        self.image = self.image if image_name is None else image_name
        self.container = self.docker_client.run(self.image, **self.docker_params)

    def stop_container(self):
        """
        Kill's current container
        :return: Nothing
        """
        self.container.kill()

    def attach_container(self):
        """
        Attaches current container
        :return:
        """
        self.container.attach()

    def commit_container(self):
        """
        Commits the changes to container
        :return:
        """
        self.container.commit()


