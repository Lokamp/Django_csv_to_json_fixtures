import csv

from data.data import jobs

dict_jobs = jobs

with open('file.csv', 'w', encoding='utf-8', newline='') as file:
    list_fieldnames = [title for title in dict_jobs[0]]  # create fieldnames
    list_fieldnames_with_id = list_fieldnames.insert(0, 'id')  # added id first row for django fixtures
    writer = csv.DictWriter(file, fieldnames=list_fieldnames)
    writer.writeheader()
    dict_writerow = {}
    for i, x in enumerate(dict_jobs, 1):
        x['id'] = i
    for i in dict_jobs:
        for title, value in i.items():
            dict_writerow[title] = value
        writer.writerow(dict_writerow)
    print('file.svc created')
