[app]
title = 抖音监测
package.name = dymonitor
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 必须包含 kivymd 和 requests
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,urllib3,certifi,idna,charset-normalizer

orientation = portrait
fullscreen = 0

# 安卓权限：网络权限
android.permissions = INTERNET, FOREGROUND_SERVICE

# 自动唤起浏览器可能需要的权限
android.api = 33
android.minapi = 21
