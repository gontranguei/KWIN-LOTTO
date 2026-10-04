[app]
title = KWIN LOTTO
package.name = kwinlotto
package.domain = com.kwin.lotto
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,ttf,json
source.exclude_dirs =.buildozer, bin,.github, venv,.git, __pycache__
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
icon.filename = icon.png

[buildozer]
log_level = 2

[app:android]
android.api = 34
android.minapi = 21
android.sdk = 34
android.build_tools = 34.0.0
android.ndk = 25b
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2
android.permissions = INTERNET
