import socket

class IRCclient:
    def __init__(self, server, port, nick, user):
        self.server = server
        self.port = port
        self.nick = nick
        self.user = user
        #AF_INET specified to use the IPv4 Internet protocol
        #SOCK_STREAM provied sequenced, reliable, two-way, connection-nased byte streams        
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.server, self.port))
        self.irc.send("NICK " + self.nick+ "\r\n")
        self.irc.send("USER " + self.user + "\r\n")
        print(self.irc.recv(4096))

    def join(self, channel):
        self.irc.send("JOIN " + channel + "\r\n")

    def message(self, msgtarget, msg):
        self.irc.send("PRIVMSG " + msgtarget + " " + msg)

    def recv(self, buflen):
        return self.irc.recv(buflen)

    def pong(self, server):
        self.irc.send("PONG " + server + "\r\n")

    def block(self, block):
	self.irc.setblocking(block)
