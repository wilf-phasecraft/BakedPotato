import tkinter as tk
import random
from PIL import Image, ImageTk  # pip install pillow

class PotatoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Potato Baker")
        self.resizable(False, False)

        # Load images
        self.raw_img = ImageTk.PhotoImage(Image.open("raw_potato.png").resize((256, 256), Image.NEAREST))
        self.baked_img = ImageTk.PhotoImage(Image.open("baked_potato.png").resize((256, 256), Image.NEAREST))

        # Canvas
        self.canvas = tk.Canvas(self, width=256, height=256, bg="#cfe8ff", highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=3)

        # Image holder
        self.image_id = self.canvas.create_image(128, 128, image=self.raw_img)

        # Status label
        self.status = tk.Label(self, text="Uncooked potato…", anchor="w")
        self.status.grid(row=1, column=0, sticky="w", padx=8, pady=(6, 10))

        # Reset button
        self.reset_btn = tk.Button(self, text="Reset", command=self.reset)
        self.reset_btn.grid(row=1, column=2, sticky="e", padx=8, pady=(6, 10))

        # State
        self.state = "raw"
        self.bake_after_id = None
        self.schedule_bake()

    def schedule_bake(self):
        ms = random.randint(1500, 5000)
        if self.bake_after_id:
            self.after_cancel(self.bake_after_id)
        self.bake_after_id = self.after(ms, self.turn_baked)

    def reset(self):
        self.state = "raw"
        self.canvas.itemconfig(self.image_id, image=self.raw_img)
        self.status.config(text="Uncooked potato…")
        self.schedule_bake()

    def turn_baked(self):
        if self.state != "raw":
            return
        self.canvas.itemconfig(self.image_id, image=self.baked_img)
        self.status.config(text="Baked potato! 🥔✨")
        self.state = "baked"

if __name__ == "__main__":
    app = PotatoApp()
    app.mainloop()
