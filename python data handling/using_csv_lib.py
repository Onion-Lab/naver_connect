import csv

data_csv = open("D:\\Python\\Naver_connect\\python_data_handling\\Data.csv","r",encoding="utf-8")
new_data_csv = open("D:\\Python\\Naver_connect\\python_data_handling\\Data2.csv","w",encoding="utf-8")

read_csv_data = csv.reader(data_csv)
write_csv_data = csv.writer(new_data_csv, delimiter="\t", quotechar="'", quoting=csv.QUOTE_ALL)

index = 0
new_data=[]

for data in read_csv_data :
    if index == 0 :
        new_data.append(data)
        index = index+1
    
    loc = data[7]

    if "성남시" in loc :
        new_data.append(data)

for data in new_data :
    write_csv_data.writerow(data)