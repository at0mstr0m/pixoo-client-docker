# https://jsramblings.com/dockerizing-a-react-app/

FROM node:19.8.1 as builder

ENV NPM_CONFIG_LOGLEVEL info

WORKDIR /app

COPY . .

# check npm works
RUN npm -v

RUN npm ci

# # TODO: check if necessary
# RUN npx update-browserslist-db@latest

RUN npm run build

FROM nginx:1.23.4-alpine as production

ENV NODE_ENV production

COPY --from=builder /app/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]