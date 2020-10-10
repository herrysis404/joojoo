[<img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" height="40"/>](https://heroku.com/deploy "Heroku")
## React app file required

- nginx.config

  ```
  server {
    listen       ${PORT:-80};
    server_name  _;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $$uri /index.html;
    }
  }
  ```

- Dockerfile

  ```
  FROM node:14.1-alpine AS builder

  WORKDIR /opt/web
  COPY package.json package-lock.json ./
  RUN npm cache verify
  RUN npm install

  ENV PATH="./node_modules/.bin:$PATH"

  COPY . ./
  RUN npm run build

  FROM nginx:1.17-alpine
  RUN apk --no-cache add curl
  RUN curl -L https://github.com/a8m/envsubst/releases/download/v1.1.0/envsubst-`uname -s`-`uname -m` -o envsubst && \
      chmod +x envsubst && \
      mv envsubst /usr/local/bin
  COPY ./nginx.config /etc/nginx/nginx.template
  CMD ["/bin/sh", "-c", "envsubst < /etc/nginx/nginx.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
  COPY --from=builder /opt/web/build /usr/share/nginx/html
  ```

- static.json
  ```
    {
    "headers": {
      "/**": {
        "Content-Security-Policy": "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self' data:;",
        "Referrer-Policy": "no-referrer, strict-origin-when-cross-origin",
        "Strict-Transport-Security": "max-age=63072000; includeSubDomains",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "X-XSS-Protection": "1; mode=block",
        "Feature-Policy": "accelerometer 'none'; camera 'none'; microphone 'none'"
      }
    },
    "https_only": true,
    "root": "build/",
    "routes": {
      "/**": "index.html"
    }
  }
  ```

## Local for docker
- Build D

## Heroku for docker
- Login heroku
  ```
  heroku login
  ```
- Create new heroku app
  ```
  heroku create
  ```
- Login heroku container
  ```
  heroku container:login
  ```
- Add docker remote git
  ```
  git remote add docker https://git.heroku.com/<your-app-name>.git
  ```
- Build and push your image to heroku docker
  ```
  heroku container:push web --remote docker
  ```
- Release your app to heroku docker
  ```
  heroku container:release web --remote docker
  ```
