# -*- coding: utf-8 -*-
# Thanks for FadhiilRachman and TCR TEAM
# I JUST FORKED
from linepy import *
import time,random,sys,json,codecs,threading,glob,re,datetime
from datetime import timedelta, date

#cl = LineClient() ----> Buat Login by QR
cl = LineClient(authToken='')
cl.log("Auth Token : " + str(cl.authToken))

# Initialize LineChannel with LineClient
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

#ki = LineClient() ----> Buat Login by QR
ki = LineClient(authToken='')
ki.log("Auth Token : " + str(ki.authToken))

# Initialize LineChannel with LineClient
channel2 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel2.channelAccessToken))

#kk = LineClient() ----> Buat Login by QR
kk = LineClient(authToken='')
kk.log("Auth Token : " + str(kk.authToken))

# Initialize LineChannel with LineClient
channel3 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel3.channelAccessToken))

#kc = LineClient() ----> Buat Login by QR
kc = LineClient(authToken='')
kc.log("Auth Token : " + str(kc.authToken))

# Initialize LineChannel with LineClient
channel4 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel4.channelAccessToken))

#km = LineClient() ----> Buat Login by QR
km = LineClient(authToken='')
km.log("Auth Token : " + str(km.authToken))

# Initialize LineChannel with LineClient
channel5 = LineChannel(km)
km.log("Channel Access Token : " + str(channel5.channelAccessToken))

poll = LinePoll(cl)
poll2 = LinePoll(ki)
poll3 = LinePoll(kk)
poll4 = LinePoll(kc)
poll5 = LinePoll(km)
creator = ["udf060a89ebb2af83af77edddb767c329"]
Qmid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Kmid = km.getProfile().mid
KAC = [cl,ki,kk,kc,km]
Bots = [Qmid,Amid,Bmid,Cmid,Kmid,admin]
responsename = cl.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = kk.getProfile().displayName
responsename4 = kc.getProfile().displayName
responsename5 = km.getProfile().displayName

# Receive messages from LinePoll
def SEND_MESSAGE(op):
    '''
        This is sample for implement BOT in LINE group
        Invite your BOT to group, then BOT will auto accept your invitation
        Thanks for Fadhiil Rachman.
        > hi
        > /author
        > responsename
        > masuk
        > keluar
    '''
    msg = op.message   
    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from
    try:
        if msg.text is None:
            return
        elif text.lower() == 'hi':
            contact = cl.getContact(sender)
            cl.log('[%s] %s' % (contact.displayName, text))
            cl.sendMessage(msg.to, 'Hi too! How are you?')
        elif text.lower() == '/author':
            contact = cl.getContact(sender)
            cl.log('[%s] %s' % (contact.displayName, text))
            cl.sendMessage(msg.to, 'My author is linepy')            
        elif text.lower() == "responsename":
            cl.sendMessage(msg.to,responsename)
            ki.sendMessage(msg.to,responsename2)
            kk.sendMessage(msg.to,responsename3)
            kc.sendMessage(msg.to,responsename4)
            km.sendMessage(msg.to,responsename5)
        elif text.lower() in ["keluar"]:
               ki.leaveGroup(msg.to)
               kk.leaveGroup(msg.to)
               kc.leaveGroup(msg.to)
               km.leaveGroup(msg.to)
        elif text.lower() in ["masuk"]:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventedJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                G = cl.getGroup(msg.to)
                G.preventedJoinByTicket = True
                cl.updateGroup(G)
                G.preventedJoinByTicket(G)
                cl.updateGroup(G)
    except Exception as e:
        cl.log("[SEND_MESSAGE] ERROR : " + str(e))
    
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        cl.acceptGroupInvitation(op.param1)
        ki.acceptGroupInvitation(op.param1)
        kk.acceptGroupInvitation(op.param1)
        kc.acceptGroupInvitation(op.param1)
        km.acceptGroupInvitation(op.param1)
    except Exception as e:
        cl.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        cl.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

# Add function to LinePoll
poll.addOpInterruptWithDict({
    OpType.SEND_MESSAGE: SEND_MESSAGE,
    OpType.NOTIFIED_KICKOUT_FROM_GROUP: NOTIFIED_KICKOUT_FROM_GROUP,
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})

while True:
    poll.trace()
