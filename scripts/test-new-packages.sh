#!/bin/sh

docker run -it --rm -v `pwd`/wheelhouse:/app/wheelhouse:ro -v `pwd`/wheelhouse_new:/app/wheelhouse_new pyconjp/wheelhouse:2016
rm -R wheelhouse
mv wheelhouse_new wheelhouse

MISSING_WHEELS="`git status -s | grep -v -e '^\s*M'`"

if [ "${MISSING_WHEELS}" != "" ]; then
  echo "Added/Deleted packages are not applied to wheelhouse directory:"
  echo -e "${MISSING_WHEELS}"
  exit 1
fi

