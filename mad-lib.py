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
    proper_noun_var.set('enter a proper noun: ')
    common_noun1_var.set('enter a common noun: ')
    common_noun2_var.set('enter a common noun: ')
    verb1_var.set('enter a verb: ')
    verb2_var.set('enter a verb: ')
    adjective1_var.set('enter an adjective: ')
    adjective2_var.set('enter an adjective: ')
    adverb1_var.set('enter an adverb: ')
    adverb2_var.set('enter an adverb: ')


    proper_noun_input = tk.Entry(window, textvariable= proper_noun_var, font= 'Courier 14 normal')
    proper_noun_input.place(x=80, y=180)
    common_noun1_input = tk.Entry(window, textvariable= common_noun1_var, font= 'Courier 14 normal')
    common_noun1_input.place(x=100, y=200)
    common_noun2_input = tk.Entry(window, textvariable= common_noun2_var, font= 'Courier 14 normal')
    common_noun2_input.place(x=120, y=220)
    verb1_input = tk.Entry(window, textvariable= verb1_var, font= 'Courier 14 normal')
    verb1_input.place(x=140, y=240)
    verb2_input = tk.Entry(window, textvariable= verb2_var, font= 'Courier 14 normal')
    verb2_input.place(x=160, y=260)
    adjective1_input = tk.Entry(window, textvariable= adjective1_var, font= 'Courier 14 normal')
    adjective1_input.place(x=180, y=280)
    adjective2_input = tk.Entry(window, textvariable= adjective2_var, font= 'Courier 14 normal')
    adjective2_input.place(x=200, y=300)
    adverb1_input = tk.Entry(window, textvariable= adverb1_var, font= 'Courier 14 normal')
    adverb1_input.place(x=220, y=320)
    adverb2_input = tk.Entry(window, textvariable= adverb2_var, font= 'Courier 14 normal')
    adverb2_input.place(x=240, y=340)

    # submit_btn = tk.Button(window, text= 'Submit', font= 'Courier 14 bold')

    # msg_var.set(f'Once upon a time, there was a kid named {proper_noun}. \n {proper_noun} had a/an {adjective1} {common_noun1} that they used to {adverb1} {verb1} the {common_noun2}. \n It was a real challenge, but {proper_noun} managed to {adverb2} {verb2}.')

    # print(msg_var)

def open_mad_lib1():

    # Toplevel object treated as new window
    mad_lib1_window = tk.Toplevel(root)

    mad_lib1_window.title('Story Time')
    mad_lib1_window.geometry('500x500')

    directions_two = tk.Label(mad_lib1_window, text='Follow the instructions:', font= 'Courier 20 bold')
    directions_two.place(x=60, y=120)

    mad_lib1(mad_lib1_window)


mad_lib1_btn = tk.Button(root, text= 'Story Time', font= 'Courier 14 bold', command= open_mad_lib1, bg= 'green')
mad_lib1_btn.place(x=60, y=120)



root.mainloop()