from telethon import TelegramClient, events, sync, functions, types, Button

import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".help"))
async def help(event):
	client.parse_mode = "html"
	await event.edit("""
<b>USERBOT HELP MENU</b>
		  
Umumiy modullar: 63
<== <b>Animatsions</b> ==>
[01] Help - Help menu — .help
[02] Bombs - Animation emojise — .bombs
[03] Loading  - Animation loading — .loading
[04] Emoji  -  Emoji text editor - .emoji <here text>
[05] Dump - Candy dump animate - .dump
[06] ||Sexy - Animation porno - .sexy||
[07] Typer - Animation write text - .type <here text>
[08] Lul - Animatsion lul - .lul
[09] Snake - Snake animation - .snake 
[10] Nothappy - Abimation Nothappy - .nothappy
[11] Clock - Animation clock - .clock
[12] Muah - Animation - .muah
[13] Heart - Animation - .heart
[14] Gym - Animation gymnastic - .gym
[15] Earth - Animation globus - .earth
[16] Moon - Animation - .moon
[17] Candy - Animation - .candy
[18] Smoon - Animation - .smoon
[19] Tmoon - Animation - .tmoon
[20] Clown - Animation - .clown
[21] Star - Butterfly and star animation - .butterfly
[22] Boxs - Color animation - .boxs
[23] Rain - Rain animation - .rain
[24] Clol - "What?" snimation - .clol
[25] Odra - Animation - .odra 
[26] Fleaveme - Animation - .fleaveme
[27] Loveu - Love animation - .loveu
[28] Plane - Animation - .plane
[29] Police - Animation sirena - .police
[30] Jio - Animation - .jio
[31] Solarsystem - Animation - .solarsystem
[32] ||Fuck - Fuck you - .fuck||
[33] React - Reactions - .react help
[34] Snow - Animation snow - .snow
[35] Magic - Animation hearts - .magic
[36] Hearts - Animation hearts - .hearts
[37] Good Night - .gn
[38] Lovely - Animation lovely - .lovely
<== <b>Functions</b> ==>
[39] Userinfo - Username information - .userinfo <reply>
[40] Base64 - shifrlash - .b64 en <reply text> .b64 de <reply encoded message>
[41] M.Q - Memocyte Quote - .mq <reply text>
[42] Mute - Admin function - .mute (m, h, d)
[43] Text to voice - .tts <lang code> <reply message>
[44] Modul o'chirilgan
[45] Clock to bio - datetime - .setbioclock <number>
[46] Clock to nick - firstname clock - .setclock <number> <nickname>
[47] Timer - timer animation - .timer <number>
[48] Afk - Afk mode - .afk-on <text> / .afk-off / .afk-info
[49] Numbers - Numbers - .numbers <number>
[50] Tag all - tag group members - .tagall
[51] N.Q - Nedo Quote - .nq <reply text>
[52] Find - find delete accounts - .finda
[53] Picture save - save the picture - .psave
[54] Remove - Admin function remove delete accounts - .removeakk
[55] Ip trace - ip osint - .iptrace <ip addres>
[56] Rename - .rename <first_name> / <last_name>
[57] Qr code - qr code generator - .qrc create <reply>
[58] Sms flood - Spam message  - .spam <time> <count> <text>
[69] Message save - save  message - .msave
[60] Rgm - reload get message - .rgm
[61] Reverse - reverse text - .rev <reply>
[62] Konspekt - konspekt yozish - .konspekt <reply message>
[63] Tr - Translator - .tr <language code > <reply message>
[++] Animatsion help - .ahelp
				  		  
Developer: @programmer_www
""")
