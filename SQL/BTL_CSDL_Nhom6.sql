USE master
GO
CREATE DATABASE BTL_QUANLYPHONGKHAM
GO
USE BTL_QUANLYPHONGKHAM
GO
-- Tạo Schema
CREATE SCHEMA NhanVien
GO
CREATE SCHEMA ThanhToan
GO
CREATE SCHEMA BenhNhan
GO
CREATE SCHEMA Thuoc
GO
CREATE SCHEMA DichVu
GO
CREATE SCHEMA TacVu
GO
--I. Tạo bảng
-- 1. Bảng Bệnh Nhân
CREATE TABLE BenhNhan.BenhNhan (
    MaBenhNhan VARCHAR(10) PRIMARY KEY,
    HoTen NVARCHAR(100) NOT NULL,
    NgaySinh DATE,
    GioiTinh NVARCHAR(10),
    DiaChi NVARCHAR(255),
    SoDienThoai VARCHAR(15) UNIQUE,
    ThongTinBaoHiem VARCHAR(50)
);

-- 2. Bảng Nhân Viên
CREATE TABLE NhanVien.NhanVien (
    MaNhanVien VARCHAR(10) PRIMARY KEY,
    HoTen NVARCHAR(100) NOT NULL,
    SoDienThoai VARCHAR(15) UNIQUE,
    ChucVu NVARCHAR(50) NOT NULL,
    MatKhau VARCHAR(100) NOT NULL
);

-- 3. Bảng Dịch Vụ
CREATE TABLE DichVu.DichVu (
    MaDichVu VARCHAR(10) PRIMARY KEY,
    TenDichVu NVARCHAR(100) NOT NULL,
    MoTa NVARCHAR(255),
    DonGia DECIMAL(18, 2) NOT NULL CHECK (DonGia >= 0)
);

-- 4. Bảng Thuốc
CREATE TABLE Thuoc.Thuoc (
    MaThuoc VARCHAR(10) PRIMARY KEY,
    TenThuoc NVARCHAR(100) NOT NULL,
    DonViTinh NVARCHAR(20) NOT NULL,
    DonGia DECIMAL(18, 2) NOT NULL CHECK (DonGia >= 0),
    SoLuongTon INT NOT NULL CHECK (SoLuongTon >= 0)
);

-- 5. Bảng Bác Sĩ
CREATE TABLE NhanVien.BacSi (
    MaBacSi VARCHAR(10) PRIMARY KEY,
    ChuyenKhoa NVARCHAR(100) NOT NULL
);

-- 6. Bảng Lượt Khám
CREATE TABLE TacVu.LuotKham (
    MaLuotKham VARCHAR(10) PRIMARY KEY,
    TrangThai NVARCHAR(50) NOT NULL,
    NgayKham DATETIME NOT NULL,
    MaBenhNhan VARCHAR(10),
    MaNhanVien_TiepNhan VARCHAR(10)
);

-- 7. Bảng Hồ Sơ Khám
CREATE TABLE TacVu.HoSoKham (
    MaHoSo VARCHAR(10) PRIMARY KEY,
    LyDoKham NVARCHAR(255),
    ChanDoan NVARCHAR(255) NOT NULL,
    GhiChu NVARCHAR(500),
    MaLuotKham VARCHAR(10) UNIQUE,
    MaBacSi VARCHAR(10)
);

-- 8. Bảng Thanh Toán
CREATE TABLE ThanhToan.ThanhToan (
    MaThanhToan VARCHAR(10) PRIMARY KEY,
    HinhThucThanhToan NVARCHAR(50) NOT NULL,
    NgayThanhToan DATETIME NOT NULL,
    TongTienDichVu DECIMAL(18, 2) CHECK (TongTienDichVu >= 0),
    TongTienThuoc DECIMAL(18, 2) CHECK (TongTienThuoc >= 0),
    GiamTru DECIMAL(18, 2) CHECK (GiamTru >= 0),
    GhiChu NVARCHAR(500),
    MaLuotKham VARCHAR(10) UNIQUE,
    MaNhanVien_ThuNgan VARCHAR(10),
);

