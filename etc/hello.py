server {
  listen 0.0.0.0:8080
  error_log /home/box/web/error2.log;
  access_log /home/box/web/access2.log;
  location / {
    root /home/box/web/hello.py;
 }
}
