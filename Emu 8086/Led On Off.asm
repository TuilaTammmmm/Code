;Tất cả đèn nhấp nháy liên tục

.model small           ; Chỉ định mô hình bộ nhớ nhỏ (code và data <= 64KB)
.stack 100h            ; Định nghĩa kích thước stack là 256 bytes (100h)
.code                  ; Bắt đầu đoạn mã chương trình

start:
    mov al, 0FFh        ; Đặt thanh ghi AL với giá trị 0FFh (tất cả các bit = 1, bật tất cả LED)
loop1:
    not al              ; Đảo ngược tất cả các bit trong AL (bật/tắt trạng thái LED)
    out 0FFh, al        ; Gửi giá trị trong AL ra cổng 0FFh (điều khiển LED)
    call delay          ; Gọi hàm delay để tạo độ trễ
    jmp loop1           ; Quay lại vòng lặp, tiếp tục thay đổi trạng thái LED

delay:
    mov cx, 1000        ; Đặt giá trị ban đầu của bộ đếm CX là 1000 (độ trễ)
delay_loop:
    nop                 ; Lệnh không làm gì (No Operation), mất 1 chu kỳ
    loop delay_loop     ; Giảm CX, nếu CX != 0 thì quay lại delay_loop
    ret                 ; Kết thúc hàm delay, quay lại vị trí gọi hàm
end start               ; Kết thúc chương trình, điểm bắt đầu là nhãn 'start'


