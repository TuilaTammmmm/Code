-- Đào Duy Tâm-B23DVCN169


-- 1. Tạo mới cơ sở dữ liệu QLBanhang với :
CREATE DATABASE QLBanhang
ON PRIMARY
(
    NAME = 'QLBanhang_Data',
    FILENAME = 'D:\QLBanhang_Data.mdf',
    SIZE = 100MB,
    MAXSIZE = 200MB,
    FILEGROWTH = 10MB
)
LOG ON
(
    NAME = 'QLBanhang_Log',
    FILENAME = 'D:\QLBanhang_Log.ldf',
    SIZE = 30MB,
    MAXSIZE = UNLIMITED,
    FILEGROWTH = 5MB
);
GO
USE QLBanHang;
GO
-- 2. Tạo các bảng cho cơ sở dữ liệu trên:
-- Vật Tư
CREATE TABLE VATTU (
    MaVTu CHAR(4) NOT NULL,
    TenVTu NVARCHAR(100),
    DvTinh NVARCHAR(10),
    PhanTram REAL
);

-- Nhà Cung Cấp
CREATE TABLE NCC (
    MaNCC CHAR(3) NOT NULL,
    TenNCC NVARCHAR(100),
    Diachi NVARCHAR(100),
    Dienthoai VARCHAR(20)
);

-- Đơn Đặt Hàng
CREATE TABLE DONDH (
    SODH CHAR(4) NOT NULL,
    NgayDH DATETIME,
    MaNCC CHAR(3)
);

-- Chi Tiết Đơn Đặt Hàng
CREATE TABLE CTDONDH (
    SODH CHAR(4) NOT NULL,
    MaVTu CHAR(4) NOT NULL,
    SIDat INT
);

-- Phiếu Nhập
CREATE TABLE PNHAP (
    SOPN CHAR(4) NOT NULL,
    Ngaynhap DATETIME,
    SODH CHAR(4)
);

-- Chi Tiết Phiếu Nhập
CREATE TABLE CTPNHAP (
    SOPN CHAR(4) NOT NULL,
    MaVTu CHAR(4) NOT NULL,
    SINhap INT,
    DgNhap MONEY
);

-- Phiếu Xuất
CREATE TABLE PXUAT (
    SOPX CHAR(4) NOT NULL,
    Ngayxuat DATETIME,
    TenKH NVARCHAR(100)
);

-- Chi Tiết Phiếu Xuất
CREATE TABLE CTPXUAT (
    SOPX CHAR(4) NOT NULL,
    MaVTu CHAR(4) NOT NULL,
    SIXuat INT,
    DgXuat MONEY
);

-- Tồn Kho
CREATE TABLE TONKHO (
    Namthang CHAR(6) NOT NULL,
    MaVTu CHAR(4) NOT NULL,
    SIDau INT,
    TongSLN INT,
    TongSLX INT,
    SlCuoi AS (SIDau + TongSLN - TongSLX)
);

-- 3. Tạo các ràng buộc cho các bảng trên như sau:
-- Bảng VATTU:
ALTER TABLE VATTU ADD CONSTRAINT PK_VATTU PRIMARY KEY (MaVTu); -- Mã vật tư là khóa chính
ALTER TABLE VATTU ADD CONSTRAINT UQ_TenVTu UNIQUE (TenVTu); -- Tên vật tư là duy nhất
ALTER TABLE VATTU ADD CONSTRAINT DF_DvTinh DEFAULT N'' FOR DvTinh;  -- Giá trị mặc định cho cột đơn vị tính là ‘’ 0<=Phần trăm<=100
ALTER TABLE VATTU ADD CONSTRAINT CK_PhanTram CHECK (PhanTram >= 0 AND PhanTram <= 100);

-- Bảng NHACC:
ALTER TABLE NCC ADD CONSTRAINT PK_NCC PRIMARY KEY (MaNCC); -- Mã nhà cung cấp là khóa chính
ALTER TABLE NCC ADD CONSTRAINT UQ_TenNCC_Diachi UNIQUE (TenNCC, Diachi); -- Tên và địa chỉ của nhà cung cấp là duy nhất
ALTER TABLE NCC ADD CONSTRAINT DF_Dienthoai DEFAULT N'Chưa có' FOR Dienthoai; -- Giá trị mặc định cho cột điện thoại là ‘Chưa có’

-- Bảng DONDH:
ALTER TABLE DONDH ADD CONSTRAINT PK_DONDH PRIMARY KEY (SODH); -- Số đơn đặt hàng là khóa chính
ALTER TABLE DONDH ADD CONSTRAINT DF_NgayDH DEFAULT GETDATE() FOR NgayDH; -- Giá trị mặc định cho cột ngày đặt hàng là ngày hiện hành

-- Bảng PNHAP
ALTER TABLE PNHAP ADD CONSTRAINT PK_PNHAP PRIMARY KEY (SOPN); -- Số đơn đặt hàng là khóa chính

