from gui.main_frame import set_gui


#if __name__ == "__main__":
# initiate gui
global frame
frame = set_gui()
frame.set_img()

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
                  row=4, col=1, sticky='W')

# set aligner
frame.set_options(type='Aligner to use',
                  options=['STAR', 'salmon'],
                  row=6, col=1, sticky='W')

# set gtf location
frame.set_buttons(text='Select GTF',
                  button='gtf',
                  cmd=frame.select_button,
                  font='Ariel',
                  row=8, col=1, sticky='W',
                  labels={'button': 'gtf', 'row': 7, 'col': 2, 'sticky': 'W'})

# set strand specificity
frame.set_options(type='Strand specificity',
                  options=['Un-stranded', 'Stranded', 'Reversely stranded'],
                  row=10, col=1, sticky='W')

# Select adapter
frame.set_options(type='Adapter',
                  options=['TruSeq3', 'TruSeq2'],
                  row=12, col=1, sticky='W')

# set resume option
frame.check_button(row=14, col=1, sticky='W')

# start pipeline
frame.set_buttons(text='Start analysis',
                  button='start',
                  cmd=frame.start,
                  font='Ariel',
                  row=25, col=1, sticky='W',
                  labels={'button': 'start', 'row': 8, 'col': 2, 'sticky': 'E'})

# exit
frame.set_buttons(text='Exit',
                  button='quit',
                  cmd=frame.quit,
                  font='Ariel',
                  row=25, col=2, sticky='W',
                  labels={'button': 'quit', 'row': 9, 'col': 2, 'sticky': 'E'})
frame.set_progress_bar(row=30, col=1, sticky='W')
frame.run_frame()
