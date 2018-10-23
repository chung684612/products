product = []
while True:
	name = input('請輸入購買商品名稱: ')
	if name == 'q':
		break
	price = int(input('請輸入購買此商品之價錢: '))
	product.append([name, price])

with open('products.csv', 'w') as f:
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')