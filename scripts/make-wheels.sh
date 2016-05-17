# Dockerfile.wheel 用

set -ex

WHEELHOUSE_OLD=/app/wheelhouse
WHEELHOUSE_NEW=/app/wheelhouse_new

# Python-2.7.11 (cp27mu)向けに依存パッケージをwheel化
/opt/python/cp27-cp27mu/bin/pip wheel -r /app/requirements/online.txt -f ${WHEELHOUSE_OLD} -w ${WHEELHOUSE_NEW}

# wheelのmanylinux化
cd ${WHEELHOUSE_NEW}
for f in ./*linux_*; do
  if [ -f $f ]; then
    auditwheel repair $f -w .
    rm $f
  fi
done

