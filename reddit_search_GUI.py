from msilib.schema import ComboBox
from secrets import choice
from tkinter import *
from tkinter.ttk import Combobox
import reddit_mod 


window = Tk()

window.title('reddit post keyword search')
window.grid()

# Specify Grid
Grid.rowconfigure(window,0,weight=1)
Grid.columnconfigure(window,0,weight=1)
 
Grid.rowconfigure(window,1,weight=1)

##
subred_label = Label(window, text='search what subreddits?(default = all)')
subred_label.grid(row=0, column=0, sticky=NSEW, padx=35, pady= 10)

subred_box = Entry(window, width=20, justify=['center'])
subred_box.grid(row=0, column=1, sticky=NSEW, padx=35, pady= 10)
##
keyword_label = Label(window, text='keyword?')
keyword_label.grid(row=1, column=0, sticky=NSEW, padx=35, pady= 10)

keyword_box = Entry(window, width=20, justify=['center'])
keyword_box.grid(row=1, column=1, sticky=NSEW, padx=35, pady= 10)

##user sort choice:

sort_option_list = [
    'relevance',
    'top',
    'hot',
    'new'
]

    #sort combobox
sort_input_variable = StringVar()
sort_input_variable.set(sort_option_list[0])

dropdown_sort = Combobox(
    window,
    values = sort_option_list,
    textvariable= sort_input_variable,
    state='readonly',
    justify='center'
    )



dropdown_sort.grid(row=2, column=1, sticky=NSEW,padx=35, pady= 10 )

    #sort text label
sort_label = Label(window, text='sort by[relevance, top, hot, new] ')
sort_label.grid(row=2, column=0, sticky=NSEW)

##user timeframe choice:
timeframe_option_list = [
    'hour',
    'day',
    'week',
    'month',
    'year',
    'all'
]

    #timeframe combobox
timeframe_input_variable = StringVar()
timeframe_input_variable.set(timeframe_option_list[0])

dropdown_timeframe = Combobox(
    window,
    values=timeframe_option_list,
    textvariable= timeframe_input_variable,
    state='readonly',
    justify='center'
    )

dropdown_timeframe.grid(row=3, column=1, sticky=NSEW, padx=35, pady= 10)

    #timeframe text label
time_label = Label(window, text='in last(hour, day, week, month, year, all[all max is 5 yr])')
time_label.grid(row=3, column=0, sticky=NSEW, padx=35, pady= 10)


##

result_label = Label(window, text='result limit?(default/max=100)')
result_label.grid(row=4, column=0, sticky=NSEW, padx=35, pady= 10)

result_limit_box = Entry(window, width=20, justify=['center'])
result_limit_box.grid(row=4, column=1, sticky=NSEW, padx=35, pady= 10)

##run search button:
btn = Button(window, 
            text='Run Search:',
            command=lambda: reddit_mod.main(subred_box.get(), keyword_box.get(), sort_input_variable.get() , timeframe_input_variable.get(), result_limit_box.get()),
            relief=RAISED)
    
btn.grid(row=5, columnspan=2, sticky=NSEW, padx=35, pady= 20)




window.mainloop()
