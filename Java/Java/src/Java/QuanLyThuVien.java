package Java;

import java.io.*;
import java.util.*;

public class QuanLyThuVien {

    public static void main(String[] args) {
        QLTV q = new QLTV();
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("""
                                1. Nhap SP
                                2. Hien thi DS
                                3. Luu DS
                                4. Doc DS
                                5. Tim theo ma
                                6. Tim theo ten
                                7. Xoa theo ma
                                8. Sua theo ma
                                9. Sap xep theo ma
                                10. Sap xep theo ten
                                11. Sap xep theo gia
                                12. Sap xep theo ngon ngu
                                0. Thoat""");
            System.out.print("Moi chon: ");
            int chon = Integer.parseInt(sc.nextLine());
            String tenFile = "SACH.in";
            String ma;
            switch (chon) {
                case 1 -> {
                    q.nhap(sc);
                }
                case 2 -> {
                    q.hienthi();
                }
                case 3 -> {
                    q.luuFile(tenFile);
                }
                case 4 -> {
                    q.docFile(tenFile);
                }
                case 5 -> {
                    ma = sc.nextLine();
                    q.timTheoMa(ma);
                }
                case 6 -> {
                    String ten = sc.nextLine();
                    q.timTheoTen(ten);
                }
                case 7 -> {
                    ma = sc.nextLine();
                    q.xoaTheoMa(ma);
                }
                case 8 -> {
                    ma = sc.nextLine();
                    q.suaTheoMa(sc, ma);
                }
                case 9 -> {
                    q.sapXepTheoMa();
                }
                case 10 -> {
                    q.sapXepTheoTen();
                }
                case 11 -> {
                    q.sapXepTheoGia();
                }
                case 12 -> {
                    q.sapXepTheoNgonNgu();
                }
                case 0 -> {
                    System.exit(0);
                }
                default ->
                    System.out.println("De nghi nhap 0->12");
            }
        }
    }
}

class QLTV implements IChucNang {

    List<Sach> a;

    public QLTV() {
        a = new ArrayList<>();
    }

    @Override
    public void nhap(Scanner sc) {
        System.out.print("Nhap ten sach: ");
        String ten = sc.nextLine();
        System.out.print("Nhap nha xuat ban: ");
        String nhaxuatban = sc.nextLine();
        System.out.print("Nhap gia: ");
        double gia = Double.parseDouble(sc.nextLine());
        System.out.print("Nhap so luong: ");
        int sl = Integer.parseInt(sc.nextLine());
        System.out.print("Nhap ngon ngu (true - Tieng Viet / false - Ngoai Ngu): ");
        boolean ngonngu = Boolean.parseBoolean(sc.nextLine());
        a.add(new Sach(ten, nhaxuatban, gia, sl, ngonngu));
    }

    @Override
    public void hienthi() {
        System.out.println("Danh Sach Sach");
        a.forEach(x->System.out.println(x));
        System.out.println("Tong:"+a.size());
    }

    @Override
    public void luuFile(String tenFile) {
        try (ObjectOutputStream o = new ObjectOutputStream(new FileOutputStream(tenFile))) {
            o.writeObject(a);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    @Override
    public void docFile(String tenFile) {
        try (ObjectInputStream o = new ObjectInputStream(new FileInputStream(tenFile))) {
            a = (List<Sach>) o.readObject();
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    private Sach timSach(String ma) {
        for (Sach s : a) {
            if (s.getMa().equalsIgnoreCase(ma)) {
                return s;
            }
        }
        return null;
    }

    @Override
    public void timTheoMa(String ma) {
        Sach s = timSach(ma);
        System.out.println("Tim thay sach: " + s);
    }

    @Override
    public void timTheoTen(String ten) {
        List<Sach> ketQua = new ArrayList<>();
        for (Sach s : a) {
            if (s.getTen().toLowerCase().contains(ten.toLowerCase())) {
                ketQua.add(s);
            }
        }
        for (Sach s : ketQua) {
            System.out.println(s);
        }
    }

    @Override
    public void xoaTheoMa(String ma) {
        Sach s = timSach(ma);
        a.remove(s);
    }

    @Override
    public void suaTheoMa(Scanner in, String ma) {
        Sach s = timSach(ma);
        System.out.print("Nhap NXB moi: ");
        s.setNhaxuatban(in.nextLine());
        System.out.print("Nhap gia moi: ");
        s.setGia(Double.parseDouble(in.nextLine()));
        System.out.print("Nhap ngon ngu moi: ");
        s.setNgonngu(Boolean.parseBoolean(in.nextLine()));
    }

    @Override
    public void sapXepTheoMa() {
        a.sort(Comparator.comparing(Sach::getMa));
    }

    @Override
    public void sapXepTheoTen() {
        a.sort((s1, s2) -> s1.getTen().compareToIgnoreCase(s2.getTen()));
    }

    @Override
    public void sapXepTheoGia() {
        a.sort(Comparator.comparing(Sach::getGia).reversed());
    }

    @Override
    public void sapXepTheoNgonNgu() {
        a.sort(Comparator.comparing(Sach::isNgonngu));
    }
}

interface IChucNang {

    void nhap(Scanner sc);

    void hienthi();

    void luuFile(String tenFile);

    void docFile(String tenFile);

    void timTheoMa(String ma);

    void timTheoTen(String ten);

    void xoaTheoMa(String ma);

    void suaTheoMa(Scanner in, String ma);

    void sapXepTheoMa();

    void sapXepTheoTen();

    void sapXepTheoGia();

    void sapXepTheoNgonNgu();
}

class Sach implements Serializable {

    private static final long serialVersionUID = 1L;
    private String ma, ten, nhaxuatban;
    private int soluong;
    private double gia;
    private boolean ngonngu;
    private static int sMa = 1;

    public Sach() {
    }

    public Sach(String ten, String nhaxuatban, double gia, int soluong, boolean ngonngu) {
        this.ma = String.format("%03d", sMa++);
        this.ten = ten;
        this.nhaxuatban = nhaxuatban;
        this.gia = gia;
        this.soluong = soluong;
        this.ngonngu = ngonngu;
    }

    public String getMa() {
        return ma;
    }

    public void setMa(String ma) {
        this.ma = ma;
    }

    public String getTen() {
        return ten;
    }

    public void setTen(String ten) {
        this.ten = ten;
    }

    public String getNhaxuatban() {
        return nhaxuatban;
    }

    public void setNhaxuatban(String nhaxuatban) {
        this.nhaxuatban = nhaxuatban;
    }

    public int getSoluong() {
        return soluong;
    }

    public void setSoluong(int soluong) {
        this.soluong = soluong;
    }

    public double getGia() {
        return gia;
    }

    public void setGia(double gia) {
        this.gia = gia;
    }

    public boolean isNgonngu() {
        return ngonngu;
    }

    public void setNgonngu(boolean ngonngu) {
        this.ngonngu = ngonngu;
    }

    public static int getsMa() {
        return sMa;
    }

    public static void setsMa(int sMa) {
        Sach.sMa = sMa;
    }

    @Override
    public String toString() {
        String nn = ngonngu ? "Tieng Viet" : "Tieng Anh";
        return ma + " " + ten + " " + nhaxuatban + " " + gia + " " + soluong + " " + nn;
    }
}
