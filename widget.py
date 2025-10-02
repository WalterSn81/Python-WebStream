import sys
import vlc
import os
import subprocess
import re
from PySide6.QtWidgets import QApplication, QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import QTimer
from ui_form import Ui_Widget
from PySide6.QtGui import QIcon, QColor

m3u_bayern1           = "https://dispatcher.rndfnk.com/br/br1/schwaben/mp3/mid"
m3u_bayern3           = "https://dispatcher.rndfnk.com/br/br3/live/mp3/mid"
m3u_top_fm            = "https://topfm.stream40.radiohost.de/topfm-live_mp3-192?addradio&ar-distributor=ffa0&aw_0_1st.playerid=web&aw_0_req.gdpr=true&upd-meta&upd-scheme=https&ref=ffa0&amsparams=ffa0&_art=dD0xNzU4OTcwMDkyJmQ9ZDdiYTkwNDlmNzczNmM4Y2ZkZGU"
m3u_90s90s_millenium  = "https://streams.90s90s.de/90s00s/mp3-192/streams.90s90s.de"
m3u_90s90s_sommerhits = "https://streams.90s90s.de/90s90s-sommerhits/mp3-192/streams.90s90s.de"
m3u_90s90s_boygroups  = "https://streams.90s90s.de/boygroup/aac-64/streams.90s90s.de"
m3u_90s90s_hiphop     = "https://streams.90s90s.de/hiphop/mp3-192/streams.90s90s.de"
m3u_90s90s_digital    = "https://streams.90s90s.de/bawue/mp3-192/streams.90s90s.de"
m3u_80s80s_deutsch    = "https://streams.80s80s.de/deutsch/mp3-192/streams.80s80s.de"
m3u_80s80s_ndw        = "https://streams.80s80s.de/ndw/aac-64/streams.80s80s.de"
m3u_swr1              = "https://dispatcher.rndfnk.com/swr/swr1/bw/mp3/128/stream.mp3"
m3u_swr3              = "https://liveradio.swr.de/sw282p3/swr3/play.mp3"
infoText              = "Systeminformationen werden geladen..."

