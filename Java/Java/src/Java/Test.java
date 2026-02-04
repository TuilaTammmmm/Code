import java.io.*;
import java.util.*;

public class Test {
    public static void main(String[] args) {
        QLSach q = new QLSach();
        Scanner sc = new Scanner(System.in);
        String tenFile = "Sach.txt";

        while (true) {
            System.out.println("""
                               ==========================
                               QUAN LY SACH - MENU
                               1. Nhap Sach (them tu ban phim)
                               2. Hien thi danh sach
                               3. Luu danh sach vao file
                               4. Doc danh sach tu file
                               5. Tim theo ma sach
                               6. Xoa theo ma sach
                               7. Sua thong tin theo ma sach
                               8. Sap xep theo ma sach
                               9. Sap xep theo ten sach
                               10. Sap xep theo gia sach
                               11. Tim theo ngon ngu (Tieng Viet)
                               0. Thoat
                               ==========================
                               """);
            System.out.print("Moi chon: ");

            int chon = Integer.parseInt(sc.nextLine());

            switch (chon) {
                case 1 -> q.nhap(sc);
                case 2 -> q.hienthi();
                case 3 -> q.luuDS(tenFile);
                case 4 -> q.docDS(tenFile);
                case 5 -> {
                    System.out.print("Nhap ma sach: ");
                    q.timTheoMa(sc.nextLine());
                }
                case 6 -> {
                    System.out.print("Nhap ma sach: ");
                    q.xoaTheoMa(sc.nextLine());
                }
                case 7 -> {
                    System.out.print("Nhap ma sach: ");
                    String ma = sc.nextLine();
                    System.out.print("NXB moi: ");
                    String nxb = sc.nextLine();
                    System.out.print("Gia moi: ");
                    double gia = Double.parseDouble(sc.nextLine());
                    System.out.print("Ngon ngu moi (true:TV, false:NN): ");
                    boolean nn = Boolean.parseBoolean(sc.nextLine());
                    q.suaTheoMa(ma, nxb, gia, nn);
                }
                case 8 -> { q.sapXepTheoMa(); q.hienthi(); }
                case 9 -> { q.sapXepTheoTen(); q.hienthi(); }
                case 10 -> { q.sapXepTheoGia(); q.hienthi(); }
                case 11 -> q.timTheoNgonNgu(true);
                case 0 -> {
                    System.out.println("Thoat!");
                    System.exit(0);
                }
                default -> System.out.println("Chon sai! Chon lai 0-11");
            }
        }
    }
}

// =============================

interface IChucNang {
    void nhap(Scanner sc);
    void hienthi();
    void luuDS(String tenFile);
    void docDS(String tenFile);
    void timTheoMa(String masach);
    void xoaTheoMa(String masach);
    void suaTheoMa(String masach, String nhaxuatban, double gia, boolean ngonngu);
    void sapXepTheoMa();
    void sapXepTheoTen();
    void sapXepTheoGia();
    void timTheoNgonNgu(boolean ngonngu);
}

// =============================

class QLSach implements IChucNang {

    private List<Sach> ds;

    public QLSach() {
        ds = new ArrayList<>();
    }

    @Override
    public void nhap(Scanner sc) {
        System.out.print("Ten sach: ");
        String ten = sc.nextLine();
        System.out.print("NXB: ");
        String nxb = sc.nextLine();
        System.out.print("Gia: ");
        double gia = Double.parseDouble(sc.nextLine());
        System.out.print("So luong: ");
        int sl = Integer.parseInt(sc.nextLine());
        System.out.print("Ngon ngu (true:TV, false:NN): ");
        boolean nn = Boolean.parseBoolean(sc.nextLine());

        ds.add(new Sach(ten, nxb, gia, sl, nn));
    }

    @Override
    public void hienthi() {
        if (ds.isEmpty()) {
            System.out.println("Danh sach rong!");
            return;
        }
        ds.forEach(System.out::println);
    }

