FROM node:14.17
WORKDIR /code
COPY package*.json .
RUN npm install
ENV NUXT_HOST=0.0.0.0
COPY . .
RUN npm run generate