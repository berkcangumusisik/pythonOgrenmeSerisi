from art import logo

def toplama(n1, n2):
  return n1 + n2

def cikarma(n1, n2):
  return n1 - n2

def carpma(n1, n2):
  return n1 * n2

def bolme(n1, n2):
  return n1 / n2

operations = {
  "+": toplama,
  "-": cikarma,
  "*": carpma,
  "/": bolme
}

def calculator():
  print(logo)

  num1 = float(input("Birinci Sayıyı Giriniz: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Yapmak istediğiniz işlemi seçiniz: ")
    num2 = float(input("İkinci Sayıyı Giriniz: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Aynı sayılarla farklı işlem yapmak için 'y' tuşuna, yeni sayılarla işlem yapmak için 'n' tuşuna basınız: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