-- Bảng PXUAT 
ALTER TABLE PXUAT ADD CONSTRAINT PK_PXUAT PRIMARY KEY (SOPX); -- Số đơn đặt hàng là khóa chính

-- Bảng CTDONDH:
ALTER TABLE CTDONDH ADD CONSTRAINT PK_CTDONDH PRIMARY KEY (SODH, MaVTu); -- (Số đơn hàng, mã vật tư) là khóa chính
ALTER TABLE CTDONDH ADD CONSTRAINT CK_SIDat CHECK (SIDat > 0); -- Số lượng đặt>0

-- Bảng CTPNHAP:
ALTER TABLE CTPNHAP ADD CONSTRAINT PK_CTPNHAP PRIMARY KEY (SOPN, MaVTu); -- Số phiếu nhập và mã vật tư là khóa chính
ALTER TABLE CTPNHAP ADD CONSTRAINT CK_CTPNHAP CHECK (SINhap > 0 AND DgNhap > 0); -- Số lượng nhập và đơn giá nhập>0

-- Bảng CTPXUAT:
ALTER TABLE CTPXUAT ADD CONSTRAINT PK_CTPXUAT PRIMARY KEY (SOPX, MaVTu); -- Số phiếu xuất và mã vật tư là khóa chính
ALTER TABLE CTPXUAT ADD CONSTRAINT CK_CTPXUAT CHECK (SIXuat > 0 AND DgXuat > 0); -- Số lượng xuất và đơn giá xuất > 0

-- Bảng TONKHO:
ALTER TABLE TONKHO ADD CONSTRAINT PK_TONKHO PRIMARY KEY (Namthang, MaVTu); -- Năm tháng, mã vật tư là khóa chính
ALTER TABLE TONKHO ADD CONSTRAINT DF_SIDau DEFAULT 0 FOR SIDau; -- Số lượng đầu, tổng số lượng nhập và tổng số lượng xuất >= 0 và đều có giá trị mặc định = 0
ALTER TABLE TONKHO ADD CONSTRAINT DF_TongSLN DEFAULT 0 FOR TongSLN;
ALTER TABLE TONKHO ADD CONSTRAINT DF_TongSLX DEFAULT 0 FOR TongSLX;
ALTER TABLE TONKHO ADD CONSTRAINT CK_TONKHO CHECK (SIDau >= 0 AND TongSLN >= 0 AND TongSLX >= 0); -- Số lượng cuối =Số lượng đầu+Tổng số lượng nhập-Tổng số lượng xuất

-- 4. Thêm các ràng buộc về khóa ngoại cho các bảng như sau:
--STT Bảng Cột Bảng tham chiếu
--1 DONDH MaNCC NHACC
--2 CTDONDH MaVTu VATTU
--3 CTDONDH SoDH DONDH
--4 PNHAP SoDH DONDH
--5 CTPNHAP MaVTu VATTU
--6 CTPNHAP SoPN PNHAP
--7 CTPXUAT MaVTu VATTU
--8 CTPXUAT SoPX PXUAT
--9 TONKHO MaVTu VATTU

-- 1
ALTER TABLE DONDH ADD CONSTRAINT FK_DONDH_NCC FOREIGN KEY (MaNCC) REFERENCES NCC(MaNCC);
-- 2
ALTER TABLE CTDONDH ADD CONSTRAINT FK_CTDONDH_VATTU FOREIGN KEY (MaVTu) REFERENCES VATTU(MaVTu);
-- 3
ALTER TABLE CTDONDH ADD CONSTRAINT FK_CTDONDH_DONDH FOREIGN KEY (SODH) REFERENCES DONDH(SODH);
-- 4
ALTER TABLE PNHAP ADD CONSTRAINT FK_PNHAP_DONDH FOREIGN KEY (SODH) REFERENCES DONDH(SODH);
-- 5
ALTER TABLE CTPNHAP ADD CONSTRAINT FK_CTPNHAP_VATTU FOREIGN KEY (MaVTu) REFERENCES VATTU(MaVTu);
-- 6
ALTER TABLE CTPNHAP ADD CONSTRAINT FK_CTPNHAP_PNHAP FOREIGN KEY (SOPN) REFERENCES PNHAP(SOPN);
-- 7
ALTER TABLE CTPXUAT ADD CONSTRAINT FK_CTPXUAT_VATTU FOREIGN KEY (MaVTu) REFERENCES VATTU(MaVTu);
-- 8
ALTER TABLE CTPXUAT ADD CONSTRAINT FK_CTPXUAT_PXUAT FOREIGN KEY (SOPX) REFERENCES PXUAT(SOPX);
-- 9
ALTER TABLE TONKHO ADD CONSTRAINT FK_TONKHO_VATTU FOREIGN KEY (MaVTu) REFERENCES VATTU(MaVTu);
GO

-- 5. Tạo mô hình quan hệ cho CSDL trên.

