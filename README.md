# hse-hack-bot

## Development

Пишите скрипт `run`
```
#!/bin/bash
docker build -t hse-hack-bot-image .
docker rm -f hse-hack-bot
docker run -dit --restart unless-stopped --name hse-hack-bot -e BOT_TOKEN=*** hse-hack-bot-image
```
и радуетесь!

## Quick start

0. Добавляем токен в переменную среды
```
echo "BOT_TOKEN=***" >> .env
```

1. Поднимаем контейнер
```
docker-compose up
```
2. Profit!