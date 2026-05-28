total_amount = int(input("Nhập tổng số tiền hóa đơn ban đầu:  "))

reduced_amount = 0

if total_amount >= 500000 :
    reduced_amount = total_amount * 0.1
else :
    reduced_amount = 0

final_total = total_amount - reduced_amount

print("---HÓA ĐƠN THANH TOÁN RIKKEI STORE----")
print("Số tiền được giảm giá:",int(reduced_amount), "VND")
print("Tổng tiền của khách phải trả:",int(final_total), "VND")

