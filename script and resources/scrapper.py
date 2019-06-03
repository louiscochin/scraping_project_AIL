import bs4 as bs
import urllib
import urllib.request as request
from fake_useragent import UserAgent
import csv


def amount_of_variable_per_school(csv_file_path, variable_result):

    school_numbers = []

    chomped_variable = ""

    for char in variable_result:
        if char == " ":
            chomped_variable += "+"
        else:
            chomped_variable += char

    append_decision = input("Would you like to append the new variable results to this CSV file?" + "\n" + "y / n:")
    append = True
    if (append_decision == "n"):
        append = False

    #with open(csv_file_path) as f:
        #row_count = len(f.readlines())

    with open(csv_file_path, newline='') as csvfile:
        text = csv.reader(csvfile, delimiter=';', quotechar='|')
        current_row = 0

        for row in text:
            current_row += 1
            school = str(row[0])
            school.encode('utf-8').strip()
            chomped_name = ""

            for char in school:
                if char != " " and char != "\ufeff":
                    chomped_name += char

            ua = UserAgent()
            req = request.Request("https://www.google.com/search?q=" + chomped_name + chomped_variable)
            req.add_header('User-Agent', ua.chrome)

            source = urllib.request.urlopen(req)
            soupt = bs.BeautifulSoup(source, 'lxml')
            full_div = str(soupt.find('div', class_='Z0LcW'))

            end_slice = len(full_div) - 6
            variable_result = full_div[19:end_slice]
            school_numbers += variable_result
            #print("Currently at " + str(current_row / row_count * 100)[:4] + "%")

            if append == True:
                row.append(variable_result)
            print(row)

    return school_numbers

amount_of_variable_per_school('testdata.csv', "is in what city")


