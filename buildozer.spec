[app]
# 应用信息
title = Douyin Monitor
package.name = douyinmonitor
package.domain = org.example
version = 0.1

# 资源
source.dir = .
source.include_exts = py,kv

# 依赖
requirements = python3,kivy,kivymd,requests,pyjnius

# 方向
orientation = portrait

[android]
# 权限
permissions = INTERNET
minapi = 21