-- 9. Bảng Chi Tiết Dịch Vụ
CREATE TABLE DichVu.ChiTietDichVu (
    MaHoSo VARCHAR(10) NOT NULL,
    MaDichVu VARCHAR(10) NOT NULL,
    SoLuong INT NOT NULL CHECK (SoLuong > 0),
    KetQua NVARCHAR(500),
    PRIMARY KEY (MaHoSo, MaDichVu)
);

-- 10. Bảng Chi Tiết Đơn Thuốc
CREATE TABLE Thuoc.ChiTietDonThuoc (
    MaHoSo VARCHAR(10) NOT NULL,
    MaThuoc VARCHAR(10) NOT NULL,
    SoLuong INT NOT NULL CHECK (SoLuong > 0),
    LieuDung NVARCHAR(100) NOT NULL,
    PRIMARY KEY (MaHoSo, MaThuoc)
);


--II. Thêm khóa ngoại
-- 1. Khóa ngoại cho bảng Bác Sĩ
ALTER TABLE NhanVien.BacSi
ADD CONSTRAINT FK_BacSi_NhanVien
FOREIGN KEY (MaBacSi) REFERENCES NhanVien.NhanVien(MaNhanVien);

-- 2. Khóa ngoại cho bảng Lượt Khám
ALTER TABLE TacVu.LuotKham
ADD CONSTRAINT FK_LuotKham_BenhNhan
FOREIGN KEY (MaBenhNhan) REFERENCES BenhNhan.BenhNhan(MaBenhNhan);

ALTER TABLE TacVu.LuotKham
ADD CONSTRAINT FK_LuotKham_NhanVien
FOREIGN KEY (MaNhanVien_TiepNhan) REFERENCES NhanVien.NhanVien(MaNhanVien);

-- 3. Khóa ngoại cho bảng Hồ Sơ Khám
ALTER TABLE TacVu.HoSoKham
ADD CONSTRAINT FK_HoSoKham_LuotKham
FOREIGN KEY (MaLuotKham) REFERENCES TacVu.LuotKham(MaLuotKham);

ALTER TABLE TacVu.HoSoKham
ADD CONSTRAINT FK_HoSoKham_BacSi
FOREIGN KEY (MaBacSi) REFERENCES NhanVien.BacSi(MaBacSi);

-- 4. Khóa ngoại cho bảng Thanh Toán
ALTER TABLE ThanhToan.ThanhToan
ADD CONSTRAINT FK_ThanhToan_LuotKham
FOREIGN KEY (MaLuotKham) REFERENCES TacVu.LuotKham(MaLuotKham);

ALTER TABLE ThanhToan.ThanhToan
ADD CONSTRAINT FK_ThanhToan_NhanVien
FOREIGN KEY (MaNhanVien_ThuNgan) REFERENCES NhanVien.NhanVien(MaNhanVien);

-- 5. Khóa ngoại cho bảng Chi Tiết Dịch Vụ
ALTER TABLE DichVu.ChiTietDichVu
ADD CONSTRAINT FK_ChiTietDichVu_HoSo
FOREIGN KEY (MaHoSo) REFERENCES TacVu.HoSoKham(MaHoSo);

ALTER TABLE DichVu.ChiTietDichVu
ADD CONSTRAINT FK_ChiTietDichVu_DichVu
FOREIGN KEY (MaDichVu) REFERENCES DichVu.DichVu(MaDichVu);

-- 6. Khóa ngoại cho bảng Chi Tiết Đơn Thuốc
ALTER TABLE Thuoc.ChiTietDonThuoc
ADD CONSTRAINT FK_ChiTietDonThuoc_HoSo
FOREIGN KEY (MaHoSo) REFERENCES TacVu.HoSoKham(MaHoSo);

ALTER TABLE Thuoc.ChiTietDonThuoc
ADD CONSTRAINT FK_ChiTietDonThuoc_Thuoc
FOREIGN KEY (MaThuoc) REFERENCES Thuoc.Thuoc(MaThuoc);


