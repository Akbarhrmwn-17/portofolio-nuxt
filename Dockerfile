# TAHAP 1: Dapur Node.js (Merakit Web)
FROM node:22-alpine AS builder

WORKDIR /app
ENV NUXT_TELEMETRY_DISABLED=1
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run generate

# TAHAP 2: Etalase Nginx (Menjalankan Web)
FROM nginx:alpine
COPY --from=builder /app/.output/public /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]