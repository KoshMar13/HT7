import csv


def exportCsv(rows):
    fields = ['id', 'name', 'phone_number', 'note']
    with open('new_data.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(rows)


def csvImp():
    with open('new_data.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(f)
        return data