--III. INSERT dữ liệu vào từng bảng
-- 1. Bệnh nhân
INSERT INTO BenhNhan.BenhNhan (MaBenhNhan, HoTen, NgaySinh, GioiTinh, DiaChi, SoDienThoai, ThongTinBaoHiem) VALUES
('BN001', N'Nguyễn Văn An', '1985-04-12', N'Nam', N'123 Giải Phóng, Hà Nội', '0912345678', 'HN0123456789'),
('BN002', N'Trần Thị Bình', '1992-09-20', N'Nữ', N'456 Lê Lợi, TP. HCM', '0987654321', NULL),
('BN003', N'Lê Văn Cường', '1970-01-30', N'Nam', N'789 Đà Nẵng', '0905123456', 'DN0112233445'),
('BN004', N'Phạm Thị Dung', '2001-07-15', N'Nữ', N'101 Cần Thơ', '0977889900', NULL),
('BN005', N'Hoàng Văn Em', '1998-11-05', N'Nam', N'222 Hải Phòng', '0933445566', 'HP0101010101');
-- 2. Nhân viên
INSERT INTO NhanVien.NhanVien (MaNhanVien, HoTen, SoDienThoai, ChucVu, MatKhau) VALUES
('NV001', N'Trần Văn Dũng', '0901112222', N'Bác Sĩ', 'bacsi001'),
('NV002', N'Nguyễn Thị Lan', '0902223333', N'Bác Sĩ', 'bacsi002'),
('NV003', N'Lê Thị Hà', '0903334444', N'Lễ Tân', 'letan001'),
('NV004', N'Phạm Văn Hùng', '0904445555', N'Thu Ngân', 'thungan001'),
('NV005', N'Đặng Văn Kiên', '0905556666', N'Quản Lý', 'quanly001');
-- 3. Bác sĩ
INSERT INTO NhanVien.BacSi (MaBacSi, ChuyenKhoa) VALUES
('NV001', N'Chuyên Khoa Nội Tổng Hợp'),
('NV002', N'Chuyên Khoa Da Liễu');
-- 4. Dịch vụ
INSERT INTO DichVu.DichVu (MaDichVu, TenDichVu, MoTa, DonGia) VALUES
('DV001', N'Khám lâm sàng tổng quát', N'Bác sĩ khám và tư vấn', 150000.00),
('DV002', N'Xét nghiệm công thức máu', N'Phân tích 18 chỉ số máu', 120000.00),
('DV003', N'Siêu âm ổ bụng', N'Siêu âm tổng quát ổ bụng', 200000.00),
('DV004', N'Nội soi tai mũi họng', N'Kiểm tra tai mũi họng bằng camera', 250000.00),
('DV005', N'Đo điện tâm đồ (ECG)', N'Kiểm tra chức năng tim', 180000.00);
-- 5. Thuốc
INSERT INTO Thuoc.Thuoc (MaThuoc, TenThuoc, DonViTinh, DonGia, SoLuongTon) VALUES
('T001', N'Paracetamol 500mg', N'Viên', 1000.00, 500),
('T002', N'Amoxicillin 500mg', N'Viên', 2500.00, 300),
('T003', N'Berberin 100mg', N'Viên', 500.00, 1000),
('T004', N'Clorpheniramin 4mg', N'Viên', 800.00, 400),
('T005', N'Oresol (Gói)', N'Gói', 3000.00, 200);
-- 6. Lượt khám
INSERT INTO TacVu.LuotKham (MaLuotKham, TrangThai, NgayKham, MaBenhNhan, MaNhanVien_TiepNhan) VALUES
('LK001', N'Đã hoàn tất', '2025-11-01 08:30:00', 'BN001', 'NV003'),
('LK002', N'Đã hoàn tất', '2025-11-01 09:15:00', 'BN002', 'NV003'),
('LK003', N'Đã hoàn tất', '2025-11-02 10:00:00', 'BN003', 'NV003'),
('LK004', N'Đã hoàn tất', '2025-11-02 11:00:00', 'BN001', 'NV003'),
('LK005', N'Đã hoàn tất', '2025-11-02 14:30:00', 'BN004', 'NV003');
-- 7. Hồ sơ khám
INSERT INTO TacVu.HoSoKham (MaHoSo, LyDoKham, ChanDoan, GhiChu, MaLuotKham, MaBacSi) VALUES
('HS001', N'Ho, sốt, đau họng', N'Viêm họng cấp', N'Uống thuốc 5 ngày, tái khám nếu không đỡ', 'LK001', 'NV001'),
('HS002', N'Nổi mẩn đỏ, ngứa', N'Viêm da dị ứng', N'Tránh tiếp xúc dị nguyên, bôi thuốc tại chỗ', 'LK002', 'NV002'),
('HS003', N'Đau bụng, tiêu chảy', N'Rối loạn tiêu hóa', N'Uống Oresol bù nước, ăn uống cẩn thận', 'LK003', 'NV001'),
('HS004', N'Tái khám viêm họng', N'Đã ổn định', N'Ngừng thuốc, giữ ấm cổ', 'LK004', 'NV001'),
('HS005', N'Khám da định kỳ', N'Mụn trứng cá', N'Vệ sinh da sạch sẽ, dùng thuốc bôi', 'LK005', 'NV002');
-- 8. Chi tiết dịch vụ
INSERT INTO DichVu.ChiTietDichVu (MaHoSo, MaDichVu, SoLuong, KetQua) VALUES
('HS001', 'DV001', 1, N'Họng sưng đỏ, amidan không sưng'),
('HS001', 'DV004', 1, N'Niêm mạc họng phù nề'),
('HS002', 'DV001', 1, N'Da có nhiều nốt mẩn đỏ ở tay'),
('HS003', 'DV001', 1, N'Bụng mềm, ấn đau nhẹ thượng vị'),
('HS003', 'DV003', 1, N'Gan, thận bình thường, không thấy bất thường'),
('HS004', 'DV001', 1, N'Họng hết sưng đỏ'),
('HS005', 'DV001', 1, N'Da mặt có mụn viêm nhẹ');
-- 9. Chi tiết đơn thuốc
INSERT INTO Thuoc.ChiTietDonThuoc (MaHoSo, MaThuoc, SoLuong, LieuDung) VALUES
('HS001', 'T001', 10, N'Ngày uống 2 lần, mỗi lần 1 viên sau ăn'),
('HS001', 'T002', 14, N'Ngày uống 2 lần, mỗi lần 1 viên sau ăn'),
('HS002', 'T004', 10, N'Ngày uống 2 lần, mỗi lần 1 viên khi ngứa'),
('HS003', 'T003', 20, N'Ngày uống 4 viên, chia 2 lần'),
('HS003', 'T005', 3, N'Pha 1 gói với 1 lít nước, uống cả ngày'),
('HS005', 'T002', 10, N'Thuốc bôi, bôi ngày 1 lần buổi tối');
-- 10. Thanh toán
INSERT INTO ThanhToan.ThanhToan (MaThanhToan, HinhThucThanhToan, NgayThanhToan, TongTienDichVu, TongTienThuoc, GiamTru, GhiChu, MaLuotKham, MaNhanVien_ThuNgan) VALUES
('TT001', N'Tiền mặt', '2025-11-01 09:00:00', 400000.00, 45000.00, 0.00, NULL, 'LK001', 'NV004'),
('TT002', N'Chuyển khoản', '2025-11-01 09:45:00', 150000.00, 8000.00, 0.00, NULL, 'LK002', 'NV004'),
('TT003', N'Tiền mặt', '2025-11-02 10:30:00', 350000.00, 19000.00, 0.00, NULL, 'LK003', 'NV004'),
('TT004', N'Tiền mặt', '2025-11-02 11:20:00', 150000.00, 0.00, 0.00, N'Tái khám', 'LK004', 'NV004'),
('TT005', N'Chuyển khoản', '2025-11-02 15:00:00', 150000.00, 25000.00, 0.00, NULL, 'LK005', 'NV004');


