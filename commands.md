cd ~/environment
 
source school-app/bin/activate

cd ~/p

cd PYTHON/Projects/SchoolAPI

pip install -r requirements.txt

## create DB
sudo mysql -u root -p
pass: hzOMT8yii


CREATE DATABASE school_api;
CREATE USER 'stupns'@'localhost' IDENTIFIED BY 'hzOMT8yii';
GRANT ALL PRIVILEGES ON school_api.* TO 'stupns'@'localhost';

## start DB
mysql -u stupns -p school_api

## commit branches

git checkout -b templates
git add *
git commit 
git push origin templates

git checkout master
git merge templates
git push origin master