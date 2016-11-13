#!/bin/bash

python /home/ec2-user/newbesturfu/manage.py dumpdata --exclude=contenttypes --exclude=auth.permission --indent=4 --natural-foreign > /home/ec2-user/newbesturfu/dumps/dump$$.json
