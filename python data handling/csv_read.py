
customer_csv = open("D:\\Python\\Naver_connect\\python_data_handling\\customers.csv", "r", encoding="utf-8")

line_counter = 0
data_header = customer_csv.readline().replace('\n','').split(',')
customer_list = []


for data in customer_csv:
    customer_list.append(data.replace("\n","").split(","))


print(data_header)
print(customer_list)