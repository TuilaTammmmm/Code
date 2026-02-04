package ThucHanh;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Bai1 {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        List<GiangVien> a=new ArrayList<>();
        int n=Integer.parseInt(in.nextLine());
        for (int i = 0; i < n; i++) {
            a.add(new GiangVien(in.nextLine(), 
           Double.parseDouble(in.nextLine())));
        }
        a.forEach(gv->System.out.println(gv));
    }
}
class GiangVien{
    private String ma,hoten;
    private double hsLuong;
    private static int sMa=1;

    public GiangVien() {
    }

    public GiangVien(String hoten, double hsLuong) {
        this.ma = "PM"+String.format("%03d", sMa++);
        this.hoten = hoten;
        this.hsLuong = hsLuong;
    }

    public String getMa() {
        return ma;
    }

    public void setMa(String ma) {
        this.ma = ma;
    }

    public String getHoten() {
        return hoten;
    }

    public void setHoten(String hoten) {
        this.hoten = hoten;
    }

    public double getHsLuong() {
        return hsLuong;
    }

    public void setHsLuong(double hsLuong) {
        this.hsLuong = hsLuong;
    }

    public static int getsMa() {
        return sMa;
    }

    public static void setsMa(int sMa) {
        GiangVien.sMa = sMa;
    }
    private double getLuong(){
        return hsLuong*300000;
    }

    @Override
    public String toString() {
        return ma+" "+hoten+" "+hsLuong+" "+Math.round(getLuong());  
    }
}
