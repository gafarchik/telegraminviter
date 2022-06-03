import os
import random
import config
import requests
from time import *
from telethon import TelegramClient, events, sync
from telethon.tl.types import InputPeerChannel,PeerUser
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors import UserPrivacyRestrictedError,UserIdInvalidError
from telethon.errors.rpcerrorlist import PeerFloodError,UserNotMutualContactError,UserChannelsTooMuchError,FloodWaitError


api_id = config.apiid
api_hash = config.apihash


client = TelegramClient('session', api_id, api_hash)
client.start()

re=config.red
black = config.black1
gr=config.green
cy=config.cyan

autor = config.cautor
settingslang = config.csettingslang
startinviting = config.cstartinviting
exitlang = config.cexitlang
changetoken = config.cchangetoken
language = config.clanguage
back = config.cback
numberofaction = config.cnumberofaction
errornumber = config.cerrornumber
newtoken = config.cnewtoken
success = config.csuccess
userinvited = config.cuserinvited
enterchat = config.centerchat
deletessesion = config.cdeletessesion
nousers = config.cnousers
getusers = config.cgetusers
userparsed = config.cuserparsed
youchat = config.cyouchat
errorrstext = config.cerrorrstext
entercount = config.centercount
uploadingtext = config.cuploadingtext
uploaduserstext = config.cuploaduserstext
sleeptimetext = config.csleeptimetext
sleeptimechtext = config.csleeptimechtext
deletedatabase = config.cdeletedatabase


users = []
chat = ''
mychat = ''

proxyvar = 0
proxies = []

sleeptime = 60

