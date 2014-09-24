#Lincoln Samelson
#CSCI 3104
#HW #3

import csv
from decimal import *

def read_file():
    open_price = []
    with open('HistoricalQuotesMSFT.csv', 'rb') as f:    #Change the file name in here
        reader = csv.reader(f)
        for row in reader:
            open_price.append(row[3])

        open_price.pop(0)     #Remove Headers
        open_price.pop(1)
        open_result = [float(x.strip(' "')) for x in open_price]
        open_result.reverse()
    return open_result


def Profit(array):
    # If the array is empty, return nothing
    if len(array) == 0:
        return 0

    profit = 0
    cheapest = array[0]

    for i in range(1, len(array)):
        # Update the minimum to be the lower of the existing minimum and the new minimum.

        cheapest = min(cheapest, array[i])

        # Update the maximum profit to be the larger of the old profit and the
        # profit made by buying at the lowest value and selling at the current price.

        profit = max(profit, array[i] - cheapest)

    return profit


if __name__ == "__main__":
    #Read in File
    open_array = read_file()
    print
    print open_array
    #Run the profit algorithm on the specific stock
    max_profit = Profit(open_array)
    print "Your max possible profit would be:  $",max_profit


