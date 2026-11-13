#!/bin/sh

pip uninstall kieker-monitoring-for-python
cd ./kieker-lang-pack-python
python3 -m build
pip install dist/kieker_monitoring_for_python-0.0.2.tar.gz