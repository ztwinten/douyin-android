[app]
title = DouyinLiveMonitor
package.name = douyinmonitor
package.domain = org.minyue

source.dir = .
source.include_exts = py,kv,png,jpg,ttf

version = 1.0

requirements = python3,kivy,kivymd,requests

android.python_version = 3.10


orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b

android.gradle_dependencies =
android.enable_androidx = True

android.archs = arm64-v8a,armeabi-v7a

android.accept_sdk_license = True

log_level = 2

[buildozer]
warn_on_root = 0

