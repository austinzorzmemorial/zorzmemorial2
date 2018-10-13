import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='zorz location: social services'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'What happendt to aron?':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'what happendt to aron?':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'what happendt to Aron?':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'what happendt to Aron':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'What happendt to Aron':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'What happendt to Aron?':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'What happendt to Zorz?':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'What happendt to zorz?':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'what happendt to zorz?':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'what happendt to Zorz?':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'what happendt to Zorz':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'What happendt to Zorz':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'What happendt to zorz':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
    if message.content == 'what happendt to zorz':
        await client.send_message(message.channel,'he stabbed 2 kids and is now in social service.')
bot.run(str(os.environ('BOT_TOKEN')))
