import threading
import time
import requests
import re

from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from jnius import autoclass

# Android Intent
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')
PythonActivity = autoclass('org.kivy.android.PythonActivity')


def open_douyin(room_id):
    intent = Intent(Intent.ACTION_VIEW)
    intent.setData(Uri.parse(f"https://live.douyin.com/{room_id}"))
    PythonActivity.mActivity.startActivity(intent)


KV = '''
MDScreen:
    MDTopAppBar:
        title: "抖音直播监测"
        elevation: 4
        pos_hint: {"top": 1}

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"
        pos_hint: {"top": 0.9}

        MDTextField:
            id: room_id
            hint_text: "直播间房间号"
            helper_text: "例如 913343065056"
            helper_text_mode: "on_focus"

        MDTextField:
            id: interval
            text: "60"
            hint_text: "检测间隔（秒）"
            input_filter: "int"

        MDRaisedButton:
            text: "开始监测"
            pos_hint: {"center_x": 0.5}
            on_release: app.start_monitor()

        MDLabel:
            id: log
            text: ""
            halign: "left"
            theme_text_color: "Secondary"
'''


class DouyinApp(MDApp):
    running = False

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"  # Dark 也可以
        return Builder.load_string(KV)

    def log(self, msg):
        self.root.ids.log.text += f"\n{msg}"

    def start_monitor(self):
        if self.running:
            return

        room_id = self.root.ids.room_id.text.strip()
        if not room_id:
            self.log("❌ 请填写房间号")
            return

        try:
            interval = int(self.root.ids.interval.text)
        except:
            interval = 60

        self.running = True
        self.root.ids.log.text = ""
        self.log("▶ 开始监测…")

        threading.Thread(
            target=self.monitor_loop,
            args=(room_id, interval),
            daemon=True
        ).start()

    def monitor_loop(self, room_id, interval):
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
            "Referer": "https://live.douyin.com/"
        }

        while self.running:
            try:
                r = requests.get(
                    f"https://live.douyin.com/{room_id}",
                    headers=headers,
                    timeout=10
                )
                html = r.text

                if "直播已结束" in html or "暂未开播" in html:
                    Clock.schedule_once(lambda dt: self.log("⏳ 未开播"))
                else:
                    m = re.search(r'"status":(\d+)', html)
                    if m and m.group(1) == "2":
                        Clock.schedule_once(lambda dt: self.log("🔥 已开播，打开直播"))
                        Clock.schedule_once(lambda dt: open_douyin(room_id))
                        self.running = False
                        return

            except:
                Clock.schedule_once(lambda dt: self.log("⚠️ 网络异常"))

            time.sleep(interval)


if __name__ == "__main__":
    DouyinApp().run()
