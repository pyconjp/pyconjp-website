sudo yum -q -y install git mercurial
sudo yum -q -y install python-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel libjpeg-devel freetype-devel gdbm-devel
sudo yum -q -y install postgresql-devel postgresql-server

sudo service postgresql initdb
sudo service postgresql start
sudo -u postgres psql template1 -c "CREATE DATABASE pyconjp2014;"
sudo -u postgres psql template1 -c "CREATE USER vagrant;"
sudo -u postgres psql template1 -c "ALTER USER vagrant  PASSWORD 'vagrant';"
sudo sh -c "cat << HERE > /var/lib/pgsql/data/pg_hba.conf 2>&1
local   all         all                               md5
host    all         all         127.0.0.1/32          md5
host    all         all         ::1/128               md5
HERE
"
sudo service postgresql restart

sudo mkdir /var/log/pyconjp
sudo chown vagrant /var/log/pyconjp

cat << HERE >> ~/.bashrc 2>&1
export DJANGO_SETTINGS_MODULE=pyconjp.settings.dev
export DB_NAME=pyconjp2014
export DB_USER=vagrant
export DB_PASSWORD="vagrant"
export DB_HOST=localhost
export DB_PORT=
export SECRET_KEY="a;sdlfkajoierajposldjkfa;lskdjfa;lskdjfa"
export LANG=ja_JP.UTF-8
export PIP_DOWNLOAD_CACHE=~/.pip
HERE

source ~/.bashrc

curl -L https://bootstrap.pypa.io/get-pip.py | python - --user
~/.local/bin/pip install --user virtualenv
~/.local/bin/virtualenv ~/.venv
source ~/.venv/bin/activate
pip install -f /vagrant/wheelhouse -r /vagrant/requirements/dev.txt
sh /vagrant/pyconjp/init_db.sh

echo "Finished if no error occured. Pleaes re-login or execute 'source ~/.bashrc'"
echo
echo "You can invoke pyconjp site with: ~/.venv/bin/python /vagrant/manage.py runserver"
