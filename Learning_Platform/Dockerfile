FROM node:23.1-slim

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . .

EXPOSE 8800

CMD ["npm", "run", "serve"]