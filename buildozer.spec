[app]
title = DouyinAndroid
package.name = douyinapp
package.domain = org.example
source.dir = .
source.main = main.py
version = 0.1

# 关键：依赖声明（根据你的实际需求调整）
requirements = python3,kivy==2.2.1,plyer,requests
# 关键：安卓版本适配
android.api = 31
android.ndk = 25b
android.sdk = 24
# 关键：权限（根据功能补充）
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE
