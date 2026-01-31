from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.lang import Builder
import requests
import webbrowser
import time

# 界面布局
KV = '''
MDScreen:
    md_bg_color: self.theme_cls.bg_normal

    MDCard:
        orientation: "vertical"
        padding: "20dp"
        spacing: "15dp"
        size_hint: 0.85, None
        height: "450dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 2
        radius: [15, ]

        MDLabel:
            text: "直播自动监测"
            font_style: "H5"
            halign: "center"
            size_hint_y: None
            height: "40dp"

        MDTextField:
            id: room_id
            hint_text: "请输入抖音房间号"
            helper_text: "例如：20338629153"
            helper_text_mode: "on_focus"
            mode: "outline"

        MDLabel:
            id: log_display
            text: "状态: 等待启动"
            theme_text_color: "Secondary"
            font_style: "Caption"
            halign: "left"
            valign: "top"

        MDRaisedButton:
            id: action_btn
            text: "开启监测"
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": .5}
            size_hint_x: 0.8
            on_release: app.toggle_monitor()
'''

class MonitorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.is_monitoring = False
        return Builder.load_string(KV)

    def toggle_monitor(self):
        if not self.is_monitoring:
            room = self.root.ids.room_id.text.strip()
            if not room:
                self.root.ids.log_display.text = "错误: 房间号不能为空"
                return
            
            self.is_monitoring = True
            self.root.ids.action_btn.text = "停止监测"
            self.root.ids.action_btn.md_bg_color = (0.8, 0.2, 0.2, 1)
            Clock.schedule_interval(self.check_live, 60) # 60秒检测一次
        else:
            self.stop_monitoring()

    def stop_monitoring(self):
        self.is_monitoring = False
        self.root.ids.action_btn.text = "开启监测"
        self.root.ids.action_btn.md_bg_color = self.theme_cls.primary_color
        Clock.unschedule(self.check_live)
        self.root.ids.log_display.text = "状态: 已停止"

    def check_live(self, dt):
        room_id = self.root.ids.room_id.text.strip()
        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10)"}
        url = f"https://live.douyin.com/{room_id}"
        
        try:
            res = requests.get(url, headers=headers, timeout=5)
            if '"status":2' in res.text or 'flv_pull_url' in res.text:
                self.root.ids.log_display.text = f"[{time.strftime('%H:%M')}] 已开播！正在跳转..."
                webbrowser.open(url)
                self.stop_monitoring()
            else:
                self.root.ids.log_display.text = f"[{time.strftime('%H:%M')}] 未开播，持续监测中..."
        except Exception as e:
            self.root.ids.log_display.text = f"访问失败: 网络错误"

if __name__ == "__main__":
    MonitorApp().run()