def start():
    logfile = open('session_log.txt','w')
    logfile.write(strftime("%H:%M:%S", gmtime())+' : start\n')
    logfile.close()
    os.system('cls' if os.name == 'nt' else 'clear')
    prx = open('proxy.txt','a')
    countlines = 0
    with open("proxy.txt") as data:
        countlines = [row.rstrip() for row in data]
    with open('proxy.txt') as fp:
        lines = fp.readlines()

    for x in range(0,len(countlines)):
        proxies.append(lines[x])
    if len(proxies)<5:
        print('proxy error!')
        sleep(5)
        exit()
    else:
        menu()
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{re}\n╔══╗{cy}╔╗ ╔╗╔╗╔╗╔══╗╔════╗╔═══╗╔══╗ ╔══╗{re}╔════╗{cy}
{re}╚╗╔╝{cy}║╚═╝║║║║║╚╗╔╝╚═╗╔═╝║╔══╝║╔╗║ ║╔╗║{re}╚═╗╔═╝{cy}
 {re}║║ {cy}║╔╗ ║║║║║ ║║   ║║  ║╚══╗║╚╝╚╗║║║║  {re}║║{cy}
 {re}║║ {cy}║║╚╗║║╚╝║ ║║   ║║  ║╔══╝║╔═╗║║║║║  {re}║║{cy}
{re}╔╝╚╗{cy}║║ ║║╚╗╔╝╔╝╚╗  ║║  ║╚══╗║╚═╝║║╚╝║  {re}║║{cy}
{re}╚══╝{cy}╚╝ ╚╝ ╚╝ ╚══╝  ╚╝  ╚═══╝╚═══╝╚══╝  {re}╚╝{cy}""")
    print(autor)
    print("")
    print("")
    print("")
def menu():
    logfile = open('session_log.txt','a')
    logfile.write(strftime("%H:%M:%S", gmtime())+' : menu opened\n')
    logfile.close()
    banner()
    print(f"{black}1) "+settingslang)
    print(f"{black}2) {gr}"+startinviting)
    print(f"{black}3) {gr}"+getusers)
    print(f"{black}4) {gr}"+uploaduserstext)
    print(f"{black}5) {re}"+exitlang)
    print("")
    print("")
    answer = int(input(f'{black}'+numberofaction))
    if answer == 1:
        settings()
    if answer == 2:
        if len(users)>=1:
            invite()
        else:
            print(nousers)
            sleep(3)
            menu()
    if answer == 3:
        parse()
    if answer == 4:
        upload_users()
    if answer == 5:
        exit()
def settings():
    logfile = open('session_log.txt','a')
    logfile.write(strftime("%H:%M:%S", gmtime())+' : settings opened\n')
    logfile.close()
    banner()
    print(f"{black}1) "+changetoken)
    print(f"{black}2) "+language)
    print(f"{black}3) "+sleeptimetext)
    print(f"{black}4) "+deletedatabase)
    print(f"{black}5) {re}"+back)
    print("")
    print("")
    answer = int(input(f'{black}'+numberofaction))
    if answer == 1:
        os.remove('session.session')
        menu()
    elif answer == 2:
        changelanguage()
    elif answer == 3:
        global sleeptime
        sleeptime = int(input(f'{black}'+sleeptimechtext+': '))
        settings()
    elif answer == 4:
        file = open('database.txt','w')
        file.close()
        settings()
    elif answer == 5:
        menu()
    else:
        print(errornumber)
        sleep(1)
        settings()
def upload_users():
    logfile = open('session_log.txt','a')
    logfile.write(strftime("%H:%M:%S", gmtime())+' : upload users\n')
    logfile.close()
    banner()
    file = open('database.txt','a')
    print(f"{black}"+uploadingtext)
    countlines = 0
    with open("database.txt") as data:
        countlines = [row.rstrip() for row in data]
    with open('database.txt') as fp:
        lines = fp.readlines()

    for x in range(0,len(countlines)):
        users.append(int(lines[x]))
        logfile = open('session_log.txt','a')
        logfile.write(strftime("%H:%M:%S", gmtime())+' : user number '+str(x)+" uploaded\n")
        logfile.close()
    sleep(2)
    menu()
def get_session(proxies):
    global proxyvar
    logfile = open('session_log.txt','a')
    logfile.write(strftime("%H:%M:%S", gmtime())+' : select new proxy\n')
    logfile.close()
    session = requests.Session()
    if proxyvar>=len(proxies):
        proxyvar = 0
        proxy = proxies[proxyvar]
        session.proxies = {"http": proxy, "https": proxy}
    else:
        proxy = proxies[proxyvar]
        session.proxies = {"http": proxy, "https": proxy}
    proxyvar+=1
    logfile = open('session_log.txt','a')
    logfile.write(strftime("%H:%M:%S", gmtime())+' : new proxy selected\n')
    logfile.close()
    return session
def invite():
    global proxyvar
    logfile = open('session_log.txt','a')
    logfile.write(strftime("%H:%M:%S", gmtime())+' : inviting started\n')
    logfile.close()
    global mychat
    error = 0
    correct = 0
    countproxy = 0
    chatt = str(input(f'{black}'+youchat))
    while "None" in users: 
        users.remove('None')
    for x in range(0,len(users)):
        banner()
        print(users[x])
        print(f'{black}{0} {0}'.format(userinvited,str(correct)))
        print(f'{black}{0} {0}'.format(errorrstext,str(error)))
        mychat = client.get_entity(chatt)
        client.get_dialogs()
        try:
            sleep(sleeptime)
            userss = client.get_entity(users[x])
            s = get_session(proxies)
            s.get(client(InviteToChannelRequest(
                mychat,
                [userss]
            )),timeout=1)
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : user invited!\n')
            logfile.close()
            correct+=1
        except UserPrivacyRestrictedError:
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : User Privacy Error\n')
            logfile.close()
            error +=1
            print(f'{black}Privacy error')
        except UserChannelsTooMuchError:
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : User Channels Too Much Error\n')
            logfile.close()
            error +=1
            print(f'{black}User Channels Too Much Error:')
        except UserNotMutualContactError:
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : User Not Mutual Contact Errorr\n')
            logfile.close()
            print(f'{black} User Not Mutual Contact')
        except PeerFloodError:
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : Flood Error\n')
            logfile.close()
            print(f'{black}Flood Error!')
            sleep(5)
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : Flood sleep end\n')
            logfile.close()
            proxyvar+=1
        except UserIdInvalidError:
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : User invalid id error\n')
            logfile.close()
            error +=1
            print(f'{black}Id error')
        except ValueError as e:
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : Value Error ('+str(e)+")\n")
            logfile.close()
            error+=1
            print(f'{black}Value')
        except TypeError as e:
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : Type Error ('+str(e)+")\n")
            logfile.close()
            error +=1
            print(f'{black}Type')
        except FloodWaitError as e:
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : Flood Error\n')
            logfile.close()
            print(f'{black}Flood wait for ',e.seconds)
            sleep(60)
            logfile = open('session_log.txt','a')
            logfile.write(strftime("%H:%M:%S", gmtime())+' : Flood sleep end\n')
            logfile.close()
            proxyvar+=1
    menu()
def parse():
    logfile = open('session_log.txt','a')
    logfile.write(strftime("%H:%M:%S", gmtime())+' : Parsing start\n')
    logfile.close()
    global chat
    banner()
    chatparse = str(input(enterchat))
    count = int(input(entercount))
    for dialog in client.iter_dialogs():
        if dialog.title == chatparse:
            chat = dialog.id
    for message in client.iter_messages(chat):
        if message.sender_id not in users:
            if len(users)>=count:
                break
                menu()
            else:
                if str(message.sender_id) != "None":
                    users.append(message.sender_id)
                    file = open('database.txt','a')
                    file.write(str(message.sender_id) + "\n")
                    file.close()
        banner()
        print(userparsed + str(len(users)))
        print(message.sender_id)
    sleep(1)
    menu()
def changelanguage():
    logfile = open('session_log.txt','a')
    logfile.write(strftime("%H:%M:%S", gmtime())+' : language changed\n')
    logfile.close()
    config.change()
    settings()

start()
