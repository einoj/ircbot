from irc import IRCclient
import time
import gtk.gdk

nick = "charmcmd"
user = "lunvk 0 * :CHARM"
server = "sinisalo.freenode.net"
port = 6667
channel = "#einojo"
bot = IRCclient(server, port, nick, user)
bot.connect()
bot.join(channel)
bot.block(0)
run = 0
data = ""
while True:
    try:
        data = bot.recv(4096)
    except:
        '''no data yet..'''
   
    if data.find("PING") != -1:
        bot.pong(data.split()[1])
    time.sleep(1)
    if "!cmd start" in data:
	bot.message("#einojo", "Data gathering started")
        run = 1
    while run == 1:
        w = gtk.gdk.get_default_root_window()
        sz = w.get_size()
        pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False,8,sz[0],sz[1])
        pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
        i = 0;
        if (pb != None):
            a = time.asctime() + ".png"
            pb.save(a, "png")
            print a
        else:
            print "no screen"
        time.sleep(12)
        try:
            data = bot.recv(4096)
        except:
            '''no data yet..'''

        if data.find("PING") != -1:
            bot.pong(data.split()[1])
        if "!cmd stop" in data:
            bot.message("#einojo", "Data gathering stopped")
            run = 0
