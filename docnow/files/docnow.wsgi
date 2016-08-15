#!/opt/docnow/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/vagrant/dnflow/")

from ui import app as application
