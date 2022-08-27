# https://jsramblings.com/dockerizing-a-react-app/

FROM node:alpine as builder

WORKDIR /app

COPY . .

RUN npm ci

RUN npm run build

FROM nginx:alpine as production

ENV NODE_ENV production

COPY --from=builder /app/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]