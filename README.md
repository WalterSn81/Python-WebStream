# Kitchen Radio

My wife wanted a radio in the kitchen — and I had a Raspberry Pi and an LCD touchscreen lying around.

## Background
I first tried **LibreELEC**, but switching between the built-in and USB Wi-Fi wasn’t straightforward.  
Then I tested **Raspberry Pi OS + Kodi**, but the touchscreen only worked in windowed mode — fullscreen broke the back button.

So I wrote a small **Python + Qt** app that simply streams the online radio stations she wanted.  
Nothing fancy — just works.

## Features
- Simple touchscreen UI  
- Plays predefined online radio stations  
- Built for Raspberry Pi with LCD display  

## Requirements
- Raspberry Pi (tested on 3B/4)
- Raspberry Pi OS
- Python 3
- PyQt5 or PySide6
- `vlc` or another audio backend

## Installation
sudo apt update
sudo apt install python3 python3-pyqt5 vlc
git clone https://github.com/<yourname>/kitchen-radio.git
cd kitchen-radio
python3 radio.py


First tests:
![IMG_20251002_073101](https://github.com/user-attachments/assets/1ad09320-ab63-4f5b-b4e0-0312562ee14f)


Result at the end:

<img width="798" height="481" alt="ksnip_20251002-083018" src="https://github.com/user-attachments/assets/88017170-1875-40c0-a7ff-6fc9ffbf4ae2" />
