import re
import os
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog


class set_gui:
    def __init__(self):
        # initialize interface
        self.root = tk.Tk()
        self.root.title('rnaseq')
        self.root.resizable(width=False, height=False)
        self.bg_color = '#d8d8d8'
        self.btn_width = 12
        self.x_padding = (10, 5)
        self.fonts = font.Font(root=self.root, family='Arial', size=14, weight='bold')
        # Initiate the main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color,
                                   padx=10, pady=10)

    def set_buttons(self, text, cmd, font,
                    row, col, sticky):
        btn = tk.Button(self.main_frame,
                        text=text,
                        command=cmd,
                        highlightbackground=self.bg_color,
                        font=font,
                        width=self.btn_width)
        btn.grid(row=row, column=col, sticky=sticky)
        return btn

    def select_button(self):
        select_folder = filedialog.askdirectory(initialdir='.')
        return select_folder

    def run_frame(self):
        # pack main frame
        self.main_frame.pack(fill='both')
        self.root.update()
        self.root.mainloop()
