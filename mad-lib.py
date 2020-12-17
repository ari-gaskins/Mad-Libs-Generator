import tkinter as tk

# creates Tk object
root = tk.Tk()
# sets size of window
root.geometry('300x300')
# title of window
root.title('ARI - Mad Libs Generator')
# the main header label
main_header = tk.Label(root, text= 'Mad Libs Generator', font= 'Courier 20 bold').pack()
# instructions label
directions_one = tk.Label(root, text= 'Click Any Button', font= 'Courier 14 bold',).place(x=40, y=80)

# instantiates variables as Strings under tkinter
proper_noun_var = tk.StringVar()
common_noun1_var = tk.StringVar()
common_noun2_var = tk.StringVar()
verb1_var = tk.StringVar()
verb2_var = tk.StringVar()
adjective1_var = tk.StringVar()
adjective2_var = tk.StringVar()
adverb1_var = tk.StringVar()
adverb2_var = tk.StringVar()
msg_var = tk.StringVar()

def mad_lib1(window):

    # gets values returned as string
    proper_noun = proper_noun_var.get()
    common_noun1 = common_noun1_var.get()
    common_noun2 = common_noun2_var.get()
    verb1 = verb1_var.get()
    verb2 = verb2_var.get()
    adjective1 = adjective1_var.get()
    adjective2 = adjective2_var.get()
    adverb1= adverb1_var.get()
    adverb2 = adverb2_var.get()
    

    # sets the values that were created to be strings
    proper_noun_var.set('')
    common_noun1_var.set('')
    common_noun2_var.set('')
    verb1_var.set('')
    verb2_var.set('')
    adjective1_var.set('')
    adjective2_var.set('')
    adverb1_var.set('')
    adverb2_var.set('')

    # labels before the entry to tell user what to type
    proper_noun_label = tk.Label(window, text= 'enter a proper noun: ', font= 'Courier 16 bold')
    proper_noun_label.place(x=75, y=180)
    common_noun1_label = tk.Label(window, text= 'enter a common noun: ', font= 'Courier 16 bold')
    common_noun1_label.place(x=75, y=220)
    common_noun2_label = tk.Label(window, text= 'enter a common noun: ', font= 'Courier 16 bold')
    common_noun2_label.place(x=75, y=260)
    verb1_label = tk.Label(window, text= 'enter a verb: ', font= 'Courier 16 bold')
    verb1_label.place(x=75, y=300)
    verb2_label = tk.Label(window, text= 'enter a verb: ', font= 'Courier 16 bold')
    verb2_label.place(x=75, y=340)
    adjective1_label = tk.Label(window, text= 'enter an adjective: ', font= 'Courier 16 bold')
    adjective1_label.place(x=75, y=380)
    adjective2_label = tk.Label(window, text= 'enter an adjective: ', font= 'Courier 16 bold')
    adjective2_label.place(x=75, y=420)
    adverb1_label = tk.Label(window, text= 'enter an adverb: ', font= 'Courier 16 bold')
    adverb1_label.place(x=75, y=460)
    adverb2_label = tk.Label(window, text= 'enter an adverb: ', font= 'Courier 16 bold')
    adverb2_label.place(x=75, y=500)

    # space made available for user input
    proper_noun_input = tk.Entry(window, textvariable= proper_noun_var, font= 'Courier 14 normal')
    proper_noun_input.place(x=375, y=180)
    common_noun1_input = tk.Entry(window, textvariable= common_noun1_var, font= 'Courier 14 normal')
    common_noun1_input.place(x=375, y=220)
    common_noun2_input = tk.Entry(window, textvariable= common_noun2_var, font= 'Courier 14 normal')
    common_noun2_input.place(x=375, y=260)
    verb1_input = tk.Entry(window, textvariable= verb1_var, font= 'Courier 14 normal')
    verb1_input.place(x=375, y=300)
    verb2_input = tk.Entry(window, textvariable= verb2_var, font= 'Courier 14 normal')
    verb2_input.place(x=375, y=340)
    adjective1_input = tk.Entry(window, textvariable= adjective1_var, font= 'Courier 14 normal')
    adjective1_input.place(x=375, y=380)
    adjective2_input = tk.Entry(window, textvariable= adjective2_var, font= 'Courier 14 normal')
    adjective2_input.place(x=375, y=420)
    adverb1_input = tk.Entry(window, textvariable= adverb1_var, font= 'Courier 14 normal')
    adverb1_input.place(x=375, y=460)
    adverb2_input = tk.Entry(window, textvariable= adverb2_var, font= 'Courier 14 normal')
    adverb2_input.place(x=375, y=500)

    # submit_btn = tk.Button(window, text= 'Submit', font= 'Courier 14 bold')

    # msg_var.set(f'Once upon a time, there was a kid named {proper_noun}. \n {proper_noun} had a/an {adjective1} {common_noun1} that they used to {adverb1} {verb1} the {common_noun2}. \n It was a real challenge, but {proper_noun} managed to {adverb2} {verb2}.')

    # print(msg_var)

def open_mad_lib1():

    # Toplevel object treated as new window
    mad_lib1_window = tk.Toplevel(root)

    mad_lib1_window.title('Story Time')
    mad_lib1_window.geometry('700x700')

    directions_two = tk.Label(mad_lib1_window, text='Follow the instructions:', font= 'Courier 20 bold')
    directions_two.place(x=60, y=120)

    mad_lib1(mad_lib1_window)


mad_lib1_btn = tk.Button(root, text= 'Story Time', font= 'Courier 14 bold', command= open_mad_lib1, bg= 'green')
mad_lib1_btn.place(x=60, y=120)



root.mainloop()