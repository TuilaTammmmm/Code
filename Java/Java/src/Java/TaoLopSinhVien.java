package Java;

import java.util.Scanner;

public class TaoLopSinhVien {

    public static void main(String[] args) {
        SinhVien s = new SinhVien();
        s.input();
        s.output();
        System.out.println(s.getHoVaTen() + " " + s.getXepLoai());
    }
}

class SinhVien {

    private String maSV, hoVaDem, ten;
    private int tuoi;
    private boolean gioitinh;
    private double diem1, diem2;

    public SinhVien() {
    }

    public void setMaSV(int number) {
        this.maSV = "D22DCCN" + number;
    }

    public void setDiem(double diem1, double diem2) {
        this.diem1 = diem1;
        this.diem2 = diem2;
    }

    public String getHoVaTen() {
        return hoVaDem + " " + ten;
    }

    public double getGPA() {
        return (diem1 + diem2 * 2) / 3;
    }

    public String getXepLoai() {
        double d = getGPA();
        if (d < 5) return "yeu";
        else if (d < 6.5) return "trung binh";
        else if (d < 8) return "kha";
        else if (d < 9) return "gioi";
        else return "xuat sac";
    }

    public void input() {
        Scanner in = new Scanner(System.in);

        System.out.print("Nhap ma so (so nguyen): ");
        int num = in.nextInt();
        setMaSV(num);

        in.nextLine(); // tránh trôi dòng

        System.out.print("Nhap ho va dem: ");
        hoVaDem = in.nextLine();

        System.out.print("Nhap ten: ");
        ten = in.nextLine();

        System.out.print("Nhap tuoi: ");
        tuoi = in.nextInt();

        System.out.print("Nhap gioi tinh (1-nam, 0-nu): ");
        gioitinh = in.nextInt() == 1;

        System.out.print("Nhap diem 1: ");
        diem1 = nhapDiem(in);

        System.out.print("Nhap diem 2: ");
        diem2 = nhapDiem(in);
    }

    private double nhapDiem(Scanner in) {
        double d;
        while (true) {
            d = in.nextDouble();
            if (d >= 0 && d <= 10) break;
            System.out.print("Nhap sai, nhap lai (0-10): ");
        }
        return d;
    }

    public void output() {
        String st=maSV+" "+getHoVaTen()+" "+tuoi+" "+(gioitinh?"nam":"nu")+" "+getGPA()+" "+getXepLoai();
        System.out.println(st);
    }
}
