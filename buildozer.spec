[app]
title = KWIN LOTTO
package.name = kwinlotto
package.domain = com.kwin.lotto
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs =.buildozer, bin,.github, venv,.git
source.exclude_exts = spec, md, txt
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
icon.filename = icon.png

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools = 33.0.2
android.ndk = 25b
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2
