from tkinter import *
import reddit_mod as rm


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
##
sort_label = Label(window, text='sort by[relevance, top, hot, new (default = relevance)] ')
sort_label.grid(row=2, column=0, sticky=NSEW)

sort_box = Entry(window, width=20, justify=['center'])
sort_box.grid(row=2, column=1, sticky=NSEW, padx=35, pady= 10)
 
##
time_label = Label(window, text='in last(hour, day, week, month, year, all[all max is 5 yr])')
time_label.grid(row=3, column=0, sticky=NSEW, padx=35, pady= 10)


timeframe_box = Entry(window, width=20, justify=['center'])
timeframe_box.grid(row=3, column=1, sticky=NSEW, padx=35, pady= 10)

##
result_label = Label(window, text='result limit?(default/max=100)')
result_label.grid(row=4, column=0, sticky=NSEW, padx=35, pady= 10)

result_limit_box = Entry(window, width=20, justify=['center'])
result_limit_box.grid(row=4, column=1, sticky=NSEW, padx=35, pady= 10)

##
btn = Button(window, 
            text='Run Search:',
            command=lambda: rm.main(subred_box.get(), keyword_box.get(), sort_box.get(), timeframe_box.get(), result_limit_box.get()),
            relief=RAISED)
    
btn.grid(row=5, columnspan=2, sticky=NSEW, padx=35, pady= 20)




window.mainloop()
