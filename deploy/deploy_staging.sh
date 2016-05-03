#!/bin/sh
set -ex

ssh deploy@pycon.jp uptime
# please replace for deployment commands
ssh deploy@pycon.jp sh -c 'date > /tmp/deploy-for-staging'

