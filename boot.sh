#!/bin/sh

exec gunicorn --reload -b :8082 --access-logfile - --error-logfile - main:api -t 240