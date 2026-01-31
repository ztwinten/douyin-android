[app]

# (str) Title of your application
title = 抖音直播监测

# (str) Package name
package.name = douyinlivemonitor
package.domain = org.test

# (str) Application version
version = 0.1

# (str) Source code directory. MUST be explicitly set to the current directory.
source.dir = .

# (list) Requirements
# python3, kivy, kivymd, requests, and 'android' for jnius access
requirements = python3,kivy,kivymd,requests,android

# (str) Main application file
source.main = main.py

# (list) Android permissions
android.permissions = INTERNET

# (int) Minimum Android API to support. Android 11 is API 30.
android.minapi = 30

# (int) Target Android API. API 33 (Android 13) is a stable target.
android.targetsdk = 33

# (str) Orientation (portrait, landscape, all)
orientation = portrait

# (bool) Enable multidex for large apps (often needed for KivyMD)
android.enable_multidex = True

# (str) Icon file
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash file
# presplash.filename = %(source.dir)s/presplash.png
