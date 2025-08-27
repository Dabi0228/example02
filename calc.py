import sys  # ← untuk membaca argumen baris perintah

def add(a, b):
    return a + b  # ← penjumlahan

def sub(a, b):
    return a - b  # ← pengurangan

def run(a, op, b):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    else:
        raise ValueError("Operator harus '+' atau '-'")

if __name__ == "__main__":
    if len(sys.argv) == 4:
        # Mode argumen: python calc.py 5 + 3
        try:
            a = float(sys.argv[1])   # ← angka pertama
            op = sys.argv[2]         # ← operator: '+' atau '-'
            b = float(sys.argv[3])   # ← angka kedua
            print(run(a, op, b))     # ← cetak hasil
        except ValueError as e:
            print("Error:", e)
            print("Cara pakai: python calc.py 5 + 3")
    else:
        # Mode interaktif: minta input jika argumen tidak lengkap
        try:
            a = float(input("Masukkan angka pertama: "))
            op = input("Masukkan operator (+ atau -): ").strip()
            b = float(input("Masukkan angka kedua: "))
            print(run(a, op, b))
        except ValueError as e:
            print("Error:", e)
