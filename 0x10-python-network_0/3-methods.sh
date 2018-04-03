#!/bin/bash
# curls input to find the verbs that a webserver it will accept
curl -sI $1 | grep Allow | rev | cut -d':' -f1 | rev | cut -c2-
