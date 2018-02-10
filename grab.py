from data import reports, years
import urllib.request, contextlib, os, codecs

def clean(filename, extension = '.csv'):
    with codecs.open(filename + extension, 'w', 'utf-8') as out:
        file = codecs.open(filename, 'r', 'latin-1')
        for filedata in file:
            filedata = filedata.replace('\xe8', 'c')
            filedata = filedata.replace('\xe6', 'c')
            filedata = filedata.replace('\xf0', 'd')
            filedata = filedata.replace('\x9a', 's')
            filedata = filedata.replace('\x9e', 'z')
            out.write(filedata)
        file.close()

def generateName(year, course, extension = ''):
    return format(year, '02d') + '-' + format(course, '04d') + extension

def skiniIzvjestaj(year, course, location = './csv/', testing = False):
    if year in years and course in reports or testing:
        print('Skidam course broj ' + str(course) + ' u akademskoj ' + str(year) + ' godini')
        url = 'https://zamger.etf.unsa.ba/index.php?sta=izvjestaj/csv_converter&koji_izvjestaj=izvjestaj/course&course=' + str(course) + '&ag=' + str(year) + '&'  
        filename = location +  generateName(year, course)
        urllib.request.urlretrieve(url, filename)
        clean(filename)
        with contextlib.suppress(FileNotFoundError):
            os.remove(filename)

def skiniSveIzvjestajeIzyears(year, location = './csv/'):
    if year in years:
        for course in reports:
            skiniIzvjestaj(year, course, location)

def skiniSveIzvjestaje(location = './csv/'):
    for year in years:
        for course in reports:
            skiniIzvjestaj(year, course, location)

def skiniSveIzvjestajeZacourse(course, location = './csv/'):
    if course in reports:
        for year in years:
            skiniIzvjestaj(year, course, location)

