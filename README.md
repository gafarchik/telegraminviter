# telegraminviter
## README map
- [1.how it's work](https://github.com/gafarchik/telegraminviter/blob/main/README.md#how-its-work)
- [2.installation](https://github.com/gafarchik/telegraminviter/blob/main/README.md#installation)
    - [install.py](https://github.com/gafarchik/telegraminviter/blob/main/README.md#installpy)
    - [Windows](https://github.com/gafarchik/telegraminviter/blob/main/README.md#windows)
    - [Linux](https://github.com/gafarchik/telegraminviter/blob/main/README.md#linux)
    - [Mac](https://github.com/gafarchik/telegraminviter/blob/main/README.md#mac)
- [3.settings](https://github.com/gafarchik/telegraminviter/blob/main/README.md#settings)
    - [API](https://github.com/gafarchik/telegraminviter/blob/main/README.md#api)
    - [Language](https://github.com/gafarchik/telegraminviter#language)
    - [Color](https://github.com/gafarchik/telegraminviter#color)






## how it's work
it's sample source code of the telegram inviter bot. This bot work by telegram desktop api key. Bot parse users id from other groups and after that add users to selected group
```mermaid
erDiagram
    Bot |o--|{ Parce : start_parsing
    Parce ||--|{ Database : save
    Bot }o..|{ Get_users : start_inviting
    Get_users }|..|{ database : upload
    database }|..|{ Invite : save_to_list
    Invite }|..|{ 
```

[⬆️Map](https://github.com/gafarchik/telegraminviter#readme-map)




## installation
install python 3.9



#### install.py
You can just open install.py and library will be installed 




#### Windows
Install python 3.9 from [python.org](https://www.python.org/downloads/windows/).
Add python to PATH, you can do than in install window
![Alt-текст](https://docs.blender.org/manual/ru/2.83/_images/about_contribute_install_windows_installer.png)

After that open cmd and write

```cd bot_directory```
and 

```python bet.py```



#### Linux
Install python 3.9
```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt install python3.9
```
and check
```
$ python3.9 --version
```
```
Output
Python 3.9.1+
```
after that install library telethon
```
pip3 install telethon
```
open directory with bot
```
cd bot_directory
```
start bot
```
python3 bet.py
```
#### Mac
Install [homebrew](https://brew.sh)
```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
check
```
$ brew doctor
```
```
Output
Your system is ready to brew.
```
install python
```
$ brew install python@3.9
```
open bot path
```
cd bot_path
```
install library
```
pip3 install telethon
```
start bot
```
python3 bet.py
```

[⬆️Map](https://github.com/gafarchik/telegraminviter#readme-map)





## settings
#### API
If you want change api of the bot you can do that in config file
```Python
apiid = 0 #api id
apihash = 'asfaf' #api hash
```
#### Language
in config file you can change translate 

change without variable name
```
cautor = " "
csettingslang = "Settings"
cstartinviting = "Start inviting"
cexitlang = "Exit"
cchangetoken = "Change token"
clanguage = "Change language"
cback = "Back" 
cnumberofaction = 'Enter the number of action: '
cerrornumber = 'Error! Input correct number'
cnewtoken = 'Enter new token: '
csuccess = 'Success! '
cuserinvited = 'Users invited: '
centerchat = 'Enter chat: '
cdeletessesion = 'Delete session.session'
cnousers = 'List of users is empty'
cgetusers = 'Parse users from groups'
cuserparsed = 'Users added: '
cyouchat = 'Enter your chat: '
cerrorrstext = "Errors: "
centercount = 'Enter user count: '
cuploadingtext = 'Uploading...'
cuploaduserstext = 'Upload users from database'
csleeptimetext = 'Sleep time'
csleeptimechtext = 'Enter sleep time'
```
#### Color
if you want change colour you need special color codes
you change only code without variable name

```Python
red = "\033[1;31m"
black1 = "\033[0m"
cyan = "\033[1;32m"
green = "\033[1;36m"
```

codes:
```Python
Color_Off="\[\033[0m\]"       # Text Reset

# Regular Colors
Black="\[\033[0;30m\]"        # Black
Red="\[\033[0;31m\]"          # Red
Green="\[\033[0;32m\]"        # Green
Yellow="\[\033[0;33m\]"       # Yellow
Blue="\[\033[0;34m\]"         # Blue
Purple="\[\033[0;35m\]"       # Purple
Cyan="\[\033[0;36m\]"         # Cyan
White="\[\033[0;37m\]"        # White

# Bold
BBlack="\[\033[1;30m\]"       # Black
BRed="\[\033[1;31m\]"         # Red
BGreen="\[\033[1;32m\]"       # Green
BYellow="\[\033[1;33m\]"      # Yellow
BBlue="\[\033[1;34m\]"        # Blue
BPurple="\[\033[1;35m\]"      # Purple
BCyan="\[\033[1;36m\]"        # Cyan
BWhite="\[\033[1;37m\]"       # White

# Underline
UBlack="\[\033[4;30m\]"       # Black
URed="\[\033[4;31m\]"         # Red
UGreen="\[\033[4;32m\]"       # Green
UYellow="\[\033[4;33m\]"      # Yellow
UBlue="\[\033[4;34m\]"        # Blue
UPurple="\[\033[4;35m\]"      # Purple
UCyan="\[\033[4;36m\]"        # Cyan
UWhite="\[\033[4;37m\]"       # White

# Background
On_Black="\[\033[40m\]"       # Black
On_Red="\[\033[41m\]"         # Red
On_Green="\[\033[42m\]"       # Green
On_Yellow="\[\033[43m\]"      # Yellow
On_Blue="\[\033[44m\]"        # Blue
On_Purple="\[\033[45m\]"      # Purple
On_Cyan="\[\033[46m\]"        # Cyan
On_White="\[\033[47m\]"       # White

# High Intensty
IBlack="\[\033[0;90m\]"       # Black
IRed="\[\033[0;91m\]"         # Red
IGreen="\[\033[0;92m\]"       # Green
IYellow="\[\033[0;93m\]"      # Yellow
IBlue="\[\033[0;94m\]"        # Blue
IPurple="\[\033[0;95m\]"      # Purple
ICyan="\[\033[0;96m\]"        # Cyan
IWhite="\[\033[0;97m\]"       # White

# Bold High Intensty
BIBlack="\[\033[1;90m\]"      # Black
BIRed="\[\033[1;91m\]"        # Red
BIGreen="\[\033[1;92m\]"      # Green
BIYellow="\[\033[1;93m\]"     # Yellow
BIBlue="\[\033[1;94m\]"       # Blue
BIPurple="\[\033[1;95m\]"     # Purple
BICyan="\[\033[1;96m\]"       # Cyan
BIWhite="\[\033[1;97m\]"      # White

# High Intensty backgrounds
On_IBlack="\[\033[0;100m\]"   # Black
On_IRed="\[\033[0;101m\]"     # Red
On_IGreen="\[\033[0;102m\]"   # Green
On_IYellow="\[\033[0;103m\]"  # Yellow
On_IBlue="\[\033[0;104m\]"    # Blue
On_IPurple="\[\033[10;95m\]"  # Purple
On_ICyan="\[\033[0;106m\]"    # Cyan
On_IWhite="\[\033[0;107m\]"   # White

```


[⬆️Map](https://github.com/gafarchik/telegraminviter#readme-map)