    @Override
    public void luuDS(String tenFile) {
        try (PrintWriter pw = new PrintWriter(new FileWriter(tenFile))) {
            for (Sach s : ds) {
                pw.println(String.join(";",
                        s.getTensach(),
                        s.getNhaxuatban(),
                        String.valueOf(s.getGia()),
                        String.valueOf(s.getSoluong()),
                        String.valueOf(s.isNgonngu())
                ));
            }
            System.out.println("Luu file thanh cong!");
        } catch (Exception e) {
            System.out.println("Loi luu file: " + e);
        }
    }

    @Override
    public void docDS(String tenFile) {
        try (BufferedReader br = new BufferedReader(new FileReader(tenFile))) {
            ds.clear();
            String line;
            while ((line = br.readLine()) != null) {
                String[] arr = line.split(";");
                if (arr.length == 5) {
                    ds.add(new Sach(
                            arr[0],
                            arr[1],
                            Double.parseDouble(arr[2]),
                            Integer.parseInt(arr[3]),
                            Boolean.parseBoolean(arr[4])
                    ));
                }
            }
            System.out.println("Doc file thanh cong!");
        } catch (Exception e) {
            System.out.println("Loi doc file: " + e);
        }
    }

    private int getViTri(String ma) {
        for (int i = 0; i < ds.size(); i++) {
            if (ds.get(i).getMasach().equalsIgnoreCase(ma))
                return i;
        }
        return -1;
    }

    @Override
    public void timTheoMa(String ma) {
        int p = getViTri(ma);
        if (p == -1) System.out.println("Khong tim thay!");
        else System.out.println(ds.get(p));
    }

    @Override
    public void xoaTheoMa(String ma) {
        int p = getViTri(ma);
        if (p == -1) System.out.println("Khong tim thay!");
        else {
            ds.remove(p);
            System.out.println("Xoa OK!");
        }
    }

    @Override
    public void suaTheoMa(String ma, String nxb, double gia, boolean nn) {
        int p = getViTri(ma);
        if (p == -1) System.out.println("Khong tim thay!");
        else {
            Sach s = ds.get(p);
            s.setNhaxuatban(nxb);
            s.setGia(gia);
            s.setNgonngu(nn);
            System.out.println("Sua OK!");
        }
    }

    @Override
    public void sapXepTheoMa() {
        ds.sort(Comparator.comparing(Sach::getMasach));
        System.out.println("Sap xep theo ma xong!");
    }

    @Override
    public void sapXepTheoTen() {
        ds.sort(Comparator.comparing(Sach::getTensach));
        System.out.println("Sap xep theo ten xong!");
    }

    @Override
    public void sapXepTheoGia() {
        ds.sort(Comparator.comparing(Sach::getGia));
        System.out.println("Sap xep theo gia xong!");
    }

    @Override
    public void timTheoNgonNgu(boolean ngonngu) {
        ds.stream().filter(s -> s.isNgonngu() == ngonngu)
                .forEach(System.out::println);
    }
}

// =============================

class Sach {
    private String tensach, masach, nhaxuatban;
    private int soluong;
    private double gia;
    private boolean ngonngu;
    private static int sMa = 1;

    public Sach(String tensach, String nhaxuatban, double gia, int soluong, boolean ngonngu) {
        this.masach = String.format("%04d", sMa++);
        this.tensach = tensach;
        this.nhaxuatban = nhaxuatban;
        this.gia = gia;
        this.soluong = soluong;
        this.ngonngu = ngonngu;
    }

    public String getMasach() { return masach; }
    public String getTensach() { return tensach; }
    public String getNhaxuatban() { return nhaxuatban; }
    public double getGia() { return gia; }
    public int getSoluong() { return soluong; }
    public boolean isNgonngu() { return ngonngu; }

    public void setNhaxuatban(String x) { this.nhaxuatban = x; }
    public void setGia(double x) { this.gia = x; }
    public void setNgonngu(boolean x) { this.ngonngu = x; }

    @Override
    public String toString() {
        return masach + " | " + tensach + " | " + nhaxuatban +
                " | " + gia + " | SL:" + soluong +
                " | " + (ngonngu ? "TV" : "NN");
    }
}