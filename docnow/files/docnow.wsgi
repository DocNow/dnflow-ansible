#!/opt/docnow/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/docnow/dnflow/")

from ui import app as application
