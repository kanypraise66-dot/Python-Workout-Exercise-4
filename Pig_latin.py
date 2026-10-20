import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk, ImageSequence

VOWELS = "aeiou"


def pig_latin(word):
    if word[0] in VOWELS:
        return word + "way"
    for i, ch in enumerate(word):          # handle clusters like "string"
        if ch in VOWELS:
            return word[i:] + word[:i] + "ay"
    return word + "ay"                      # no vowels at all, e.g. "my"


def translate(event=None):
    word = entry.get().strip().lower()
    if not word.isalpha():
        result.config(text="Please enter one word (letters only)")
        return
    result.config(text=pig_latin(word))


def animate(i=0):
    gif_label.config(image=frames[i])
    root.after(delays[i], animate, (i + 1) % len(frames))


root = tk.Tk()
root.title("Pig Latin Translator")

# Load GIF frames (keep references so they aren't garbage collected)
gif = Image.open(Path(__file__).parent.parent /
                 "Memes" / "So Excited Flirting GIF.gif")
frames, delays = [], []
for f in ImageSequence.Iterator(gif):
    delays.append(max(f.info.get("duration", 100), 100))
    frames.append(ImageTk.PhotoImage(
        f.copy().convert("RGBA").resize((200, 200))))

gif_label = tk.Label(root)
gif_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack(padx=20)
entry.bind("<Return>", translate)

tk.Button(root, text="Translate!", command=translate).pack(pady=8)

result = tk.Label(root, text="", font=("Arial", 20, "bold"))
result.pack(pady=10)

animate()
root.mainloop()
