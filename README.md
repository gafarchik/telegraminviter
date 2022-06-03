# telegraminviter
- [1.how it's work](https://github.com/gafarchik/telegraminviter/blob/main/README.md#how-its-work)
- [2.installation](https://github.com/gafarchik/telegraminviter/blob/main/README.md#installation)
    - [install.py](https://github.com/gafarchik/telegraminviter/blob/main/README.md#installpy)
    - [Windows](https://github.com/gafarchik/telegraminviter/blob/main/README.md#windows)
    - [Linux](https://github.com/gafarchik/telegraminviter/blob/main/README.md#linux)
    - [Mac](https://github.com/gafarchik/telegraminviter/blob/main/README.md#mac)
- [3.examples](https://github.com/gafarchik/telegraminviter/blob/main/README.md#examples)
## how it's work
it's sample source code of the telegram inviter bot. This bot work by telegram desktop api key. Bot parse users id from other groups and after that add users to selected group
```mermaid
erDiagram
    Bot ||--|{ Parce : start_parsing
    Parce ||--|{ Database : save
    Bot }|..|{ Get_users : start_inviting
    Get_users }|..|{ database : upload
    database }|..|{ Invite : save_to_list
    Invite }|..|{ 
```

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
## examples
