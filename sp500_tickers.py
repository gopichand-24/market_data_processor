#! /usr/bin/env python3

'''Script to get the list of S&P 500 tickers'''
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_sp500_table():
    '''
    Parse a wikipedia article to extract information on the S&P 500 companies
    :return: Data Frame containing company tickers, names, sector
    information etc., of all the companies in S&P 500.
    '''
    # Todo:- Add a test case for this function.
    url = "https://en.wikipedia.org/wiki/List_of_S&P_500_companies"
    resp = requests.get(url)
    # resp.text is the content of the response in unicode.
    soup = BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class': 'wikitable sortable'})
    # Each row in the table is limited by <tr>..</tr>.
    rows = table.findAll('tr')
    # The first row is the header of the table. Each cell in the header is
    # delimited by <th>..</th>
    columns = [x.text for x in rows[0].findAll('th')]
    # The cells in each row are delimited by <td>..</td>
    df = pd.DataFrame([[cell.text
                        for cell in row.findAll('td')]
                       for row in rows[1:]],
                      columns=columns)
    return df


def get_sp500_tickers():
    '''Get the list of S&P 500 tickers'''
    return get_sp500_table()['Ticker symbol'].tolist()


if __name__ == "__main__":
    # from time import time
    # start = time()
    print(*get_sp500_tickers(), sep='\n')
    # print("time taken = ", time()-start, " s")
