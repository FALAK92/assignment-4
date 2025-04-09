#Implement an 'eraser' on a canvas.

#The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen.
#We then create an eraser rectangle which, when dragged around the canvas,
# sets all of the rectangles it is in contact with to white.

import tkinter as tk

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.create_grid()
        self.eraser = None

        self.canvas.bind("<B1-Motion>", self.erase)

        # Bind Escape key to close the window
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    def create_grid(self):
        for row in range(0, 400, 40):
            for col in range(0, 400, 40):
                self.canvas.create_rectangle(col, row, col + 40, row + 40, fill="blue", tags="cell")

    def erase(self, event):
        overlapping_items = self.canvas.find_overlapping(event.x, event.y, event.x + 20, event.y + 20)
        for item in overlapping_items:
            self.canvas.itemconfig(item, fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()
