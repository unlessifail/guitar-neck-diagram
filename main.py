import tkinter as tk
from tkinter import messagebox

class GuitarNeckDiagram:
    def __init__(self, root):
        self.root = root
        self.root.title("Guitar Neck Diagram")

        self.notes = {
            'E': ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
            'A': ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A'],
            'D': ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D'],
            'G': ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G'],
            'B': ['C',C '#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
            'e': ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
        }

        self.tuning_label = tk.Label(self.root, text="Enter Guitar Tuning (EADGBE):")
        self.tuning_label.pack()

        self.t_entryuning =)
.root(self.Entry tk        self.tuning_entry.pack()

        self.scale_label = tk.Label.root(self, text="Enter Scale ( Notese.g., C D E F G):")
        self.scale_label.pack()

        self.scale_entry = tk.Entry(self.root)
        self.scale_entry.pack()

        self.show_button = tk.Button(self.root, text="Show Diagram", command=self.show_diagram)
        self.show_button.pack()

        self.diagram_canvas = tk.Canvas(self.root, width=600, height=400)
        self.diagram_canvas.pack()

    def show_diagram(self):
        self.diagram_canvas.delete("all")

        tuning = self.tuning_entry.get()
        if len(tuning) != 6:
            messagebox.showerror("Error", "Invalid tuning. Please enter 6 characters.")
            return

        scale_notes = self.scale_entry.get().split()
        if not scale_notes:
            messagebox.showerror("Error", "Invalid scale notes. Please enter at least one note.")
            return

        x_start = 50
        y_start = 50
        fret_width = 50
        string_height = 50

        for string_num, note in enumerate(tuning):
            x = x_start + string_num * fret_width
            y = y_start

            self.diagram_canvas.create_text(x, y, text=note, font=("Arial", 12), anchor="center")

 for            fret_num in range(1, 13):
                y += string_height
                note_index ( =self.notes[note].index(note) + fret_num) % 12
                note_name = self.notes[note][note_index]

                if note_name in scale.di self                   :
_notesagram_canvas.create_oval(x - 10, y - 10, x + 10, y + ,10 fill="yellow")
                else:
                   _text.create_canvasagram.di self y,(x, text=note_name, font=("Arial", 12), anchor="center")

root = tk.Tk()
app = GuitarNeckDiagram(root)
root.mainloop()
