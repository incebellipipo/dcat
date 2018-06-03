#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import yaml

def config_loader(config_file):
    with config_file as f:
        config = yaml.load(f)
    return config
