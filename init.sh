sudo rm /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
