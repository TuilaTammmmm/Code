.model small            ; Chỉ định mô hình bộ nhớ nhỏ (code và data <= 64KB)
.stack 100h               ; Đặt kích thước stack là 256 bytes (100h)
.code                     ; Bắt đầu đoạn mã chương trình
start2:
    mov al, 80h           ; Đặt giá trị ban đầu cho AL: LED trái nhất sáng (10000000)
loop2:
    mov dx, 02C0h     ; Gán địa chỉ cổng ra vào DX
    out dx, al        ; Xuất dữ liệu từ AL ra cổng 02C0h
    shr al, 1             ; Dịch phải 1 bit (LED sáng di chuyển sang phải)
    call delay2           ; Gọi hàm delay để tạo độ trễ
    test al, 01h          ; Kiểm tra bit thấp nhất (D8) của AL
    jnz end_loop          ; Nếu bit thấp nhất là 1, nhảy đến end_loop
    jmp loop2             ; Nếu không, quay lại loop2 để tiếp tục
end_loop:
    mov al, 00h           ; Tắt tất cả các LED (AL = 00000000)
    mov dx, 02C0h     ; Gán địa chỉ cổng ra vào DX
    out dx, al        ; Xuất dữ liệu từ AL ra cổng 02C0h
    jmp $                 ; Dừng chương trình (hoặc có thể thay bằng lệnh restart)
delay2:
    mov cx, 2000          ; Đặt giá trị ban đầu cho bộ đếm CX (tạo độ trễ)
delay_loop2:
    nop                   ; Lệnh không làm gì (No Operation)
    loop delay_loop2      ; Giảm CX, lặp lại cho đến khi CX = 0
    ret                   ; Quay lại đoạn mã gọi hàm delay2
end start2                ; Kết thúc chương trình
