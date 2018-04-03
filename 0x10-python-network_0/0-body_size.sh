#!/bin/bash
# curls input to find the size of the webpage in bytes
curl -sI $1 | grep Content-Length | rev | cut -d':' -f1 | rev | cut -c2-