--IV. Truy vấn nâng cao , index, view, stored procedure
-- 1. Chức năng thêm mới dữ liệu
-- a. Thêm một bệnh nhân mới vào hệ thống
INSERT INTO BenhNhan.BenhNhan (MaBenhNhan, HoTen, NgaySinh, GioiTinh, DiaChi, SoDienThoai, ThongTinBaoHiem)
VALUES ('BN006', N'Lý Thị Mai', '1995-02-18', N'Nữ', N'55 Hùng Vương, Huế', '0915667788', NULL);
-- b. Thêm một loại thuốc mới vào kho
INSERT INTO Thuoc.Thuoc (MaThuoc, TenThuoc, DonViTinh, DonGia, SoLuongTon)
VALUES ('T006', N'Aspirin 81mg', N'Viên', 500.00, 1000);

-- 2. Chức năng sửa đổi dữ liệu
-- a. Sửa địa chỉ cho bệnh nhân có mã BN004
UPDATE BenhNhan.BenhNhan
SET DiaChi = N'12 Lý Thường Kiệt, Hà Nội'
WHERE MaBenhNhan = 'BN004';

-- b. Sửa số điện thoại cho nhân viên có mã NV003
UPDATE NhanVien.NhanVien
SET SoDienThoai = '0903334455'
WHERE MaNhanVien = 'NV003';

