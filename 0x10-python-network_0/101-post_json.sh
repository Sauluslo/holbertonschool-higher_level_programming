#!/bin/bash
# Bash script that sends a JSON POST
curl -s "$1" -d @"$2" -H "Content-Type: application/json"
