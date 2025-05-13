print("nhap cac dong van ban (nhap 'done' de ket thuc):")
lines =[]
while True:
    line = input()
    if line.lower()== 'dome':
        break 
    lines.append(line) 
    print("\n các dòng đã nhập sau khi chuyển thành chữ in hoa :")
    for line in lines :
        print(line.upper())