--6. Nhập dữ liệu thử sau đó tạo file backup cho CSDL QLBanhang, thử xóa CSDL QLBanhang rồi phục hồi dữ liệu từ file backup.

-- Bảng VATTU
INSERT INTO VATTU (MaVTu, TenVTu, DvTinh, PhanTram) VALUES
('DD01', N'Đầu DVD Hitachi 1 đĩa', N'Bộ', 40),
('DD02', N'Đầu DVD Hitachi 3 đĩa', N'Bộ', 40),
('L001', N'Loa Panasonic 1000W', N'Bộ', 10),
('TL15', N'Tủ lạnh Sanyo 120 lit', N'Cái', 25),
('TL90', N'Tủ lạnh Sanyo 90 lit', N'Cái', 20),
('TV14', N'TV Sony 14 inches', N'Cái', 15),
('TV21', N'TV Sony 21 inches', N'Cái', 10),
('TV29', N'TV Sony 29 inches', N'Cái', 10),
('VD01', N'Đầu VCD Sony 1 đĩa', N'Bộ', 30),
('VD02', N'Đầu VCD Sony 3 đĩa', N'Bộ', 30);

-- Bảng NCC
INSERT INTO NCC (MaNCC, TenNCC, Diachi, Dienthoai) VALUES
('C01', N'Lưu Thanh Duyên', N'334 Thanh Xuân HN', DEFAULT),
('C02', N'Nguyễn Thanh Hoài', N'225 Định Công HN', '8253467'),
('C03', N'Dương Đức Mạnh', N'120 Lý Thái Tổ HN', '8257456'),
('C04', N'Nguyễn Hoài Nguyên', N'45A Liễu Giai HN', '8287654'),
('C05', N'Nguyễn Thị Trang', N'18 Trường Chinh HN', '8587648'),
('C06', N'Trần Ngọc Anh', N'58 Quán Sứ HN', '853128'),
('C07', N'Trần Ngọc Trâm', N'125 Tôn Đức Thắng HN', '8567381');

-- Bảng DONDH
INSERT INTO DONDH (SODH, NgayDH, MaNCC) VALUES
('D001', '2002-01-15', 'C03'),
('D002', '2002-01-30', 'C01'),
('D003', '2002-02-10', 'C02'),
('D004', '2002-02-17', 'C05'),
('D005', '2002-03-01', 'C02'),
('D006', '2002-03-12', 'C05');

-- Bảng CTDONDH
INSERT INTO CTDONDH (SODH, MaVTu, SIDat) VALUES
('D001', 'DD01', 10), ('D001', 'DD02', 15),
('D002', 'VD02', 30), ('D003', 'TV14', 10),
('D003', 'TV29', 20), ('D004', 'TL90', 10),
('D005', 'TV14', 10), ('D005', 'TV29', 20),
('D006', 'TV14', 10), ('D006', 'TV29', 20),
('D006', 'VD01', 20);

-- Bảng PNHAP
INSERT INTO PNHAP (SOPN, Ngaynhap, SODH) VALUES
('N001', '2002-01-17', 'D001'), ('N002', '2002-01-20', 'D001'),
('N003', '2002-01-31', 'D002'), ('N004', '2002-02-15', 'D003');

-- Bảng CTPNHAP
INSERT INTO CTPNHAP (SOPN, MaVTu, SINhap, DgNhap) VALUES
('N001', 'DD01', 8, 2500000), ('N001', 'DD02', 10, 3500000),
('N002', 'DD01', 2, 2500000), ('N002', 'DD02', 5, 3500000),
('N003', 'VD02', 30, 2500000), ('N004', 'TV14', 5, 2500000),
('N004', 'TV29', 12, 3500000);

-- Bảng PXUAT
INSERT INTO PXUAT (SOPX, Ngayxuat, TenKH) VALUES
('XOO', '2008-05-20', N'Trần Thành Trung'),
('X001', '2002-01-17', N'Trần Phương Hoa'),
('X002', '2002-01-25', N'Đào Minh Chung'),
('X003', '2002-01-31', N'Nguyễn Thúy Hạnh'),
('X005', '2008-05-20', N'Hàn Ngọc Đức');

-- Bảng CTPXUAT
INSERT INTO CTPXUAT (SOPX, MaVTu, SIXuat, DgXuat) VALUES
('X001', 'DD01', 2, 3500000), ('X002', 'DD01', 1, 3500000),
('X002', 'DD02', 5, 4900000), ('X003', 'DD01', 3, 3500000),
('X003', 'DD02', 2, 4900000), ('X003', 'VD02', 10, 3250000);
GO

-- Tạo file backup cho CSDL
BACKUP DATABASE QLBanhang
TO DISK = 'D:\\QLBanhang.bak';

-- Xóa CSDL QLBanhang
USE master;
GO
DROP DATABASE QLBanhang;
GO

-- Phục hồi CSDL từ file backup
RESTORE DATABASE QLBanhang
FROM DISK = 'D:\\QLBanhang.bak';