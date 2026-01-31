[app]

# (str) Title of your application
title = 抖音直播监测

# (str) Package name
package.name = douyinlivemonitor
package.domain = org.test

# (str) Application version
version = 0.1

# (list) Requirements
# KivyMD is based on Kivy, and the code uses 'requests' and 'jnius' (for Android API access)
requirements = python3,kivy,kivymd,requests

# (str) Main application file
# Assuming the user's code is saved as main.py
source.main = main.py

# (list) Android permissions
# The app uses 'requests' for network access and Android Intent to open a URL, so INTERNET is required.
android.permissions = INTERNET

# (int) Minimum Android API to support.
# Android 11 is API 30. Setting minapi to 30 ensures compatibility with Android 11 and newer.
android.minapi = 30

# (int) Target Android API.
# API 33 (Android 13) is a common stable target for modern Kivy builds.
android.targetsdk = 33

# (str) Orientation (portrait, landscape, all)
orientation = portrait

# (bool) Enable multidex for large apps (often needed for KivyMD)
android.enable_multidex = True

# (str) Icon file
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash file
# presplash.filename = %(source.dir)s/presplash.png
