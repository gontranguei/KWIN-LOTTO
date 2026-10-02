[app]
title = KWIN LOTTO
package.name = kwinlotto
package.domain = com.kwin.lotto
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools = 33.0.2
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.arch = armeabi-v7a
p4a.bootstrap = sdl2
