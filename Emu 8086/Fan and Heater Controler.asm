.model small
.stack 100h
.data
temp db 0               ; Biến lưu trữ nhiệt độ đọc từ cảm biến

.code
start:
    mov ax, @data       ; Khởi tạo đoạn dữ liệu
    mov ds, ax          ; Gán DS (Data Segment) với địa chỉ đoạn dữ liệu

main_loop:
    ; Đọc nhiệt độ từ cảm biến ở cổng 3FDh
    mov dx, 3FDh        ; Đặt địa chỉ cổng cảm biến nhiệt độ vào DX
    in  al, dx          ; Đọc giá trị nhiệt độ từ cổng vào thanh ghi AL
    mov temp, al        ; Lưu giá trị nhiệt độ vào biến `temp`

    ; So sánh nhiệt độ > 25
    mov al, temp        ; Lấy giá trị nhiệt độ từ biến `temp` vào AL
    cmp al, 25          ; So sánh nhiệt độ với 25
    ja turn_on_fan       ; Nếu nhiệt độ > 25°C, nhảy đến đoạn bật quạt

    ; So sánh nhiệt độ < 22
    mov al, temp        ; Lấy lại giá trị nhiệt độ từ biến `temp` vào AL
    cmp al, 22          ; So sánh nhiệt độ với 22
    jb turn_on_heater    ; Nếu nhiệt độ < 22°C, nhảy đến đoạn bật đèn sưởi

    ; Nếu nhiệt độ trong khoảng [22–25]
    jmp turn_off_all     ; Nếu nhiệt độ nằm trong khoảng 22–25°C, tắt cả quạt và đèn sưởi

turn_on_fan:
    ; Bật quạt (ghi giá trị FFh vào cổng 3FFh), tắt đèn sưởi (ghi giá trị 00h vào cổng 3FEh)
    mov al, 0FFh        ; Giá trị FFh để bật quạt
    mov dx, 3FFh        ; Đặt địa chỉ cổng quạt vào DX
    out dx, al          ; Ghi giá trị vào cổng để bật quạt

    mov al, 00h         ; Giá trị 00h để tắt đèn sưởi
    mov dx, 3FEh        ; Đặt địa chỉ cổng đèn sưởi vào DX
    out dx, al          ; Ghi giá trị vào cổng để tắt đèn sưởi

    jmp delay_and_loop  ; Nhảy đến đoạn chờ và lặp lại

turn_on_heater:
    ; Bật đèn sưởi (ghi giá trị FFh vào cổng 3FEh), tắt quạt (ghi giá trị 00h vào cổng 3FFh)
    mov al, 0FFh        ; Giá trị FFh để bật đèn sưởi
    mov dx, 3FEh        ; Đặt địa chỉ cổng đèn sưởi vào DX
    out dx, al          ; Ghi giá trị vào cổng để bật đèn sưởi

    mov al, 00h         ; Giá trị 00h để tắt quạt
    mov dx, 3FFh        ; Đặt địa chỉ cổng quạt vào DX
    out dx, al          ; Ghi giá trị vào cổng để tắt quạt

    jmp delay_and_loop  ; Nhảy đến đoạn chờ và lặp lại

turn_off_all:
    ; Tắt cả quạt và đèn sưởi
    mov al, 00h         ; Giá trị 00h để tắt quạt
    mov dx, 3FFh        ; Đặt địa chỉ cổng quạt vào DX
    out dx, al          ; Ghi giá trị vào cổng để tắt quạt

    mov dx, 3FEh        ; Đặt địa chỉ cổng đèn sưởi vào DX
    out dx, al          ; Ghi giá trị vào cổng để tắt đèn sưởi

delay_and_loop:
    ; Chờ 1 phút bằng cách thực hiện 600 lệnh NOP
    mov cx, 600         ; Đặt bộ đếm vòng lặp là 600
delay1:
    nop                 ; Lệnh NOP (No Operation) không làm gì, chỉ tốn thời gian
    loop delay1         ; Giảm CX và lặp lại nếu CX > 0

    jmp main_loop       ; Quay lại vòng lặp chính

end start               ; Kết thúc chương trình, bắt đầu thực thi từ nhãn `start`
