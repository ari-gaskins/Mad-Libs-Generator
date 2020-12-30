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

    # list of the variables/words
    w = [proper_noun, common_noun1, common_noun2, verb1, verb2, adjective1, adjective2, adverb1, adverb2]

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

    # submit button to open mad_lib1_final (conditional)
    submit_btn = tk.Button(mad_lib1_window, text= 'Submit', font= 'Courier 14 bold', relief= tk.RAISED, bg= 'green')
    submit_btn.place(x=300, y=550)

    def default_case():
        return tk.Label(mad_lib1_window, text= 'Forget Something?', font= 'Courier 16 bold').place(x=275, y=600)

    def check_for_words(w):
        
        # creates cases for the strings taken from the user
        user_cases = {
            0 : proper_noun,
            1 : common_noun1,
            2 : common_noun2,
            3 : verb1,
            4 : verb2,
            5 : adjective1,
            6 : adjective2,
            7 : adverb1,
            8 : adverb2
        }
        
        # iterates through the list
        for words in w:
            user_cases.get(words, default_case())
            if words is not default_case:
                submit_btn.config(command= open_mad_lib1_final)
            if words is default_case:
                break

    check_for_words(w)

    def msg_mad_lib1(mad_lib1_window, proper_noun, common_noun1, common_noun2, verb1, verb2, adjective1, adjective2, adverb1, adverb2):
        
        msg1 = f'Once upon a time, there was a kid named {proper_noun}.\n'
        msg2 = f'{proper_noun} had a/an {adjective1} {common_noun1} that they used to {adverb1} {verb1} the {adjective2}{common_noun2}.\n'
        msg3 = f'It was a real challenge, but {proper_noun} managed to {adverb2} {verb2}.\n'

        return (msg1 + msg2 + msg3)

    final_msg_txt = msg_mad_lib1(mad_lib1_window, proper_noun, common_noun1, common_noun2, verb1, verb2, adjective1, adjective2, adverb1, adverb2)

    def open_mad_lib1_final(final_msg_txt):
        
        # creates final mad_lib1_window for mad_lib1
        mad_lib1_window_FINAL = tk.Toplevel(mad_lib1_window)
        # sets size of mad_lib1_window
        mad_lib1_window_FINAL.geometry('500x300')
        # sets title of mad_lib1_window
        mad_lib1_window_FINAL.title('Story Time ENDING')
        # shows final message
        final_msg = tk.Text(mad_lib1_window_FINAL, font= 'Courier 14 normal').insert(final_msg_txt)
        # quit button
        quit_button = tk.Button(mad_lib1_window_FINAL, text= 'QUIT', font= 'Courier 20 bold', relief= tk.RAISED, command= mad_lib1_window.quit, bg= 'red')
    

# mad-lib1 'Story Time'
mad_lib1_btn = tk.Button(master, text= 'Story Time', font= 'Courier 14 bold', relief= tk.RAISED, command= open_mad_lib1, bg= 'dark violet')
mad_lib1_btn.place(x=60, y=120)




master.mainloop()