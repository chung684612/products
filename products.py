product = []
while True:
	name = input('請輸入購買商品名稱: ')
	if name == 'q':
		break
	price = int(input('請輸入購買此商品之價錢: '))
	product.append([name, price])
number = int(input('請輸入想要收尋商品之編號: '))
print(product[number])
