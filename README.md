# hse-hack-bot

Как это поднять?

```
docker build -t hse-hack-bot-image .
docker rm -f hse-hack-bot
docker run -dit --restart unless-stopped --name hse-hack-bot -e BOT_TOKEN=*** hse-hack-bot-image
```
