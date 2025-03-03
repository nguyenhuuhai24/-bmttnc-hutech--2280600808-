print("nhập các dòn văn bản (nhập 'done' để kết thúc:")
line = []
while true:
line = input()
if line.lower() == 'done':
    break
lines.append(line)
print("\n các dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())
    