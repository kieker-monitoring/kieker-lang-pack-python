#!/bin/sh

pip uninstall kieker-monitoring-for-python
python3 -m build
pip install dist/kieker_monitoring_for_python-0.0.10.tar.gz