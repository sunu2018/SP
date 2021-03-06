from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse

# Untuk Login Via Qr link 
#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#line.log("Timeline Token : " + str(line.tl.channelAccessToken))

# Untuk Login Via Email & password
#line = LINE('EMAIL', 'PASSWORD')
#line.log("Auth Token : " + str(line.authToken))
#line.log("Timeline Token : " + str(line.tl.channelAccessToken))

line = LINE()
#nadya = LINE("TOKEN KAMU")
#nadya = LINE("Email","Password")
line.log("Auth Token : " + str(nadya.authToken))
channelToken = nadya.getChannelResult()
line.log("Channel Token : " + str(channelToken))

cl = line
oepoll = OEPoll(cl)
All = [cl]
mid = cl.profile.mid
RABots = [mid]
RASuper = ["u7f558dcb5a7dd310f770242d56c3acef"]
RAFamily = RASuper + RABots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

def bot(op):
    try:
        if op.type == 5:
            if Setmain["RAautoadd"] == True:
                cl.sendMessageWithMention(op.param1, op.param1,"Hai","\nsudah ku addback ya\n\n{}".format(str(Setmain["RAmessage"])))
                
        if op.type == 22:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    cl.leaveRoom(op.param1) 
                    
        # Jika tidak bisa autojoin, silahkan cek letter sealing akun bot di setting -> privasi
        # udah dites pakai akun bot yg sudah berteman & letter sealing dinonaktifkan
        if op.type == 13:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = cl.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
                            ra = cl.getGroup(op.param1)
                            cl.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ra = cl.getGroup(op.param1)
                            cl.sendMessageWithMention(op.param1, ra.creator.mid,"hallo","\nsalken group creator...")
                            
        if op.type == 46:
            if op.param2 in RABots:
                cl.removeAllMessages() 
                
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                    
                if msg.contentType == 13:
                    if Setmain["RAautoscan"] == True:
                        msg.contentType = 0
                        cl.sendText(msg.to,msg.contentMetadata["u7f558dcb5a7dd310f770242d56c3acef"])
                        
                elif msg.contentType == 0:
                    if Setmain["RAautoread"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                        ks.sendChatChecked(msg.to, msg_id)
                    if text is None:    
                        return
                    else:
                        
            #---------------------- Start Command ------------------------#
                        
                        if text.lower() == "menu":
                            md = "🔰|RA|Family github version\n\n"
                            md += ".cek「@」\n"
                            md += ".gid\n"
                            md += ".yid\n"
                            md += ".me\n"
                            md += ".spbot\n"
                            md += ".pengaturan\n"
                            md += ".restart\n"
                            md += ".removechat\n"
                            md += ".cekmid 「on/off」\n"
                            md += ".autoread 「on/off」\n"
                            md += ".join\n"
                            md += ".bye\n"
                            md += ".listbl\n"
                            md += ".kick「@」\n"
                            cl.sendText(msg.to, md)
                            
                        elif text.lower() == ".pengaturan":
                            if msg._from in RASuper:
                                md = "🔰|RA|Family github version\n\n"
                                if Setmain["RAautoscan"] == True: md+="✅ Cekmid\n"
                                else: md+="❎ Cekmid\n"
                                if Setmain["RAautoread"] == True: md+="✅ Autoread\n"
                                else: md+="❎ Autoread\n"
                                cl.sendText(msg.to, md)
                                
            #---------------------- On/Off Command -------------------# 
            
                        elif text.lower() == ".autoread on":
                            if msg._from in RASuper:
                                if Setmain["RAautoread"] == False:
                                    Setmain["RAautoread"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Autoread diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".autoread off":
                            if msg._from in RASuper:
                                if Setmain["RAautoread"] == True:
                                    Setmain["RAautoread"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Autoread dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")
                                    
                        elif text.lower() == ".cekmid on":
                            if msg._from in RASuper:
                                if Setmain["RAautoscan"] == False:
                                    Setmain["RAautoscan"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Cekmid diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".cekmid off":
                            if msg._from in RASuper:
                                if Setmain["RAautoscan"] == True:
                                    Setmain["RAautoscan"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Cekmid dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")            
                            
            #---------------- Fungsi Command ------------------#
            
                        elif ".cek" in text.lower():
                            key = eval(msg.contentMetadata["MENTION"])
                            keys = key["MENTIONEES"][0]["M"]
                            ra = cl.getContact(keys)
                            try:
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/{}".format(str(ra.pictureStatus)))
                                cl.sendMessageWithMention(msg.to,ra.mid,"[Nama]\n","\n\n[Bio]\n{}".format(str(ra.statusMessage)))
                            except:
                                pass
                            
                        elif text.lower() == ".gid":
                            cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            cl.sendText(msg.to,msg.to)
                            
                        elif text.lower() == ".yid":
                            cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            cl.sendText(msg.to,msg._from)
                        
                        elif text.lower() == ".me":
                            cl.sendMessageWithMention(msg.to,msg._from,"Hay","\nada apa?")
                            
                        elif text.lower() == ".spbot":
                            start = time.time()
                            cl.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start
                            cl.sendText(msg.to, "%s " % (elapsed_time))
                            
                            start2 = time.time()
                            ki.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start2
                            ki.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start3 = time.time()
                            kk.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start3
                            kk.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start4 = time.time()
                            kc.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start4
                            kc.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start5 = time.time()
                            ks.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start5
                            ks.sendText(msg.to, "%s" % (elapsed_time))
                                
                        elif text.lower() == ".restart":
                            if msg._from in RASuper:
                                cl.sendMessageWithMention(msg.to,msg._from,"","Tunggu Sebentar..")
                                python3 = sys.executable
                                os.execl(python3, python3, *sys.argv)
                                
                        elif text.lower() == ".removechat":
                            if msg._from in RASuper:
                                try:
                                    cl.removeAllMessages(op.param2)
                                    ki.removeAllMessages(op.param2)
                                    kk.removeAllMessages(op.param2)
                                    kc.removeAllMessages(op.param2)
                                    ks.removeAllMessages(op.param2)
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Chat bersih...")
                                except:
                                    pass        
                            
                        elif text.lower() == ".join":
                            if msg._from in RASuper:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                G.preventedJoinByTicket(G)
                                cl.updateGroup(G)
                        
                        elif text.lower() == ".bye":
                            if msg._from in RASuper:
                                ra = cl.getGroup(msg.to)
                                cl.sendMessageWithMention(msg.to,ra.creator.mid,"Maaf","\naku keluar dulu ya..")
                                cl.leaveGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                ks.leaveGroup(msg.to)
                                
                        elif text.lower() == ".listbl":
                            if msg._from in RASuper:
                                if Setmain["RAblacklist"] == {}:
                                    cl.sendMessageWithMention(msg.to, msg._from,"Maaf","\nblacklist kosong")
                                else:
                                    no = 0
                                    hasil = "User\n"
                                    for a in cl.getContacts(Setmain["RAblacklist"]):
                                        no += 1
                                        hasil += "\n" + str(no) + ". " + str(a.displayName)
                                    hasil += "\n\nTotal {} blacklist".format(str(len(cl.getContacts(Setmain["RAblacklist"]))))
                                    cl.sendText(msg.to,hasil)
                                    
                        elif ".kick" in text.lower():
                            if msg._from in RASuper:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in RAFamily:
                                        pass
                                    else:
                                        try:
                                            cl.sendMessageWithMention(msg.to,target,"Maaf","aku kick")
                                            klist = [ki,kk,kc,ks]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                        except:
                                            pass        
                                
                        elif '/ti/g/' in msg.text.lower():
                            if msg._from in RASuper:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["RAautojoin"] == True:
                                        ra = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        ki.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        kk.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        kc.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        ks.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        
                                    else:    
                                        cl.sendMessageWithMention(msg.to,msg._from,"Maaf","\naktifkan auotojoin dulu")

    except Exception as error:
        print (error)
        
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
