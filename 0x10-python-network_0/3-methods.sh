#!/bin/bash
#displays all HTTP methods the server will accept.
curl -sI "$1" | grep -i "allow:"| cut -f2- -d" "
