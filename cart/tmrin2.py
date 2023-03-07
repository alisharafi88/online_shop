

aaaa = {
    'cart': {
        'products': {'qq': 2},
        'products2': {'qq': 2}

    }
}

print(aaaa['cart']['products'])

del aaaa['cart']['products']

print(aaaa['cart'])

qq = 1
aaaa['cart'][qq] ={}

print(aaaa['cart'])
