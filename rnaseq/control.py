import re
import os
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from gui.main_frame import set_gui

if __name__ == "__main__":
    # initiate gui
    frame = set_gui()

    # set input path to fastq files
    frame.set_buttons(text='Fastq files',
                      button='input',
                      cmd=frame.select_button,
                      font='Ariel',
                      row=1, col=1, sticky='W',
                      labels={'button': 'input', 'row': 1, 'col': 2, 'sticky': 'W'})

    # set output directory
    frame.set_buttons(text='Output dir',
                      button='output',
                      cmd=frame.select_button,
                      font='Ariel',
                      row=2, col=1, sticky='W',
                      labels={'button': 'output', 'row': 2, 'col': 2, 'sticky': 'W'})

    # set library types
    frame.set_options(type='Library type',
                      options=['Paired-end', 'Single-end'],
                      row=3, col=1, sticky='W')

    # set aligner
    frame.set_options(type='Aligner to use',
                      options=['STAR', 'salmon'],
                      row=5, col=1, sticky='W')

    # start pipeline
    frame.set_buttons(text='Start analysis',
                      button='start',
                      cmd=frame.start,
                      font='Ariel',
                      row=8, col=1, sticky='W',
                      labels={'button': 'start', 'row': 8, 'col': 2, 'sticky': 'E'})

    # exit
    frame.set_buttons(text='Exit',
                      button='quit',
                      cmd=frame.quit,
                      font='Ariel',
                      row=8, col=2, sticky='W',
                      labels={'button': 'quit', 'row': 9, 'col': 2, 'sticky': 'E'})
    frame.run_frame()
