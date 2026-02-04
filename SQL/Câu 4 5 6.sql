--Cau 4
CREATE VIEW v_ChiTietDonHang AS
SELECT
    OD.IDDonHang,
    OD.IDSanPham,
    SP.TenSP AS TenSanPham,
    LH.TenLoaiHang,
    NCC.TenCongTy AS TenCongTyCungCap,
    OD.SoLuong AS SoLuongBan,
    SP.DonGiaNhap,
    OD.DonGiaBan,
    OD.TyLeGiamGia,

    -- ThanhTienBan = SoLuong * DonGiaBan * (1 - TyLeGiamGia)
    (OD.SoLuong * OD.DonGiaBan * (1 - COALESCE(OD.TyLeGiamGia, 0))) AS ThanhTienBan,

    -- TienLai = ThanhTienBan - (SoLuong * DonGiaNhap)
    (OD.SoLuong * OD.DonGiaBan * (1 - COALESCE(OD.TyLeGiamGia, 0))) - (OD.SoLuong * SP.DonGiaNhap) AS TienLai

FROM
    SP_DonHang AS OD
INNER JOIN
    SanPham AS SP ON OD.IDSanPham = SP.IDSanPham
INNER JOIN
    LoaiHang AS LH ON SP.IDLoaiHang = LH.IDLoaiHang
INNER JOIN
    NhaCungCap AS NCC ON SP.IDNhaCungCap = NCC.IDNhaCungCap;
GO
--Câu 5
CREATE VIEW v_TongKetDonHang AS
SELECT
    DH.IDDonHang,
    DH.IDKhachHang,
    KH.HoTen AS HoTenKhachHang,
    KH.GioiTinh AS GioiTinhKhachHang,
    DH.IDNhanVien,
    NV.HoTen AS HoTenNhanVien,
    DH.NgayDatHang,
    DH.NgayGiaoHang,
    DH.NgayYeuCauChuyen,
    DH.IDCtyGiaoHang,
    CTY.TenCongTy AS TenCongTyGiaoHang,

    -- Số mặt hàng: Đếm số dòng (IDSanPham khác nhau) trong mỗi đơn hàng
    COUNT(CT.IDSanPham) AS SoMatHang,

    -- TongTienHoaDon: Tổng của cột ThanhTienBan từ v_ChiTietDonHang
    SUM(CT.ThanhTienBan) AS TongTienHoaDon,

    -- TongTienLai: Tổng của cột TienLai từ v_ChiTietDonHang
    SUM(CT.TienLai) AS TongTienLai

FROM
    DonHang AS DH
INNER JOIN
    KhachHang AS KH ON DH.IDKhachHang = KH.IDKhachHang
INNER JOIN
    NhanVien AS NV ON DH.IDNhanVien = NV.IDNhanVien
LEFT JOIN
    CtyGiaoHang AS CTY ON DH.IDCtyGiaoHang = CTY.IDCty
LEFT JOIN
    v_ChiTietDonHang AS CT ON DH.IDDonHang = CT.IDDonHang
GROUP BY
    DH.IDDonHang, DH.IDKhachHang, KH.HoTen, KH.GioiTinh, DH.IDNhanVien, NV.HoTen,
    DH.NgayDatHang, DH.NgayGiaoHang, DH.NgayYeuCauChuyen, DH.IDCtyGiaoHang, CTY.TenCongTy;
GO
--Cau 6
--a Tìm nhân viên bán được nhiều đơn hàng nhất
SELECT TOP 1
    IDNhanVien,
    HoTenNhanVien,
    COUNT(IDDonHang) AS SoDonHangBanDuoc
FROM
    v_TongKetDonHang
GROUP BY
    IDNhanVien, HoTenNhanVien
ORDER BY
    SoDonHangBanDuoc DESC
GO
--b Đưa ra danh sách các nhân viên theo thứ tự giảm dần của số đơn hàng bán được
SELECT
    IDNhanVien,
    HoTenNhanVien,
    COUNT(IDDonHang) AS SoDonHangBanDuoc
FROM
    v_TongKetDonHang
GROUP BY
    IDNhanVien, HoTenNhanVien
ORDER BY
    SoDonHangBanDuoc DESC;
GO
--c Đưa ra danh sách các công ty đã từng giao hàng trễ
SELECT DISTINCT
    IDCtyGiaoHang,
    TenCongTyGiaoHang
FROM
    v_TongKetDonHang
WHERE
    NgayGiaoHang > NgayYeuCauChuyen
    AND NgayGiaoHang IS NOT NULL
    AND NgayYeuCauChuyen IS NOT NULL;
GO
--d Đưa ra danh sách các mặt hàng theo thứ tự giảm dần tổng số tiền lãi thu được
SELECT
    IDSanPham,
    TenSanPham,
    SUM(TienLai) AS TongTienLaiThuDuoc
FROM
    v_ChiTietDonHang
GROUP BY
    IDSanPham, TenSanPham
ORDER BY
    TongTienLaiThuDuoc DESC;
GO
--e Đưa ra loại mặt hàng có số lượng bán được nhiều nhất
SELECT TOP 1
    LH.IDLoaiHang,
    LH.TenLoaiHang,
    SUM(OD.SoLuong) AS TongSoLuongBan
FROM
    SP_DonHang AS OD
INNER JOIN
    SanPham AS SP ON OD.IDSanPham = SP.IDSanPham
INNER JOIN
    LoaiHang AS LH ON SP.IDLoaiHang = LH.IDLoaiHang
GROUP BY
    LH.IDLoaiHang, LH.TenLoaiHang
ORDER BY
    TongSoLuongBan DESC
GO
-- Xem 4 5
SELECT * FROM v_ChiTietDonHang;
GO
SELECT * FROM v_TongKetDonHang