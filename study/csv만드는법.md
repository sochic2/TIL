lunch = {
  '용성돌솥비빔밥':'054-474-7119',
  '별난짬뽕':'054-473-3040',
  '매콤돈가스':'054-472-2030'
}

# 1. string formatting
with open('lunch.csv','w') as f:
    for item in lunch.items():
        f.write(f'{item[0]},{item[1]}\r\n')

# 2. join
with open('lunch.csv','w') as f:
    for item in lunch.items():
        f.write(','.join(item)+'\r\n')

# 3. csv.writer
import csv
with open('lunch.csv','w') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)


# 4. csv.DictWriter
import csv
with open('names.csv', 'w', newline='') as f:
    fieldnames = ('first_name', 'last_name')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})