FROM node:20-alpine AS builder

WORKDIR /app

RUN npm install -g @angular/cli

COPY ./package*.json ./
COPY ./package-lock.json ./

RUN npm install

COPY ./ ./

RUN npm run build --omit=dev

FROM nginx:alpine

COPY --from=builder /app/dist/todo_app/browser /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
