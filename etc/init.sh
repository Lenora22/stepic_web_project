sudo ln -s /home/box/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/etc/hello.py   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
