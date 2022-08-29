from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from pygame import midi
import threading

midi.init()

reg_classes = []

def register(instance):
    reg_classes.append(instance)

class NoteEvent:
    def __init__(self, note, note_number, note_press):
        self.note = note
        self.note_number = note_number
        self.note_press = note_press

def get_piano_index(piano_name):
    for i in range(midi.get_count()):
        device_info = midi.get_device_info(i)
        device_name = device_info[1].decode("utf-8")
        device_input = device_info[2]

        if device_name == piano_name:
            if device_input == 1:
                return i

def get_piano_input(piano_input):
    while True:
        if piano_input.poll():
            event = piano_input.read(1)[0]
            note_press_type = event[0][0]
            note_press = "down"
            if note_press_type == 128:
                note_press = "up"
            note_number = event[0][1]
            note = midi.midi_to_ansi_note(note_number)

            for instance in reg_classes:
                for method_name in dir(instance):
                    needed_method_name = "on" + note.replace("#", "S")
                    if method_name == needed_method_name:
                        note_event = NoteEvent(note, note_number, note_press)
                        eval("instance." + method_name + "(note_event)")
                    elif ''.join([i for i in needed_method_name if not i.isdigit()]) == method_name:
                        note_event = NoteEvent(note, note_number, note_press)
                        eval("instance." + method_name + "(note_event)")

piano_index = get_piano_index("Digital Piano")
piano_input = midi.Input(piano_index)
input_thread = threading.Thread(target=get_piano_input, args=(piano_input,))
input_thread.start()
            
