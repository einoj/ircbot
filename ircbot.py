from irc import IRCclient


nick = "lunsjbtt"
user = "lunvk 0 * :lunsh"
server = "irc.ifi.uio.no"
port = 6667
channel = "#einojo"
bot = IRCclient(server, port, nick, user)
bot.connect()
while True:
    data = bot.recv(4096)
    print data

    if data.find("PING") != -1:
        bot.pong(data.split()[1])
