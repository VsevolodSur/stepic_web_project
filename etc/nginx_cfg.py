server {
    listen       80;
    server_name  192.168.1.201;
    access_log /home/box/web/nginx_access.log;
    error_log  /home/box/web/nginx_error.log;
    location ^~ /uploads {
        root    /home/box/web/;
#        index    index.html;
    }
    location  ~* ^.+\.\w+$ {
        root /home/box/web/public/;
    }
    location /static/ {
        root    /home/box/web/ask/;
        expires 30d;
    }
    location /hello/ {
        proxy_pass http://192.168.1.201:8080/;
        proxy_set_header Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location / {
        proxy_pass http://192.168.1.201:8000/;
        proxy_set_header Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