-- 3. Chức năng xoá dữ liệu
-- Xóa một loại thuốc (T005) khỏi hệ thống
-- Bước 1: Xóa khỏi các đơn thuốc đã kê
DELETE FROM Thuoc.ChiTietDonThuoc
WHERE MaThuoc = 'T005' AND MaHoSo = 'HS003';
-- Bước 2: Xóa thuốc khỏi danh mục
DELETE FROM Thuoc.Thuoc
WHERE MaThuoc = 'T005';

-- 4. Chức năng tìm kiếm theo tiêu chí
-- a. Danh sách các bác sĩ thuộc chuyên khoa Da Liễu
SELECT 
    NV.MaNhanVien, 
    NV.HoTen, 
    NV.SoDienThoai, 
    BS.ChuyenKhoa
FROM NhanVien.NhanVien NV
JOIN NhanVien.BacSi BS ON NV.MaNhanVien = BS.MaBacSi
WHERE BS.ChuyenKhoa = N'Chuyên Khoa Da Liễu';
-- b. Danh sách bệnh nhân đã được khám bởi bác sĩ NV001 (Trần Văn Dũng)
SELECT DISTINCT 
    BN.MaBenhNhan, 
    BN.HoTen, 
    BN.SoDienThoai
FROM BenhNhan.BenhNhan BN
JOIN TacVu.LuotKham LK ON BN.MaBenhNhan = LK.MaBenhNhan
JOIN TacVu.HoSoKham HS ON LK.MaLuotKham = HS.MaLuotKham
WHERE HS.MaBacSi = 'NV001';
-- c. Tìm các lượt khám trong ngày 2025-11-01
SELECT 
    LK.MaLuotKham, 
    BN.HoTen, 
    LK.TrangThai
FROM TacVu.LuotKham LK
JOIN BenhNhan.BenhNhan BN ON LK.MaBenhNhan = BN.MaBenhNhan
WHERE CONVERT(DATE, LK.NgayKham) = '2025-11-01';

-- 5. Chức năng tổng hợp dữ liệu
-- a. Tính tổng số tiền đã chi tiêu của mỗi bệnh nhân
SELECT
    BN.HoTen,
    SUM(TT.TongTienDichVu + TT.TongTienThuoc - TT.GiamTru) AS TongChiTieu
FROM ThanhToan.ThanhToan TT
JOIN TacVu.LuotKham LK ON TT.MaLuotKham = LK.MaLuotKham
JOIN BenhNhan.BenhNhan BN ON LK.MaBenhNhan = BN.MaBenhNhan
GROUP BY BN.MaBenhNhan, BN.HoTen;
-- b. Thống kê số lượng lượt khám do mỗi bác sĩ thực hiện
SELECT
    NV.HoTen AS TenBacSi,
    COUNT(HS.MaHoSo) AS TongSoLuotKham
