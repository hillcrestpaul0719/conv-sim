import discord
import config
import random
import time
import requests
import json
import asyncio

show_status = {
    'on': False,
    'speaker': None
}

def curTime():
    localtime = time.localtime(time.time())
    return [localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min]

def scan4activation(shows):
    for i in range(0, len(shows)):
        print(i)
        print(curTime())
        if shows[i]['showtime'] == curTime():
            return i
    return None

def send_webhook(user, text):
    headers = {'Content-Type': 'application/json'}
    data = {
        "content": text,
        "username": user['name'],
        "avatar_url": user['profile_picture'],
    }
    request = requests.post(config.webhook_url, headers=headers,data = json.dumps(data, ensure_ascii=False))
    print(request.text)

# async def send_webhook(user, text):
#     await client.edit_profile(username=user['name'])
#     headers = {'Content-Type': 'application/json'}
#     data = {
#         "content": text,
#         "username": user['name'],
#         "avatar_url": user['profile_picture'],
#     }
#     request = requests.post("https://discordapp.com/api/webhooks/559390785733132288/IZ9TFrFqkYI5VY3uxLMx4juyacsRCLX6QtUU71ViJMf3XFq6eY7MqL08CWV4uCDSApJ6", headers=headers,data = json.dumps(data, ensure_ascii=False))
#     print(request.text)
#     await client.edit_profile(username="???")


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        global show_status
        shows = config.data

        print("task run")
        await self.wait_until_ready()
        print("ready")
        print("hihih")
        print(self.is_closed)
        global show_status
        shows = config.data

        while not self.is_closed:
            print("check")

            newShow = scan4activation(config.data[1])
            print(newShow)
            print(not newShow == None)
            if not newShow == None:
                print("start")
                show_status['on'] = newShow
                print("on")
                for i in shows[1][newShow]['conversation']:
                    show_status['speaker'] = i['speaker']
                    print("send")
                    for j in i['text'].split("\n"):
                        await asyncio.sleep(round(random.uniform(1.5, 3), 2))
                        await self.send_typing(self.get_channel(str(config.channel)))
                        print(len(j)/5)
                        print(len(j)/7)
                        print(random.uniform(len(j)/5, len(j)/7))
                        await asyncio.sleep(round(random.uniform(len(j)/5, len(j)/7), 2))
                        send_webhook(shows[0][i['speaker']], j)
                        # message = await client.send_message(self.get_channel(str(config.channel)), '.')
                        # await client.delete_message(message)
                show_status = {
                    'on': False,
                    'speaker': None
                }
            await asyncio.sleep(60) # task runs every 60 seconds
        print("closed")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        # print(message.author.nick)
        # print(config.data[0][show_status['speaker']]['name'])
        # if message.author.name == config.data[0][show_status['speaker']]['name']:
        #     return

        # print(config.data[0][show_status['speaker']]['name'])
        # print([i['name'] for i in config.data[0]])
        print(message.author.name)
        if (message.author.name in [i['name'] for i in config.data[0]]) or message.author == client.user:
            return

        if show_status['on']:
            send_webhook(config.data[0][show_status['speaker']], "{0.author.mention} ".format(message) + random.choice(config.data[0][show_status['speaker']]['interruption_responses']))
            # await client.send_message(message.channel, random.choice(config.data[0][show_status['speaker']]['interruption_responses']))
            # await message.channel.send()

    async def my_background_task(self):
        # print("task run")
        # await self.wait_until_ready()
        # print("ready")
        # print("hihih")
        # print(self.is_closed)
        # global show_status
        # shows = config.data
        #
        # while not self.is_closed:
        #     print("check")
        #
        #     newShow = scan4activation(config.data[1])
        #     print(newShow)
        #     print(not newShow == None)
        #     if not newShow == None:
        #         print("start")
        #         show_status['on'] = newShow
        #         print("on")
        #         for i in shows[1][newShow]['conversation']:
        #             show_status['speaker'] = i['speaker']
        #             print("send")
        #             for j in i['text'].split("\n"):
        #                 await send_typing(config.channel)
        #                 print(len(j)/5)
        #                 print(len(j)/7)
        #                 print(random.uniform(len(j)/5, len(j)/7))
        #                 await asyncio.sleep(round(random.uniform(len(j)/5, len(j)/7), 2))
        #                 send_webhook(shows[0][i['speaker']], j)
        #         show_status = {
        #             'on': False,
        #             'speaker': None
        #         }
        #     await asyncio.sleep(60) # task runs every 60 seconds
        # print("closed")
        pass

client = MyClient()
client.run(config.token)
