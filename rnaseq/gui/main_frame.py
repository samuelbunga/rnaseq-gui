import re
import os
import tkinter as tk
from tkinter import font
from tkinter import Label
from tkinter import StringVar
from tkinter import messagebox
from tkinter import filedialog


class set_gui:
    def __init__(self):
        # initialize interface
        self.root = tk.Tk()
        self.root.title('rnaseq')
        self.root.resizable(width=False, height=False)
        self.root.geometry('550x550')  # width x height
        self.bg_color = '#d8d8d8'
        self.btn_width = 12
        self.x_padding = (10, 5)
        self.fonts = font.Font(root=self.root, family='Arial', size=14, weight='bold')
        self.button = ''
        self.all_buttons = {}
        self.all_labels = {}
        # Initiate the main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color,
                                   padx=10, pady=10)

    def set_buttons(self, text, button, cmd,
                    font, row, col, sticky, labels):
        if button not in self.all_buttons:
            self.all_buttons[button] = ('', '')

        self.button = button
        self._initiate_label(labels)
        print(self.all_labels)
        btn = tk.Button(self.main_frame,
                        text=text,
                        command=lambda onclick=text: cmd(onclick),
                        highlightbackground=self.bg_color,
                        font=font,
                        width=self.btn_width)
        btn.grid(row=row, column=col, sticky=sticky)

    def select_button(self, onclick):
        select_folder = filedialog.askdirectory(initialdir='.')
        rel_mapping = {'Fastq files': 'input',
                       'Output dir': 'output',
                       'Exit': 'quit'}

        self.button = rel_mapping[onclick]
        if self.button in self.all_buttons:
            self.all_buttons[self.button] = os.path.realpath(select_folder)
            self.all_labels[self.button][0].set(select_folder)

    def _initiate_label(self, labels_dict):
        if self.button not in self.all_labels:
            label = StringVar()
            label.set('')
            label_obj = Label(self.main_frame,
                              textvariable=label,
                              bg=self.bg_color,
                              font=self.fonts)

            label_obj.grid(row=labels_dict['row'],
                           column=labels_dict['col'],
                           columnspan=3,
                           sticky=labels_dict['sticky'],
                           padx=self.x_padding)
            self.all_labels[self.button] = (label, label_obj)

    def quit(self, labels):
        self.root.quit()

    def run_frame(self):
        # pack main frame
        self.main_frame.pack(fill='both')
        self.root.update()
        self.root.mainloop()
