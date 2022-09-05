from turtle import up
from telegram.ext import *
import responses


def help_command(update,context):
    update.message.reply_text("""categories -> movies,tv,games,music,apps,anime,documentaries,xxx,others\n
category default -> movies for all\n 
count default -> 5\n
/search.category.count.name -> to download\n
/search...harry potter -> to search randomly\n
/trending.category -> to find top 10 trending torrents\n
/trending. -> to get trending torrents on all categories\n
/top.category -> to find top 10 torrents\n
/top. -> to get top torrents on all categories
    """)


def search_torrent(update,context):
    try:
        text = str(update.message.text).lower()
        command = text.split(".")
        category=command[1]
        times=int(command[2]) if command[2] not in ['',None] else 5
        file_name =command[3]
        from py1337x import py1337x
        torrents = py1337x()
        resp = torrents.search(file_name,category=category,sortBy='seeders',order='desc')['items']
        count=0
        for res in resp:
            torrentid = res['torrentId']
            count+=1
            info = torrents.info(torrentId=torrentid)
            content=f"""Name : {info.get('name')}
    Category : {info.get('category')}\n
    Type : {info.get('type')} \n
    Size : {info.get('size')}\n
    Downloads: {info.get('downloads')}\n
    Seeders: {info.get('seeders')}\n
    Magnetlink find bellow"""
            update.message.reply_text(content)
            content = f"{info.get('magnetLink')}"
            update.message.reply_text(content)
            if(count == times):
                break

    except Exception as e:
        content = """Please give correct syntax.\n
To know syntax give /help"""
        update.message.reply_text(content)



def trending_torrent(update,context):
    try:
        text = str(update.message.text).lower()
        command = text.split(".")
        category=command[1]
        from py1337x import py1337x
        torrents = py1337x()
        resp = torrents.trending(category=category)['items']
        count=0
        for res in resp:
            torrentid = res['torrentId']
            count+=1
            info = torrents.info(torrentId=torrentid)
            content=f"""Name : {info.get('name')}
    Category : {info.get('category')}\n
    Type : {info.get('type')} \n
    Size : {info.get('size')}\n
    Downloads: {info.get('downloads')}\n
    Seeders: {info.get('seeders')}\n
    Magnetlink find bellow"""
            update.message.reply_text(content)
            content = f"{info.get('magnetLink')}"
            update.message.reply_text(content)
            if(count == 10):
                break
    except Exception as e:
        content = """Please give correct syntax.\n
To know syntax give /help"""
        update.message.reply_text(content)

def top_torrent(update,context):
    try:
        text = str(update.message.text).lower()
        command = text.split(".")
        category=command[1]
        from py1337x import py1337x
        torrents = py1337x()
        resp = torrents.top(category=category)['items']
        count=0
        for res in resp:
            torrentid = res['torrentId']
            count+=1
            info = torrents.info(torrentId=torrentid)
            content=f"""Name : {info.get('name')}
    Category : {info.get('category')}\n
    Type : {info.get('type')} \n
    Size : {info.get('size')}\n
    Downloads: {info.get('downloads')}\n
    Seeders: {info.get('seeders')}\n
    Magnetlink find bellow"""
            update.message.reply_text(content)
            content = f"{info.get('magnetLink')}"
            update.message.reply_text(content)
            if(count == 10):
                break
    except Exception as e:
        content = """Please give correct syntax.\n
To know syntax give /help"""
        update.message.reply_text(content)

    
updater = Updater("5604562055:AAEl1xXZg9w_yN72JygXHttrqtq4oZXc89Q",use_context=True)
dp = updater.dispatcher
#commands
dp.add_handler(CommandHandler('help',help_command))
dp.add_handler(CommandHandler('search',search_torrent))
dp.add_handler(CommandHandler('trending',trending_torrent))
dp.add_handler(CommandHandler('top',top_torrent))


updater.start_polling(1)
updater.idle()
