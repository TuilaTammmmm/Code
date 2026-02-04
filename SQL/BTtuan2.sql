-- Đào Duy Tâm-B23DVCN169

-- Câu 1
-- a Hiển thị danh sách các vật tư trong bảng VATTU (sắp xếp theo thứ tự tên vật tư giảm dần)
SELECT *
FROM VATTU
ORDER BY TenVTu DESC;
GO

-- b Hiển thị danh sách các thông tin trong bảng CTPNHAP, có bổ sung thêm cột thành tiền biết rằng Thành tiền = SlNhap*DgNhap
SELECT SOPN, MaVTu, SINhap, DgNhap, (SINhap * DgNhap) AS ThanhTien
FROM CTPNHAP;
GO

-- c Sử dụng mệnh đề COMPUTE BY để hiển thị các thông tin: Mã vật tư, số lượng nhập, đơn giá nhập trong bảng CTPNHAP và 
-- có bổ sung dòng thống kê: Tổng số lượng nhập, giá nhập thấp nhất, giá nhập cao nhất cho từng vật tư.

-- Không dùng được COMPUTE BY vì em đang dùng SQL Server Management Studio 21
SELECT
    MaVTu,                           
    SUM(SINhap) AS TongSoLuongNhap,  
    MIN(DgNhap) AS GiaNhapThapNhat,   
    MAX(DgNhap) AS GiaNhapCaoNhat     
FROM
    CTPNHAP
GROUP BY
    MaVTu;
GO

-- d Hiển thị danh sách các nhà cung cấp (mã nhà cung cấp và tên nhà cung cấp) đã từng được đặt hàng (dữ liệu không trùng lặp)
SELECT DISTINCT T1.MaNCC, T1.TenNCC
FROM NCC AS T1
INNER JOIN DONDH AS T2 ON T1.MaNCC = T2.MaNCC;
GO

-- e Làm tương tự ý d cho các nhà cung cấp có hàng đã được xuất (hoặc nhập)
SELECT DISTINCT T1.MaNCC, T1.TenNCC
FROM NCC AS T1
INNER JOIN DONDH AS T2 ON T1.MaNCC = T2.MaNCC
INNER JOIN PNHAP AS T3 ON T2.SODH = T3.SODH;
GO

-- f Hiển thị danh sách các đơn đặt hàng gần đây nhất trong bảng DONDH
SELECT *
FROM DONDH
ORDER BY NgayDH DESC;
GO

-- g Hiển thị danh sách các phiếu xuất hàng gồm các cột: số phiếu xuất và tổng trị giá, dữ liệu được sắp xếp theo cột tổng trị giá giảm dần
SELECT SOPX, SUM(SIXuat * DgXuat) AS TongTriGia
FROM CTPXUAT
GROUP BY SOPX
ORDER BY TongTriGia DESC;
GO

-- h Hiển thị danh sách các vật tư có trong bảng đơn đặt hàng cùng với tổng số lượng nhập/xuất tương ứng
SELECT
    vt.MaVTu,
    vt.TenVTu,
    ISNULL(nhap.TongSLNhap, 0) AS TongSoLuongNhap,
    ISNULL(xuat.TongSLXuat, 0) AS TongSoLuongXuat
FROM VATTU vt
LEFT JOIN (
    SELECT MaVTu, SUM(SINhap) AS TongSLNhap
    FROM CTPNHAP
    GROUP BY MaVTu
) AS nhap ON vt.MaVTu = nhap.MaVTu
LEFT JOIN (
    SELECT MaVTu, SUM(SIXuat) AS TongSLXuat
    FROM CTPXUAT
    GROUP BY MaVTu
) AS xuat ON vt.MaVTu = xuat.MaVTu
WHERE vt.MaVTu IN (SELECT DISTINCT MaVTu FROM CTDONDH);
GO

-- i Làm tương tự ý h song chỉ chọn ra 2 bản ghi thứ 2 và thứ 3 trong kết quả tìm được
WITH TongHop AS (
    SELECT
        vt.MaVTu,
        vt.TenVTu,
        ISNULL(nhap.TongSLNhap, 0) AS TongSoLuongNhap,
        ISNULL(xuat.TongSLXuat, 0) AS TongSoLuongXuat,
        ROW_NUMBER() OVER (ORDER BY vt.MaVTu) as rn
    FROM VATTU vt
    LEFT JOIN (
        SELECT MaVTu, SUM(SINhap) AS TongSLNhap FROM CTPNHAP GROUP BY MaVTu
    ) AS nhap ON vt.MaVTu = nhap.MaVTu
    LEFT JOIN (
        SELECT MaVTu, SUM(SIXuat) AS TongSLXuat FROM CTPXUAT GROUP BY MaVTu
    ) AS xuat ON vt.MaVTu = xuat.MaVTu
    WHERE vt.MaVTu IN (SELECT DISTINCT MaVTu FROM CTDONDH)
)
SELECT MaVTu, TenVTu, TongSoLuongNhap, TongSoLuongXuat
FROM TongHop
WHERE rn BETWEEN 2 AND 3;
GO

