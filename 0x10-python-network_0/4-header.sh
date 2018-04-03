#!/bin/bash
# displays body of GET to input webserver with custom header
curl -sH "X-HolbertonSchool-User-Id: 98" $1
