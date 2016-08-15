#!/bin/bash

source /opt/docnow/bin/activate
cd /vagrant/dnflow/

rq worker &
