#!/bin/sh
set -ex

# please remove this deploy_trial.sh file after merging SAR-553-circleci branch

ssh deploy@pycon.jp uptime
ssh deploy@pycon.jp sudo -u pyconjp /opt/workspace/deploy-scripts/update.sh staging 2016

