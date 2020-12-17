import tkinter as tk

root = tk.Tk()
root.geometry('600x600')
root.title('ARI - Mad Libs Generator')
main_header = tk.Label(root, text= 'Mad Libs Generator', font= 'Courier 20 bold').pack()
directions_one = tk.Label(root, text= 'Click Any Button', font= 'Courier 14 bold',).place(x=40, y=80)

proper_noun_var = tk.StringVar()
common_noun1_var = tk.StringVar()
common_noun2_var = tk.StringVar()
verb1_var = tk.StringVar()
verb2_var = tk.StringVar()
adjective1_var = tk.StringVar()
adjective2_var = tk.StringVar()
adverb1_var = tk.StringVar()
adverb2_var = tk.StringVar()

def mad_lib1():

    proper_noun = tk.StringVar()
    # input('enter a proper noun: ')
    common_noun1 = tk.StringVar()
    # input('enter a common noun: ')
    common_noun2 = tk.StringVar()
    # input('enter a common noun: ')
    verb1 = tk.StringVar()
    # input('enter a verb: ')
    verb2 = tk.StringVar()
    # input('enter a verb: ')
    adjective1 = tk.StringVar()
    # input('enter an adjective: ')
    adjective2 = tk.StringVar()
    # input('enter an adjective: ')
    adverb1= tk.StringVar()
    # input('enter an adverb: ')
    adverb2 = tk.StringVar()
    # input('enter an adverb: ')

    msg = f'Once upon a time, there was a kid named {proper_noun}. \n {proper_noun} had a/an {adjective1} {common_noun1} that they used to {adverb1} {verb1} the {common_noun2}. \n It was a real challenge, but {proper_noun} managed to {adverb2} {verb2}.'

    print(msg)

mad_lib1_button = tk.Button(root, text= 'Story Time', font= 'Courier 14', command= mad_lib1, bg= 'green')
mad_lib1_button.place(x=60, y=120)

directions_two = tk.Label(root, text='Follow the instructions:', font= 'Courier 20 bold')
directions_two.place(x=80, y=180)

proper_noun_input = tk.Entry(root, textvariable= ,)

root.mainloop()