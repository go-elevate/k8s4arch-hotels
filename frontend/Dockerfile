# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY . .
RUN npm install && npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/build /usr/share/nginx/html
EXPOSE 80
WORKDIR /usr/share/nginx/html
COPY ./env.sh .
COPY .env .
RUN chmod +x env.sh
CMD ["/bin/sh", "-c", "/usr/share/nginx/html/env.sh && nginx -g \"daemon off;\""]