#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="seg-actions",
    version="0.0.8",
    author="Jorge Niedbalski R.",
    author_email="jnr@metaklass.org",
    description="",
    packages=find_packages(),
    test_suite='nose.collector',
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
    entry_points={
        'mistral.actions': [
            'seg.uncompress_sosreport = seg_actions.uncompress:UncompressSosreportAction',
            'seg.xsos = seg_actions.xsos:XsosAction',
            'seg.pastebinit = seg_actions.pastebinit:PastebinitAction',
        ]
    }
)
