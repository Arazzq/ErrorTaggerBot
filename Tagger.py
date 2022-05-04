import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []

tekli_calisan = []



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**AysunBot**\n ile Grubunuzdakı Nerdeyse Tüm Üyelere Etiket Ata bilirim \nKomutlar için =======> /help yazın**",
                    buttons=(
                   
		      [Button.url('Məni Qrupa Sal ➕', 'https://t.me/Ayssunbot?startgroup=a')],
                      [Button.url('Support🛠', 'https://t.me/supmerlin')],
                      [Button.url('Rəsmi Kanal📣', 'https://t.me/MerlinUserBot')],
		      [Button.url('Developer👨🏻‍💻', 'https://t.me/Arazdi')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "** AysunBot əmrləri**\n\n**/tag <sebeb> - 5-li Etiket Atar**\n\n**/etag <sebeb> - Emoji ile etiketler**\n\n**/tektag sebeb - Üyeleri Tek Tek Etiketler**\n\n**/admins sebeb - Yöneticileri Tek Tek Tag Eder**\n\n**/start - botu başlatır**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Məni Gruba Ekle➕', 'https://t.me/Ayssunbot?startgroup=a')],
                      [Button.url('Support👨‍💻', 'https://t.me/supmerlin')],
                      [Button.url('Rəsmi Kanal🔖', 'https://t.me/MerlinUserBot')],
		      [Button.url('Developer🧑‍🔧', 'https://t.me/Arazdi')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**Çox özəllikləri Etiket Botu tapmağa Çalışan Grub Sahibləri @Ayssunbot Sizə Görə:\n\n📌 5-li etiket\n📌 Stiker etiket\n📌 Təkli Etiket\n📌 Yalnız Yöneticileri etiketleme\n📌\n\n Belə Çoc özəllikli @ErrorTagger_Bot 'u grubunuza yönetici olarak ekleyip rahatlıkla üyelir , etiket ata bilirsiz **"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Botu Gruba Ekle➕', 'https://t.me/lucitaggerbot?startgroup=a')],
                    ),
                    link_preview=False
                   )


print(">> Bot çalıyor merak etme 🚀 @ozuduqaqaw bilgi alabilirsin <<")
client.run_until_disconnected()



