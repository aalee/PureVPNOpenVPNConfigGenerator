#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil


def cleanup(file_or_folder):
    try:
        if os.path.isfile(file_or_folder):
            os.remove(file_or_folder)
        elif os.path.isdir(file_or_folder):
            shutil.rmtree(file_or_folder)
    except IOError:
        pass
