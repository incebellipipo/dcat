#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import dcat
import argparse
import pkg_resources
from config_loader import config_loader


class DCatCli:
    def __init__(self):
        self.dcat = dcat.DCat()

    def run(self):
        parser = argparse.ArgumentParser(description='Simple Dockerization of catkin workspaces.')
        parser.add_argument('-v', '--version', action='version', version=pkg_resources.require("dcat")[0].version)
        parser.add_argument('-c', '--config-file', dest="config_file", type=argparse.FileType('r'),
                            help="Config file for DCatCli, must be formatted as yaml")

        args = parser.parse_args()

        print config_loader(args.config_file)


def main():
    cli = DCatCli()
    cli.run()

if __name__ == "__main__":
    main()