-- Câu 2
-- a) Xóa các đơn đặt hàng trong bảng DONDH mà ngày đặt hàng là 15/01/2002
DELETE FROM CTPNHAP WHERE SOPN IN (SELECT SOPN FROM PNHAP WHERE SODH IN (SELECT SODH FROM DONDH WHERE NgayDH = '2002-01-15'));
DELETE FROM PNHAP WHERE SODH IN (SELECT SODH FROM DONDH WHERE NgayDH = '2002-01-15');
DELETE FROM CTDONDH WHERE SODH IN (SELECT SODH FROM DONDH WHERE NgayDH = '2002-01-15');
DELETE FROM DONDH WHERE NgayDH = '2002-01-15';
GO

-- b) Sử dụng Insert into để chèn lại các dòng dữ liệu đã bị xóa ở ý a
INSERT INTO DONDH (SODH, NgayDH, MaNCC) VALUES ('D001', '2002-01-15', 'C03');
INSERT INTO CTDONDH (SODH, MaVTu, SIDat) VALUES ('D001', 'DD01', 10), ('D001', 'DD02', 15);
INSERT INTO PNHAP (SOPN, Ngaynhap, SODH) VALUES ('N001', '2002-01-17', 'D001'), ('N002', '2002-01-20', 'D001');
INSERT INTO CTPNHAP (SOPN, MaVTu, SINhap, DgNhap) VALUES
('N001', 'DD01', 8, 2500000),
('N001', 'DD02', 10, 3500000),
('N002', 'DD01', 2, 2500000),
('N002', 'DD02', 5, 3500000);
GO

-- c Cập nhật lại giá xuất cho các vật tư trong bảng CTPXUAT mà giá xuất hiện
-- thời <4000000, giá trị cập nhật mới bằng bình phương của giá trị cũ
UPDATE CTPXUAT
SET DgXuat = DgXuat * DgXuat
WHERE DgXuat < 4000000;
GO

-- d Sử dụng hàm Datename kiểm tra xem trong số các đơn đặt hàng đã có, có tồn
-- tại đơn đặt hàng nào được lập vào ngày chủ nhật hay không, nếu có, in ra chi tiết
-- đơn hàng (số đơn hàng, mã vật tư, số lượng đặt hàng)
SET DATEFIRST 1;
SELECT T1.SODH, T2.MaVTu, T2.SIDat, T1.NgayDH
FROM DONDH AS T1
JOIN CTDONDH AS T2 ON T1.SODH = T2.SODH
WHERE DATENAME(weekday, T1.NgayDH) = 'Sunday';
GO

-- e Đếm số đơn đặt hàng cho mã vật tư DD01, hiển thị các thông tin tương ứng, trong đó ngày đặt hàng được hiển thị theo định dạng dd/mm/yy
SELECT
    T1.SODH,
    FORMAT(T1.NgayDH, 'dd/MM/yy') AS NgayDatHang,
    T2.MaVTu,
    T2.SIDat,
    (SELECT COUNT(DISTINCT SODH) FROM CTDONDH WHERE MaVTu = 'DD01') AS TongSoDonHangChuaDD01
FROM DONDH AS T1
JOIN CTDONDH AS T2 ON T1.SODH = T2.SODH
WHERE T2.MaVTu = 'DD01';
GO

-- f Xóa đi dữ liệu ở trường Số lượng đặt của một số bản ghi trong bảng CTDONDH, 
-- sau đó sử dụng hàm isnull kiểm tra và cập nhật lại giá trị = 0 cho các bản ghi đó
ALTER TABLE CTDONDH NOCHECK CONSTRAINT CK_SIDat;

UPDATE CTDONDH SET SIDat = NULL WHERE SODH = 'D001' AND MaVTu = 'DD01';
UPDATE CTDONDH SET SIDat = ISNULL(SIDat, 0) WHERE SIDat IS NULL;

ALTER TABLE CTDONDH CHECK CONSTRAINT CK_SIDat;
GO
