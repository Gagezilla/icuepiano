import piano, icue

devices = icue.Devices()

red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (46, 43, 95)
violet = (139, 0, 255)

class PianoKeys:
    def onA(event):
        if event.note_press == "down":
            devices.set_led_colors(red)
    def onB(event):
        if event.note_press == "down":
            devices.set_led_colors(orange)
    def onC(event):
        if event.note_press == "down":
            devices.set_led_colors(yellow)
    def onD(event):
        if event.note_press == "down":
            devices.set_led_colors(green)
    def onE(event):
        if event.note_press == "down":
            devices.set_led_colors(blue)
    def onF(event):
        if event.note_press == "down":
            devices.set_led_colors(indigo)
    def onG(event):
        if event.note_press == "down":
            devices.set_led_colors(violet)

piano.register(PianoKeys)

while True:
    pass
