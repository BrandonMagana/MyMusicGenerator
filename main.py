import numpy as np
import sounddevice as sd
from typing import List
from utils.music_notes import NOTE_TRANSITIONS, NOTE_TO_FRECUENCY, INDEX_TO_NOTE


def generate_melody(start: int, iterations: int) -> List[int]:
    current_note = start
    result = []
    for _ in range(iterations):
        result.append(current_note)
        current_note = np.random.choice(
                len(NOTE_TRANSITIONS),
                p=NOTE_TRANSITIONS[current_note])
    return result


def play_tone(note, duration=0.5, sample_rate=45000, amplitude=0.5):
    frequency = NOTE_TO_FRECUENCY[note]
    note = INDEX_TO_NOTE[note]
    time = np.linspace(0, duration, int(sample_rate * duration), False)
    audio = amplitude * np.sin(2 * np.pi * frequency * time)
    print(note)
    sd.play(audio, sample_rate)
    sd.wait()


def main():
    n_transitions = int(input("# de transiciones: "))
    melody = generate_melody(0, n_transitions)
    for note in melody:
        play_tone(note)


if __name__ == '__main__':
    main()
