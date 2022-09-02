from telegram.ext import *
import responses


def help_command(update,context):
    update.message.reply_text("""/download->category->name
    categories -> movies,tv,games,music,apps,anime,documentaries,xxx,others
    /download->->name -- for searching simply
    """)

def download_torrent(update,context):
    text = str(update.message.text).lower()
    print(text)
    command = text.split("->")
    category=command[1]
    file_name =command[2]
    from py1337x import py1337x
    torrents = py1337x()
    resp = torrents.search(file_name,category=category,sortBy='seeders',order='desc')['items']
    count=0
    for res in resp:
        torrentid = res['torrentId']
        count+=1
        info = torrents.info(torrentId=torrentid)
        content=f""""Name : {info.get('name')}
        Category : {info.get('category')}\n
        Type : {info.get('type')} \n
        Size : {info.get('size')}\n
        Downloads: {info.get('downloads')}\n
        Seeders: {info.get('seeders')}\n
        Magnetlink: {info.get('magnetLink')}"""
        update.message.reply_text(content)
        if(count == 3):
            break
    
    
updater = Updater("5604562055:AAEl1xXZg9w_yN72JygXHttrqtq4oZXc89Q",use_context=True)
dp = updater.dispatcher
#commands
dp.add_handler(CommandHandler('help',help_command))
dp.add_handler(CommandHandler('download',download_torrent))
updater.start_polling(1)
updater.idle()
