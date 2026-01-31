[app]
# (str) 应用标题
title = Douyin Monitor

# (str) 包名
package.name = douyinmonitor

# (str) 域名（包名反转）
package.domain = org.example

# (str) 源代码目录
source.dir = .

# (list) 包含的文件后缀
source.include_exts = py,kv,png,jpg

# (list) 应用依赖
# 核心提示：requests 在 Android 上需要 certifi 来处理 HTTPS 证书
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,urllib3,certifi,idna,charset-normalizer,pyjnius

# (str) 自定义 Java 类路径 (如果有自定义 Java 文件)
# android.add_src = 

# (list) Android 权限
android.permissions = INTERNET

# (int) 目标 Android API (推荐 33 或 34)
android.api = 33

# (int) 最小 API 版本
android.minapi = 21

# (int) Android SDK 版本
# android.sdk = 33

# (int) Android NDK 版本
# android.ndk = 25b

# (bool) 是否自动接受 SDK 许可
android.accept_sdk_license = True

# (str) 屏幕方向
orientation = portrait

# (bool) 指示应用是否全屏
fullscreen = 0

# (list) 架构支持 (GitHub Actions 建议只选这两种，缩短打包时间)
android.archs = arm64-v8a, armeabi-v7a

# (str) 应用版本
version = 0.1

[buildozer]
# (int) 日志级别 (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) 如果打包出错，是否停止
warn_on_root = 1
