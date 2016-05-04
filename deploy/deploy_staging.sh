#!/bin/sh
set -ex

ssh deploy@pycon.jp uptime
# please replace for deployment commands
ssh deploy@pycon.jp sudo -u pyconjp /opt/workspace/deploy-scripts/update.sh staging 2016

