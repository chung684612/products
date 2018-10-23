import os

product = []
if os.path.isfile('products.csv'):
	print('檔案存在!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'Mechandise,Price' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
else:
	print('檔案不存在, 請創立一個新的!')
while True:
	name = input('請輸入購買商品名稱: ')
	if name == 'q':
		break
	price = int(input('請輸入購買此商品之價錢: '))
	product.append([name, price])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Mechandise,Price\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')