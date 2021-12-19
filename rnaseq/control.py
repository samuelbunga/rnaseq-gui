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
    # get input path to fastq files
    frame.input_path = frame.set_buttons(text='Fastq files',
                                         cmd=frame.select_button,
                                         font='Ariel',
                                         row=1, col=1, sticky='W')
    # get output directory
    frame.output_path = frame.set_buttons(text='Output dir',
                                          cmd=frame.select_button,
                                          font='Ariel',
                                          row=1, col=2, sticky='W')

    frame.run_frame()

