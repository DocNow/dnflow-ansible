#!/opt/docnow/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/docnow/")

from dnflow import app as application
