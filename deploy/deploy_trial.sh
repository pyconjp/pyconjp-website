#!/bin/sh
set -ex

# please remove this deploy_trial.sh file after merging SAR-553-circleci branch

ssh deploy@pycon.jp uptime
ssh deploy@pycon.jp sh -c 'date > /tmp/hello-from-circleci'

