import sys
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

for filename in sys.argv[1:]:
    # load data and transpose so that country names are
    # the columns and their gdp data becomes the rows
    data = pandas.read_csv(filename, index_col = 'country').T

    # create a plot of the transposed data
    ax = data.plot(title = filename)

    # set some plot attributes
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP Per Capita")
    # set the x location and labels
    ax.set_xticks(range(len(data.index)))
    ax.set_xticklabels(data.index, rotation = 45)

    # save plot to figs folder. In python change under #display the plot
    # save the plot with a unique file name
    # data-python/gapminder_gdp_xxx.csv - input name
    split_name1 = filename.split('.')[0] #data-python/gapminder_gdp_xxx
    split_name2 = filename.split('/')[1] #gapminder_gdp_xxx
    save_name = 'figs/' + split_name2 + '.png'
    plt.savefig(save_name)

