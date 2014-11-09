from irc import IRCclient
from get_my_ip import getIP
import time

nick = "vanaisa"
user = "lunvk 0 * :CHARM"
server = "sinisalo.freenode.net"
port = 6667
bot = IRCclient(server, port, nick, user)
bot.connect()
run = 0
data = ""
time.sleep(20)
bot.message("einojo", getIP())
