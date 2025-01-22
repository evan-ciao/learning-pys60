from socket import *
from random import randint

PHRASES =[ u"Beautiful is better than ugly.",
           u"Explicit is better than implicit.",
           u"Simple is better than complex.",
           u"Complex is better than complicated.",
           u"Flat is better than nested.",
           u"Sparse is better than dense.",
           u"Readability counts.",
           u"Special cases aren't special enough to break the rules.",
           u"Although practicality beats purity.",
           u"Errors should never pass silently.",
           u"Unless explicitly silenced.",
           u"In the face of ambiguity, refuse the temptation to guess.",
           u"There should be one-- and preferably only one --obvious way to do it.",
           u"Although that way may not be obvious at first unless you're Dutch.",
           u"Now is better than never.",
           u"Although never is often better than *right* now.",
           u"If the implementation is hard to explain, it's a bad idea.",
           u"If the implementation is easy to explain, it may be a good idea.",
           u"Namespaces are one honking great idea -- let's do more of those!" ]
 
HOST = "192.168.1.13"
PORT = 6969
 
s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
 
while True:
    (cs,addr) = s.accept()
    fortune = PHRASES[randint(0,len(PHRASES)-1)]
    cs.sendall(fortune)
    cs.close()
