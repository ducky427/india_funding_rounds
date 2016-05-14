
import csv
import urllib

from bs4 import BeautifulSoup

URLS = ['http://trak.in/india-startup-funding-investment-2015/january-2015/',
        'http://trak.in/india-startup-funding-investment-2015/february-2015/',
        'http://trak.in/india-startup-funding-investment-2015/march-2015/',
        'http://trak.in/india-startup-funding-investment-2015/april-2015/',
        'http://trak.in/india-startup-funding-investment-2015/may-2015/',
        'http://trak.in/india-startup-funding-investment-2015/june-2015/',
        'http://trak.in/india-startup-funding-investment-2015/july-2015/',
        'http://trak.in/india-startup-funding-investment-2015/august-2015/',
        'http://trak.in/india-startup-funding-investment-2015/september-2015/',
        'http://trak.in/india-startup-funding-investment-2015/october-2015/',
        'http://trak.in/india-startup-funding-investment-2015/november-2015/',
        'http://trak.in/india-startup-funding-investment-2015/december-2015/',
        'http://trak.in/india-startup-funding-investment-2015/january-2016/',
        'http://trak.in/india-startup-funding-investment-2015/february-2016/',
        'http://trak.in/india-startup-funding-investment-2015/']

def get_row_text(row):
    cells = row.find_all('td')
    res = [c.get_text().encode('ascii', 'ignore') for c in cells]
    return res

def main(url, writer):
    i = 1
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")
    tables = soup.find_all('table')
    print "Number of tables: %s" % (len(tables),)
    res = []
    header = None
    for table in tables:
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
        if header is None:
            header = get_row_text(rows[0])
            if i == 1:
                header[1] = 'Date'
                writer.writerow(header)
        for row in rows[1:]:
            r = get_row_text(row)
            r[0] = i
            if len(r[2].strip()) > 0:
                assert len(r) == len(header)
                writer.writerow(r)
                i += 1

if __name__ == '__main__':
    for u in URLS:
        name = u.split('/')[-2] + '.csv'
        with open(name, 'wb') as f:
            writer = csv.writer(f)
            main(u, writer)
