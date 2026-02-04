package ThucHanh;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Bai2 {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        List<Tour> a=new ArrayList<>();
        int n=Integer.parseInt(in.nextLine());
        for (int i = 0; i < n; i++) {
            a.add(new Tour(in.nextLine(),in.nextLine()
                    ,Integer.parseInt(in.nextLine())
                    ,Double.parseDouble(in.nextLine())));
        }
        a.forEach(x->System.out.println(x));
    }
}
class Tour{
    private String ma,tu,den;
    private int soNguoi;
    private double gia;
    private static int sMa=1;

    public Tour() {
    }

    public Tour(String tu, String den, int soNguoi, double gia) {
        this.tu = tu;
        this.den = den;
        this.soNguoi = soNguoi;
        this.gia = gia;
    }

    public String getMa() {
        return tu+"-"+den+"*"+String.format("%03d",sMa++);
    }

    public void setMa(String ma) {
        this.ma = ma;
    }

    public String getTu() {
        return tu;
    }

    public void setTu(String tu) {
        this.tu = tu;
    }

    public String getDen() {
        return den;
    }

    public void setDen(String den) {
        this.den = den;
    }

    public int getSoNguoi() {
        return soNguoi;
    }

    public void setSoNguoi(int soNguoi) {
        this.soNguoi = soNguoi;
    }

    public double getGia() {
        return gia;
    }

    public void setGia(double gia) {
        this.gia = gia;
    }

    public static int getsMa() {
        return sMa;
    }

    public static void setsMa(int sMa) {
        Tour.sMa = sMa;
    }
    private double getThanhTien(){
        if(soNguoi<5){
            return soNguoi*gia;
        }
        else if(soNguoi<=10){
            double Tongtien=soNguoi*gia;
            double Dagiam=Tongtien-(Tongtien*10/100);
            return Dagiam;
        }
        else{
            double Tongtien=soNguoi*gia;
            double Dagiam=Tongtien-(Tongtien*20/100);
            return Dagiam;
        }
    }

    @Override
    public String toString() {
        return getMa()+" "+soNguoi+" "+gia+" "+getThanhTien();
    }
}