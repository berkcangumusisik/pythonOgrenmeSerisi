
"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.
1,1,2,3,5,8,13,21,34...............
"""
ilkSayi = 1

ikincisayi = 1

fibonacci = [ilkSayi,ikincisayi]
for i in range(10):


    ilkSayi,ikincisayi = ikincisayi,ilkSayi + ikincisayi

    fibonacci.append(ikincisayi)

print(fibonacci)