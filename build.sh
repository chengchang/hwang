#!/bin/bash

PKG=hwang

pushd build
if make -j$(nproc); then
    popd
    cd python
    if rm -rf dist && \
        python3 setup.py bdist_wheel;
    then
        cwd=$(pwd)
        # cd to /tmp to avoid name clashes with Python module name and any
        # directories of the same name in our cwd
        pushd /tmp
        (yes | pip3 uninstall $PKG)
        (yes | pip3 install $cwd/dist/*)
        popd
    fi
else
    popd
fi
