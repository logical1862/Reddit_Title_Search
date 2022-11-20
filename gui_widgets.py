#handles tkinter widget vaules to keep gui logic clean

from tkinter import *
from tkinter.ttk import Combobox
import reddit_mod 


class search_window():
    window = Tk()
    window.grid()

    # sort choices:
    sort_option_list = [
        'relevance',
        'top',
        'hot',
        'new'
    ]
    #  timeframe options
    timeframe_option_list = [
        'hour',
        'day',
        'week',
        'month',
        'year',
        'all'
    ]
    # limit results range
    range_list = list(range(100,1, -1))

    def __init__(self, title:str):
        self.window.title(title)
        
        #labels

        subred_label = Label(self.window, text='search what subreddits?(default = all)')
        subred_label.grid(row=0, column=0, sticky=NSEW, padx=35, pady= 10)

        keyword_label = Label(self.window, text='keyword?')
        keyword_label.grid(row=1, column=0, sticky=NSEW, padx=35, pady= 10)

        sort_label = Label(self.window, text='sort by[relevance, top, hot, new] ')
        sort_label.grid(row=2, column=0, sticky=NSEW)
        
        time_label = Label(self.window, text='in last(hour, day, week, month, year, all[all max is 5 yr])')
        time_label.grid(row=3, column=0, sticky=NSEW, padx=35, pady= 10)

        result_label = Label(self.window, text='result limit?(default/max=100)')
        result_label.grid(row=4, column=0, sticky=NSEW, padx=35, pady= 10)

        # entry boxes

        subreddit_entry_box = Entry(self.window, width=20, justify=['center'])
        subreddit_entry_box.grid(row=0, column=1, sticky=NSEW, padx=35, pady= 10)
        
        keyword_entry_box = Entry(self.window, width=20, justify=['center'])
        keyword_entry_box.grid(row=1, column=1, sticky=NSEW, padx=35, pady= 10)



        # result limit combobox
        result_limit_dropdown = Combobox(
            self.window,
            values=self.range_list,
            state='readonly',
            justify='center'
        )
        result_limit_dropdown.set(self.range_list[0])
        result_limit_dropdown.grid(row=4, column=1, sticky=NSEW,padx=35, pady= 10)


        # sort combobox
        sort_choice_dropdown = Combobox(
            self.window,
            values = self.sort_option_list,
            state='readonly',
            justify='center'
        )
        sort_choice_dropdown.set(self.sort_option_list[0])
        sort_choice_dropdown.grid(row=2, column=1, sticky=NSEW,padx=35, pady= 10 )


        # timeframe combobox
        timeframe_choice_dropdown = Combobox(
            self.window,
            values=self.timeframe_option_list,
            state='readonly',
            justify='center'
            )

        timeframe_choice_dropdown.grid(row=3, column=1, sticky=NSEW, padx=35, pady= 10)
        timeframe_choice_dropdown.set(self.timeframe_option_list[0])



        # run search button:
        btn = Button(self.window, 
                    text='Run Search:',
                    command=lambda: reddit_mod.main(subreddit_entry_box.get(), keyword_entry_box.get(), sort_choice_dropdown.get() , timeframe_choice_dropdown.get(), result_limit_dropdown.get()),
                    relief=RAISED)
            
        btn.grid(row=5, columnspan=2, sticky=NSEW, padx=35, pady= 20)



