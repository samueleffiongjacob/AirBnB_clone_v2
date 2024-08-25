# The above instruction to start code base

Create A virtual environment
 am actively using wsl on linux u can us what best for by googling here is a qucik [startup](https://realpython.com/python-virtual-environments-a-primer/)

```bash
# create a venv
$ $ python3 -m venv venv
# activate it
$ $ source venv/bin/activate
# install package
$ (venv) $ python -m pip install <package-name>
$ 
```

## to use console.py read [view](./README.md) and use from there.

```bash
# to test if tjings worsk  fine 
$ pip install pycodestyle
# writing query form terminal
$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
# remember to create a docker containier leave password empty
$ cat setup_mysql_dev.sql | docker exec -i alx_docker mysql -uroot

$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db

$ echo "SHOW DATABASES;" | docker exec -i alx_docker mysql -uhbnb_dev -p'hbnb_dev_pwd' | grep hbnb_dev_db
$ echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
$ echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | docker exec -i alx_docker mysql -uroot

# test server
$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
$ cat setup_mysql_test.sql | docker exec -i alx_docker mysql -uroot

$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
$ echo "SHOW DATABASES;" | docker exec -i alx_docker mysql -uhbnb_test -p'hbnb_test_pwd' | grep hbnb_test_db

$ echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
$ echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | docker exec -i alx_docker mysql -uroot

$ pip install --force-reinstall mysqlclient

$ docker exec -it 4066908c7ad7 bash -c 'echo "create State name=\"California\" ' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 ./console.py

# fetching from temicnal
```