FROM TacVu.HoSoKham HS
JOIN NhanVien.BacSi BS ON HS.MaBacSi = BS.MaBacSi
JOIN NhanVien.NhanVien NV ON BS.MaBacSi = NV.MaNhanVien
GROUP BY NV.MaNhanVien, NV.HoTen
ORDER BY TongSoLuotKham DESC;
-- c. Tìm bệnh nhân có hóa đơn thanh toán cao nhất
SELECT
    BN.HoTen,
    (TT.TongTienDichVu + TT.TongTienThuoc - TT.GiamTru) AS TongHoaDon
FROM ThanhToan.ThanhToan TT
JOIN TacVu.LuotKham LK ON TT.MaLuotKham = LK.MaLuotKham
JOIN BenhNhan.BenhNhan BN ON LK.MaBenhNhan = BN.MaBenhNhan
WHERE (TT.TongTienDichVu + TT.TongTienThuoc - TT.GiamTru) = (
    SELECT MAX(TongTienDichVu + TongTienThuoc - GiamTru)
    FROM ThanhToan.ThanhToan
);
-- d. Thống kê doanh thu theo từng dịch vụ
SELECT
    DV.TenDichVu,
    SUM(DV.DonGia * CT.SoLuong) AS TongDoanhThu
FROM DichVu.ChiTietDichVu CT
JOIN DichVu.DichVu DV ON CT.MaDichVu = DV.MaDichVu
GROUP BY DV.MaDichVu, DV.TenDichVu
ORDER BY TongDoanhThu DESC;
-- e. Đếm số lượng bác sĩ theo từng chuyên khoa
SELECT
    BS.ChuyenKhoa,
    COUNT(BS.MaBacSi) AS SoLuongBacSi
FROM NhanVien.BacSi BS
GROUP BY BS.ChuyenKhoa;
GO

--6 Tạo View
CREATE VIEW vw_ThongTinKhamBenhChiTiet
AS
SELECT 
    LK.MaLuotKham,
    LK.NgayKham,
    BN.HoTen AS TenBenhNhan,
    BN.NgaySinh,
    BN.GioiTinh,
    NV.HoTen AS TenBacSi,
    BS.ChuyenKhoa,
    HS.ChanDoan,
    HS.LyDoKham,
    HS.GhiChu AS GhiChuBacSi
FROM 
    TacVu.LuotKham AS LK
JOIN 
    BenhNhan.BenhNhan AS BN ON LK.MaBenhNhan = BN.MaBenhNhan
JOIN 
    TacVu.HoSoKham AS HS ON LK.MaLuotKham = HS.MaLuotKham
JOIN 
    NhanVien.BacSi AS BS ON HS.MaBacSi = BS.MaBacSi
JOIN 
    NhanVien.NhanVien AS NV ON BS.MaBacSi = NV.MaNhanVien;
GO

--7 Tạo Index
CREATE NONCLUSTERED INDEX IX_BenhNhan_HoTen
ON BenhNhan.BenhNhan(HoTen);
GO
CREATE NONCLUSTERED INDEX IX_LuotKham_MaBenhNhan
ON TacVu.LuotKham(MaBenhNhan);
GO
CREATE NONCLUSTERED INDEX IX_HoSoKham_MaBacSi
ON TacVu.HoSoKham(MaBacSi);
GO
--8 Tạo Stored Procedure
CREATE PROCEDURE sp_TimLichSuKham_TheoBenhNhan
    @MaBenhNhan VARCHAR(10)
AS
BEGIN
    SELECT 
        LK.NgayKham,
        HS.ChanDoan,
        HS.GhiChu,
        NV.HoTen AS TenBacSi
    FROM 
        LuotKham LK
    JOIN 
        HoSoKham HS ON LK.MaLuotKham = HS.MaLuotKham
    JOIN 
        BacSi BS ON HS.MaBacSi = BS.MaBacSi
    JOIN 
        NhanVien NV ON BS.MaBacSi = NV.MaNhanVien
    WHERE 
        LK.MaBenhNhan = @MaBenhNhan
    ORDER BY 
        LK.NgayKham DESC;
END;
GO

--Backup database
--BACKUP DATABASE [BTL_QUANLYPHONGKHAM]
--TO DISK = 'D:\\BTL_Nhom6_Quanlyphongkham.bak'
