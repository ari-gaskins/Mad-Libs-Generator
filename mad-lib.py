import tkinter as tk

# creates master Tk object
master = tk.Tk()
# sets size of mad_lib1_window
master.geometry('300x300')
# title of mad_lib1_window
master.title('ARI - Mad Libs Generator')
# the main header label
main_header = tk.Label(master, text= 'Mad Libs Generator', font= 'Courier 20 bold')
main_header.pack()
# instructions label
directions_one = tk.Label(master, text= 'Click Any Button', font= 'Courier 14 bold',)
directions_one.place(x=40, y=80)

# instantiates variables as Strings under tkinter
ml1_proper_noun_var = tk.StringVar()
ml1_common_noun1_var = tk.StringVar()
ml1_common_noun2_var = tk.StringVar()
ml1_verb1_var = tk.StringVar()
ml1_verb2_var = tk.StringVar()
ml1_adjective1_var = tk.StringVar()
ml1_adjective2_var = tk.StringVar()
ml1_adverb1_var = tk.StringVar()
ml1_adverb2_var = tk.StringVar()
ml1_msg_var = tk.StringVar()


def open_mad_lib1():
    
    # creates mad_lib1_window Toplevel object
    mad_lib1_window = tk.Toplevel(master)
    # sets size of mad_lib1_window
    mad_lib1_window.geometry('700x700')
    # title of mad_lib1_window
    mad_lib1_window.title('Story Time')
    # header label
    directions_two = tk.Label(mad_lib1_window, text='Follow the instructions:', font= 'Courier 20 bold')
    directions_two.place(x=60, y=120)
    
    # gets values returned as string
    proper_noun = ml1_proper_noun_var.get()
    common_noun1 = ml1_common_noun1_var.get()
    common_noun2 = ml1_common_noun2_var.get()
    verb1 = ml1_verb1_var.get()
    verb2 = ml1_verb2_var.get()
    adjective1 = ml1_adjective1_var.get()
    adjective2 = ml1_adjective2_var.get()
    adverb1= ml1_adverb1_var.get()
    adverb2 = ml1_adverb2_var.get()
    
    # sets the values that were created to be strings
    ml1_proper_noun_var.set('')
    ml1_common_noun1_var.set('')
    ml1_common_noun2_var.set('')
    ml1_verb1_var.set('')
    ml1_verb2_var.set('')
    ml1_adjective1_var.set('')
    ml1_adjective2_var.set('')
    ml1_adverb1_var.set('')
    ml1_adverb2_var.set('')

    # labels before the entry to tell user what to type
    proper_noun_lbl = tk.Label(mad_lib1_window, text= 'enter a proper noun: ', font= 'Courier 16 bold')
    proper_noun_lbl.place(x=75, y=180)
    common_noun1_lbl = tk.Label(mad_lib1_window, text= 'enter a common noun: ', font= 'Courier 16 bold')
    common_noun1_lbl.place(x=75, y=220)
    common_noun2_lbl = tk.Label(mad_lib1_window, text= 'enter a common noun: ', font= 'Courier 16 bold')
    common_noun2_lbl.place(x=75, y=260)
    verb1_lbl = tk.Label(mad_lib1_window, text= 'enter a verb: ', font= 'Courier 16 bold')
    verb1_lbl.place(x=75, y=300)
    verb2_lbl = tk.Label(mad_lib1_window, text= 'enter a verb: ', font= 'Courier 16 bold')
    verb2_lbl.place(x=75, y=340)
    adjective1_lbl = tk.Label(mad_lib1_window, text= 'enter an adjective: ', font= 'Courier 16 bold')
    adjective1_lbl.place(x=75, y=380)
    adjective2_lbl = tk.Label(mad_lib1_window, text= 'enter an adjective: ', font= 'Courier 16 bold')
    adjective2_lbl.place(x=75, y=420)
    adverb1_lbl = tk.Label(mad_lib1_window, text= 'enter an adverb: ', font= 'Courier 16 bold')
    adverb1_lbl.place(x=75, y=460)
    adverb2_lbl = tk.Label(mad_lib1_window, text= 'enter an adverb: ', font= 'Courier 16 bold')
    adverb2_lbl.place(x=75, y=500)

    # space made available for user input
    proper_noun_ent = tk.Entry(mad_lib1_window, textvariable= ml1_proper_noun_var, font= 'Courier 14 normal')
    proper_noun_ent.place(x=375, y=180)
    common_noun1_ent = tk.Entry(mad_lib1_window, textvariable= ml1_common_noun1_var, font= 'Courier 14 normal')
    common_noun1_ent.place(x=375, y=220)
    common_noun2_ent = tk.Entry(mad_lib1_window, textvariable= ml1_common_noun2_var, font= 'Courier 14 normal')
    common_noun2_ent.place(x=375, y=260)
    verb1_ent = tk.Entry(mad_lib1_window, textvariable= ml1_verb1_var, font= 'Courier 14 normal')
    verb1_ent.place(x=375, y=300)
    verb2_ent = tk.Entry(mad_lib1_window, textvariable= ml1_verb2_var, font= 'Courier 14 normal')
    verb2_ent.place(x=375, y=340)
    adjective1_ent = tk.Entry(mad_lib1_window, textvariable= ml1_adjective1_var, font= 'Courier 14 normal')
    adjective1_ent.place(x=375, y=380)
    adjective2_ent = tk.Entry(mad_lib1_window, textvariable= ml1_adjective2_var, font= 'Courier 14 normal')
    adjective2_ent.place(x=375, y=420)
    adverb1_ent = tk.Entry(mad_lib1_window, textvariable= ml1_adverb1_var, font= 'Courier 14 normal')
    adverb1_ent.place(x=375, y=460)
    adverb2_ent = tk.Entry(mad_lib1_window, textvariable= ml1_adverb2_var, font= 'Courier 14 normal')
    adverb2_ent.place(x=375, y=500)
    
    def open_mad_lib1_final():
        
        # creates final mad_lib1_window for mad_lib1
        mad_lib1_window_FINAL = tk.Toplevel(mad_lib1_window)
        # sets size of mad_lib1_window
        mad_lib1_window_FINAL.geometry('300x300')
        # sets title of mad_lib1_window
        mad_lib1_window_FINAL.title('Story Time ENDING')
        # quit button
        quit_button = tk.Button(mad_lib1_window_FINAL, text= 'QUIT', font= 'Courier 20 bold',relief= tk.RAISED, command= mad_lib1_window.quit, bg= 'red')

    # submit button to open mad_lib1_window
    submit_btn = tk.Button(mad_lib1_window, text= 'Submit', font= 'Courier 14 bold', relief= tk.RAISED, command= open_mad_lib1_final, bg= 'green')
    submit_btn.place(x=300, y=550)

    
# mad-lib1 'Story Time'
mad_lib1_btn = tk.Button(master, text= 'Story Time', font= 'Courier 14 bold', relief= tk.RAISED, command= open_mad_lib1, bg= 'dark violet')
mad_lib1_btn.place(x=60, y=120)

# def msg_mad_lib1(mad_lib1_window, pn, cn1, cn2, v1, v2, adj1, adj2, adv1, adv2):

   # msg1 = f'Once upon a time, there was a kid named {pn}.\n'
   # msg2 = f'{pn} had a/an {adj1} {cn1} that they used to {adv1} {v1} the {cn2}.\n'
   # msg3 = f'It was a real challenge, but {pn} managed to {adv2} {v2}.\n'


master.mainloop()