icons_path              = "/home/pi/radio/icons/"
volume_up_firs_icon     = (icons_path + "audio_2625893p.png"  )
volume_down_firs_icon   = (icons_path + "audio_26258932pp.png")
volume_up_second_icon   = (icons_path + "audio_2625893.png"   )
volume_down_second_icon = (icons_path + "audio_26258932.png"  )
wlan_interface          = "wlan1"

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        #self.setFixedSize(800,480)
        self.showFullScreen()

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.ui.btn_volume_plis.pressed.connect(self.volume_up)
        self.ui.btn_volume_minus.pressed.connect(self.volume_down)
        self.ui.btn_volume_plis.released.connect(self.volume_up_i)
        self.ui.btn_volume_minus.released.connect(self.volume_down_i)
        self.ui.btn_poweroff.clicked.connect(self.shutdown_pi)

        self.add_shadow(self.ui.btn_bayern1)
        self.add_shadow(self.ui.btn_bayern3)
        self.add_shadow(self.ui.btn_top_fm)
        self.add_shadow(self.ui.btn_swr1)
        self.add_shadow(self.ui.btn_swr3)
        self.add_shadow(self.ui.btn_90s90s_boygroups)
        self.add_shadow(self.ui.btn_90s90s_digital)
        self.add_shadow(self.ui.btn_90s90s_hiphop)
        self.add_shadow(self.ui.btn_90s90s_millenium)
        self.add_shadow(self.ui.btn_90s90s_sommerhits)
        self.add_shadow(self.ui.btn_80s80s_deutsch)
        self.add_shadow(self.ui.btn_80s80s_ndw)

        self.ui.btn_bayern1.clicked.connect          (lambda: self.play_station(m3u_bayern1, self.ui.btn_bayern1                   ))
        self.ui.btn_bayern3.clicked.connect          (lambda: self.play_station(m3u_bayern3, self.ui.btn_bayern3                   ))
        self.ui.btn_top_fm.clicked.connect           (lambda: self.play_station(m3u_top_fm, self.ui.btn_top_fm                     ))
        self.ui.btn_swr1.clicked.connect             (lambda: self.play_station(m3u_swr1,self.ui.btn_swr1                          ))
        self.ui.btn_swr3.clicked.connect             (lambda: self.play_station(m3u_swr3, self.ui.btn_swr3                         ))
        self.ui.btn_90s90s_digital.clicked.connect   (lambda: self.play_station(m3u_90s90s_digital, self.ui.btn_90s90s_digital     ))
        self.ui.btn_90s90s_sommerhits.clicked.connect(lambda: self.play_station(m3u_90s90s_sommerhits,self.ui.btn_90s90s_sommerhits))
        self.ui.btn_90s90s_millenium.clicked.connect (lambda: self.play_station(m3u_90s90s_millenium, self.ui.btn_90s90s_millenium ))
        self.ui.btn_90s90s_hiphop.clicked.connect    (lambda: self.play_station(m3u_90s90s_hiphop, self.ui.btn_90s90s_hiphop       ))
        self.ui.btn_90s90s_boygroups.clicked.connect (lambda: self.play_station(m3u_90s90s_boygroups,self.ui.btn_90s90s_boygroups  ))
        self.ui.btn_80s80s_deutsch.clicked.connect   (lambda: self.play_station(m3u_80s80s_deutsch,self.ui.btn_80s80s_deutsch      ))
        self.ui.btn_80s80s_ndw.clicked.connect       (lambda: self.play_station(m3u_80s80s_ndw,self.ui.btn_80s80s_ndw              ))

        self.info_timer = QTimer(self)
        self.info_timer.timeout.connect(self.update_info)
        self.info_timer.start(5000)

        self.update_info()


    def add_shadow(self,button):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setOffset(10, 10)
        shadow.setColor(QColor(0, 0, 0, 160))
        button.setGraphicsEffect(shadow)

    def get_wifi_signal_strength(self, interface=wlan_interface):
        try:
            result = subprocess.run(['iwconfig', interface], capture_output=True, text=True)
            output = result.stdout
            for line in output.splitlines():
                if "Signal level" in line:
                    parts = line.strip().split("Signal level=")
                    if len(parts) > 1:
                        signal_str = parts[1].split(" ")[0]
                        signal_dbm = int(signal_str)
                        percent = max(0, min(100, 2 * (signal_dbm + 100)))
                        return percent
        except Exception as e:
            print(f"Fehler WLAN Signal: {e}")
        return None

    def get_cpu_temperature(self):
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temp_str = f.read().strip()
                temp_c = int(temp_str) / 1000.0
                return temp_c
        except Exception as e:
            print(f"Fehler CPU Temperatur: {e}")
            return None

    def update_info(self):
        wifi = self.get_wifi_signal_strength()
        cpu_temp = self.get_cpu_temperature()
        info = "Systeminformationen: "
        if wifi is not None:
            info += f" WLAN Signal: {wifi}%"
        if cpu_temp is not None:
            info += f" | CPU Temp: {cpu_temp:.1f}°C"
        self.ui.infoText.setText(info)

    def play_station(self, stream_url, button):
        self.set_stream_from_m3u_content(stream_url)
        self.highlight_active_button(button)

    def highlight_active_button(self, active_button):
        buttons = [
            self.ui.btn_bayern1,
            self.ui.btn_bayern3,
            self.ui.btn_80s80s_ndw,
            self.ui.btn_80s80s_deutsch,
            self.ui.btn_90s90s_boygroups,
            self.ui.btn_90s90s_digital,
            self.ui.btn_90s90s_hiphop,
            self.ui.btn_90s90s_millenium,
            self.ui.btn_90s90s_sommerhits,
            self.ui.btn_swr1,
            self.ui.btn_swr3,
            self.ui.btn_top_fm
        ]
        for btn in buttons:
            if btn == active_button:
                btn.setStyleSheet("background-color: #ba5f00; color: white; font-weight: bold;")
            else:
                btn.setStyleSheet("background-color: #2d2d44;color: #f0f0f0;border: none;border-radius: 12px;padding: 12px;")

    def set_stream_from_m3u_content(self, m3u_str):
        urls = self.parse_m3u(m3u_str)
        if urls:
            self.set_stream(urls[0])
        else:
            print("Keine gültigen Streams in m3u Inhalt gefunden.")

    def parse_m3u(self, m3u_str):
        urls = []
        for line in m3u_str.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line)
        return urls

    def set_stream(self, source):
        if source.startswith("http://") or source.startswith("https://"):
            media = self.instance.media_new(source)
            self.player.set_media(media)
            self.player.play()
        else:
            if not os.path.exists(source):
                return
            with open(source, 'r') as f:
                for line in f:
                    if line.strip() and not line.startswith("#"):
                        stream_url = line.strip()
                        media = self.instance.media_new(stream_url)
                        self.player.set_media(media)
                        self.player.play()
                        return

    def shutdown_pi(self):
        subprocess.run(["sudo", "shutdown", "-h", "now"])

    def get_system_volume(self):
        result = subprocess.run(["amixer", "get", "Master"], capture_output=True, text=True)
        matches = re.findall(r"\[(\d+)%\]", result.stdout)
        if matches:
            return int(matches[0])
        return None

    def set_system_volume(self, percent):
        percent = max(0, min(100, percent))
        subprocess.run(["amixer", "set", "Master", f"{percent}%"], check=True)

    def volume_up(self):
        current = self.get_system_volume()
        self.ui.btn_volume_plis.setIcon(QIcon(volume_up_firs_icon))
        if current is not None:
            self.set_system_volume(current + 5)

    def volume_down(self):
        current = self.get_system_volume()
        self.ui.btn_volume_minus.setIcon(QIcon(volume_down_firs_icon))
        if current is not None:
            self.set_system_volume(current - 5)

    def volume_up_i(self):
        self.ui.btn_volume_plis.setIcon(QIcon(volume_up_second_icon))

    def volume_down_i(self):
        self.ui.btn_volume_minus.setIcon(QIcon(volume_down_second_icon))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())