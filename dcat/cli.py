#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from core import DCat
import argparse
import sys
from common import *


class DCatCli:
    def __init__(self):
        self.dcat = DCat()

    def program(self):
        parser = argparse.ArgumentParser(
            description='Simple Dockerization of catkin workspace',
            usage='''dcatcli <command> [<args>]

Available commands are:
    init        Initializes Docker Container with given parameters
    remove      Removes Docker Container with given parameters, destroys its data
    recreate    Removes and reinitializes container with given parameters
    run         Runs Docker container with given name
    stop        Stops Docker container with given name
    attach      Drops to container shell with given name
    commit      Commits container state
            '''
        )
        parser.add_argument('command', help="Command to run")
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def init(self):
        parser = argparse.ArgumentParser(
            description="Initializes docker container with given information"
        )
        parser.add_argument('-c', '--config-file', dest="config_file", type=argparse.FileType('r'),
                            help="Config file for DCat, expected as yaml file")
        parser.add_argument('--src-dir', dest="src_dir",
                            help="Source directory of Catkin Workspace")
        parser.add_argument('--name', dest='name',
                            help="Name of the container")
        parser.add_argument('--tag', dest='tag',
                            help="Tag of the container")
        parser.add_argument('--ros-distro', dest="rosdistro",
                            help="ROS Distro name for dockerized catkin")
        args = parser.parse_args(sys.argv[2:])
        print args
        print "NOT IMPLEMENTED YET"

    def remove(self):
        parser = argparse.ArgumentParser(
            description="Removes Docker Container with given parameters, destroys its data"
        )
        parser.add_argument('-c', '--config-file', dest="config_file", type=argparse.FileType('r'),
                            help="Config file for DCat, expected as yaml file")
        parser.add_argument('--src-dir', dest="src_dir",
                            help="Source directory of Catkin Workspace")
        parser.add_argument('--name', dest='name',
                            help="Name of the container")
        parser.add_argument('--tag', dest='tag',
                            help="Tag of the container")
        parser.add_argument('--ros-distro', dest="rosdistro",
                            help="ROS Distro name for dockerized catkin")
        args = parser.parse_args(sys.argv[2:])
        print args
        print "NOT IMPLEMENTED YET"

    def recreate(self):
        parser = argparse.ArgumentParser(
            description="Removes and reinitializes container with given parameters"
        )
        parser.add_argument('-c', '--config-file', dest="config_file", type=argparse.FileType('r'),
                            help="Config file for DCat, expected as yaml file")
        parser.add_argument('--src-dir', dest="src_dir",
                            help="Source directory of Catkin Workspace")
        parser.add_argument('--name', dest='name',
                            help="Name of the container")
        parser.add_argument('--tag', dest='tag',
                            help="Tag of the container")
        parser.add_argument('--ros-distro', dest="rosdistro",
                            help="ROS Distro name for dockerized catkin")
        args = parser.parse_args(sys.argv[2:])
        print args
        print "NOT IMPLEMENTED YET"

    def run(self):
        parser = argparse.ArgumentParser(
            description="Runs Docker container with given name"
        )
        parser.add_argument('-c', '--config-file', dest="config_file", type=argparse.FileType('r'),
                            help="Config file for DCat, expected as yaml file")
        parser.add_argument('--src-dir', dest="src_dir",
                            help="Source directory of Catkin Workspace")
        parser.add_argument('--name', dest='name',
                            help="Name of the container")
        parser.add_argument('--tag', dest='tag',
                            help="Tag of the container")
        parser.add_argument('--ros-distro', dest="rosdistro",
                            help="ROS Distro name for dockerized catkin")
        args = parser.parse_args(sys.argv[2:])
        print args
        print "NOT IMPLEMENTED YET"

    def stop(self):
        parser = argparse.ArgumentParser(
            description="Stops Docker container with given name"
        )
        parser.add_argument('--name', dest='name',
                            help="Name of the container")
        parser.add_argument('--tag', dest='tag',
                            help="Tag of the container")
        args = parser.parse_args(sys.argv[2:])
        print args
        print "NOT IMPLEMENTED YET"

    def attach(self):
        parser = argparse.ArgumentParser(
            description="Drops to container shell with given name"
        )
        parser.add_argument('--name', dest='name',
                            help="Name of the container")
        parser.add_argument('--tag', dest='tag',
                            help="Tag of the container")
        args = parser.parse_args(sys.argv[2:])
        print args
        print "NOT IMPLEMENTED YET"

    def commit(self):
        parser = argparse.ArgumentParser(
            description="Commits container state"
        )
        parser.add_argument('--name', dest='name',
                            help="Name of the container")
        parser.add_argument('--tag', dest='tag',
                            help="Tag of the container")
        args = parser.parse_args(sys.argv[2:])
        print args
        print "NOT IMPLEMENTED YET"


def main():
    cli = DCatCli()
    cli.program()


if __name__ == "__main__":
    main()
