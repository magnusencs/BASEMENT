def shopping():
    barang = ["sabun", "sikat gigi", "odol", "sampo", "pasta gigi"]
    harga = [3000, 5000, 4000, 10000, 7000]
    total = 0
    barang_dibeli = []
    for i in range(len(barang)):
        print(f"{i + 1}. {barang[i]}, Rp{harga[i]}")
    
    while True:
        pilih = int(input("pilih barang yang ingin dibeli (ketik 0 untuk selesai): "))
        if pilih == 0:
            break
        if pilih < 0 or pilih > len(barang):
            print("pilihan tidak valid, coba lagi.")
            continue
        if 1 <= pilih <= len(barang): #njir bisa gitu?
            total += harga[pilih - 1]
            barang_dibeli.append(barang[pilih - 1])
            print(f"{barang[pilih - 1]} ditambahkan ke keranjang. Total sementara: Rp{total}")
    if total > 100000: total *= 0.9
    print("Barang yang dibeli:") 
    nomor = 1
    if not barang_dibeli:
        print("Tidak ada barang yang dibeli.")
    else:
        for item in barang_dibeli:
            print(f"{nomor}. {item}")
            nomor += 1
        print(f"Total belanjaan: Rp{total}")
      


def calculator(input1, input2, operation):
    if operation == '+':
        return input1 + input2
    elif operation == '-':
        return input1 - input2
    elif operation == '*':
        return input1 * input2
    elif operation == '/':
        return input1 / input2
    else:
        return "Invalid operation"


def main_calc():
    input1 = float(input("enter first number: "))
    input2 = float(input("enter second number: "))
    operation = input("enter operation (+, -, *, /): ")
    result = calculator(input1, input2, operation)
    print(result)

def guessingGame():
    import random
    failAmount = 0
    number = random.randint(1, 20)
    guessedNum = int(input("enter a number between 1 and 20:"))
    while failAmount < 6:
        if guessedNum == number: 
            print(f"you win! the number was {number} you smart nigga")
            break
        elif guessedNum < number: 
            failAmount += 1
            print (f"{guessedNum} is too low, try again: \n")
            guessedNum = int(input())

        elif guessedNum > number: 
            failAmount += 1
            print (f"{guessedNum} is too high, try again: \n")
            guessedNum = int(input())
    
    if failAmount == 3: print(f"you lose! the number was {number}, fucking loser!")

if __name__ == "__main__": #calc.py would have its __name__ set to "__main__" if and only if it's explicitly run
    
    while True:
        arr = ["shopping list", "calculator", "guessing game", "quit"]
        
        for i in range (len(arr)):
            print(f"{i + 1}. {arr[i]}")
        choice = int(input("choose a program you fucking idiot: "))
        if choice == 1:
            shopping()
        elif choice == 2:
            main_calc()
        elif choice == 3:
            guessingGame()
        elif choice == 4:
            break
        else:
            print("bitch, dont play around")
    
    

        
        
    
