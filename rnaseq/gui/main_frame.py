import re
import os
import sys
import time
import tkinter as tk
from tkinter import font
from tkinter import Label
from tkinter import StringVar
from tkinter import OptionMenu
from tkinter import messagebox
from tkinter.ttk import Style
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter.ttk import Progressbar
from pre_process import *


class set_gui:
    def __init__(self):
        # initialize interface
        self.root = tk.Tk()
        self.root.title('rnaseq-gui')
        self.root.resizable(width=False, height=False)
        self.root.geometry('550x505')  # width x height
        self.bg_color = '#d8d8d8'
        self.btn_width = 12
        self.x_padding = (25, 0)
        self.y_padding = (5, 10)
        self.fonts = font.Font(root=self.root, family='Ariel', size=14, weight='bold')
        self.progress = ''
        self.button = ''
        self.img = ''
        self.all_buttons = {}
        self.all_labels = {}
        self.opts = {}
        self.all_inputs = {}
        self.chk_btn = tk.IntVar()
        # Initiate the main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color,
                                   padx=1, pady=10)

    def set_img(self):
        img_file = os.path.join(os.path.realpath(os.path.dirname(__file__)), os.path.pardir, os.path.pardir,
                                'img', 'dna.png')

        img = Image.open(img_file)
        img = img.resize((50, 50), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        Label(self.main_frame, image=self.img).grid(row=1, column=10, columnspan=1, sticky='E')

    def set_progress_bar(self, row, col, sticky):
        s = Style()
        s.theme_use('clam')
        s.configure("neon.Horizontal.TProgressbar", foreground='#39FF14', background='#39FF14')
        self.progress = Progressbar(self.main_frame,
                                    style="neon.Horizontal.TProgressbar",
                                    orient='horizontal',
                                    length=540,
                                    maximum=100,
                                    cursor='coffee_mug',
                                    mode='determinate',
                                    )
        self.progress.grid(row=row, column=col, columnspan=10, sticky=sticky, pady=(15, 0))
        self.progress['value'] = 2
        self.root.update_idletasks()

    def progress_bar(self, val):
        self.progress['value'] = val
        self.root.update()

    def set_buttons(self, text, button, cmd,
                    font, row, col, sticky, labels):
        if button not in self.all_buttons:
            self.all_buttons[button] = ''

        self.button = button
        self._initiate_label(labels)
        btn = tk.Button(self.main_frame,
                        text=text,
                        command=lambda onclick=text: cmd(onclick),
                        highlightbackground=self.bg_color,
                        font=font,
                        width=self.btn_width)
        btn.grid(row=row, column=col, sticky=sticky)

    def set_options(self, type, options, row, col, sticky):
        label = Label(self.main_frame, text=type,
                      bg=self.bg_color, font=self.fonts)
        label.grid(row=row, column=col, columnspan=1, sticky=sticky)
        if type not in self.opts:
            self.opts[type] = tk.StringVar(self.main_frame)
            self.opts[type].set(options[0])

        opt = OptionMenu(self.main_frame, self.opts[type], *options)
        opt.grid(row=row + 1, column=col, sticky='EW', padx=self.x_padding,
                 pady=self.y_padding)

    def select_button(self, onclick):
        select_folder = filedialog.askdirectory(initialdir='.')
        rel_mapping = {'Fastq files': 'input',
                       'Output dir': 'output',
                       'Select GTF': 'gtf',
                       'Exit': 'quit'}

        self.button = rel_mapping[onclick]
        if self.button in self.all_buttons:
            self.all_buttons[self.button] = os.path.realpath(select_folder)
            self.all_labels[self.button][0].set(select_folder[0:35] + '...')

    def check_button(self, row, col, sticky):
        label = Label(self.main_frame, text='Resume analysis',
                      bg=self.bg_color, font=self.fonts)
        label.grid(row=row, column=col, columnspan=1, sticky=sticky)
        c1 = tk.Checkbutton(self.main_frame, text='Yes', onvalue=0, offvalue=1,
                            variable=self.chk_btn)
        c2 = tk.Checkbutton(self.main_frame, text='No', onvalue=1, offvalue=0,
                            variable=self.chk_btn)

        c1.grid(row=row + 1, column=col, sticky='W')
        c2.grid(row=row + 1, column=col, sticky='W', padx=(55))

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
                           columnspan=1,
                           sticky=labels_dict['sticky'],
                           )
            self.all_labels[self.button] = (label, label_obj)

    def start(self, labels):
        self.all_buttons['start'] = 1
        self.all_inputs['library_type'] = 'PE' if self.opts['Library type'].get() == 'Paired-end' else 'SE'
        self.all_inputs['aligner'] = self.opts['Aligner to use'].get()
        self.all_inputs.update(self.all_buttons)
        self.all_inputs['resume'] = str(self.chk_btn.get())
        self.all_inputs['strand'] = self.opts['Strand specificity'].get()
        self.all_inputs['Adapter'] = self.opts['Adapter'].get()

        self.all_inputs['input'] = '/Users/sbunga/gitHub/rnaSeq/rnaseq/test/data/'
        self.all_inputs['output'] = '/Users/sbunga/gitHub/rnaSeq/rnaseq/test'

        # check for inputfiles
        if check_dir([self.all_inputs['input']]):
            self.progress_bar(5)
        else:
            messagebox.showerror("Error", "Input directory doesn't exist, Please try again.")

        if check_dir([self.all_inputs['output']]):
            self.progress_bar(15)
        else:
            messagebox.showerror("Error", "Output directory doesn't exist, Please try again.")

        # run fastqc
        run_fastqc(self.all_inputs)
        self.progress_bar(30)
        time.sleep(1)

        # run multiqc
        run_multiqc(self.all_inputs)
        self.progress_bar(35)
        time.sleep(1)
        
        # run trimmomatic
        trim_reads(self.all_inputs)
        self.progress_bar(60)
        time.sleep(1)

        # run alignment

    def quit(self, labels):
        self.all_buttons['quit'] = 1
        self.root.quit()

    def run_frame(self):
        # pack main frame
        self.main_frame.pack(fill='both')
        self.root.update()
        self.root.mainloop()
