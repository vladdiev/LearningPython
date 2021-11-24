"""
Домашнее задание №1
Цикл for: Продажи товаров
* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phones_sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
  
sales_iphone = 0 
for total in phones_sales[0]['items_sold']:
  sales_iphone += total
print(f"Суммарное количество продаж для {phones_sales[0]['product']} - {sales_iphone}")

sales_Xiaomi = 0 
for total in phones_sales[1]['items_sold']:
  sales_Xiaomi += total
print(f"Суммарное количество продаж для {phones_sales[1]['product']} - {sales_Xiaomi}")

sales_Samsung = 0 
for total in phones_sales[2]['items_sold']:
  sales_Samsung += total
print(f"Суммарное количество продаж для {phones_sales[2]['product']} - {sales_Samsung}")

avg_sales_iPhone = 0
for avg in phones_sales[0]['items_sold']:
  avg_sales_iPhone += avg 
res_avg_iPhone = avg_sales_iPhone // len(phones_sales[0]['items_sold'])
print(f"Среднее количество продаж для {phones_sales[0]['product']} - {res_avg_iPhone}")

avg_sales_Xiaomi = 0
for avg in phones_sales[1]['items_sold']:
  avg_sales_Xiaomi += avg
avg_sales_Xiaomi = avg_sales_Xiaomi // len(phones_sales[1]['items_sold'])
print(f"Среднее количество продаж для {phones_sales[1]['product']} - {avg_sales_Xiaomi}")

avg_sales_Samsung = 0
for avg in phones_sales[2]['items_sold']:
  avg_sales_Samsung += avg
avg_sales_Samsung = avg_sales_Samsung // len(phones_sales[2]['items_sold'])
print(f"Среднее количество продаж для {phones_sales[2]['product']} - {avg_sales_Samsung}")

total_sum_sales = sales_iphone + sales_Xiaomi + sales_Samsung
print (f'Суммарное количество продаж всех товаров: {total_sum_sales}')

total_avg_sales = total_sum_sales // len(phones_sales)
print (f'Среднее количество продаж всех товаров: {total_avg_sales}')