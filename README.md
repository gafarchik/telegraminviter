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
    Bot ||--|{ Parce : 
    Parce ||--|{ Database : save
    Bot }|..|{ Get users : upload
    Get users }||--|{ Database
    database }||--|{ Invite
```

## installation
install python 3.9
#### install.py
You can just open install.py and library will be installed 
#### Windows
Install python 3.9 from [python.org](https://www.python.org/downloads/windows/)\n
Add python to PATH, you can do than in install window
![Alt-текст](https://docs.blender.org/manual/ru/2.83/_images/about_contribute_install_windows_installer.png)
#### Linux
#### Mac
## examples
