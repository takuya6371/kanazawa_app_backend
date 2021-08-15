FROM nginx
RUN mkdir -p /etc/nginx/ssl
WORKDIR /etc/nginx/ssl
ADD server.cert ./
ADD server.key ./
CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]