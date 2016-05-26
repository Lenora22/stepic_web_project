server {
  listen 0.0.0.0:8080
  error_log /home/box/web/error2.log;
  access_log /home/box/web/access2.log;
  location ^~ /hello/ {
  proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host host;proxysetheaderX−Forwarded−Forhost;proxysetheaderX−Forwarded−Forproxy_add_x_forwarded_for;
    }
 }
}
