from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
Window.clearcolor = (0.1, 0.06, 0.25, 1)
class KwinLottoApp(App):
 def build(self):
  return Label(text="KWIN LOTTO\nCap sur la win", font_size='24sp')
KwinLottoApp().run()
