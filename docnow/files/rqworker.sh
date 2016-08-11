#!/bin/bash

source /opt/docnow/bin/activate
cd /home/docnow/dnflow/

rq worker &
