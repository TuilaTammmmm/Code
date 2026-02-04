
package Java;


import java.io.*;
import java.util.*;

public class LuongGiangVien {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=Integer.parseInt(sc.nextLine());
        for (int i = 0; i < n; i++) {
            String ten=sc.nextLine();
            double hsluong=Double.parseDouble(sc.nextLine());
            String hskk=sc.nextLine();
            int gio=Integer.parseInt(sc.nextLine());
            GiangVien gv=new GiangVien(ten, hsluong, hskk, gio);
            System.out.println(gv);
        }
    }
}
class GiangVien{
    private String ma,hoten;
    private double hsluong;
    private String hskhuyenkhich;
    private int gnnkk;
    private static int sma=1;

    public GiangVien() {
    }
    

    public GiangVien(String hoten, double hsluong, String hskhuyenkhich, int gnnkk) {
        this.ma = "PM"+String.format("%03d",sma++);
        this.hoten = hoten;
        this.hsluong = hsluong;
        this.hskhuyenkhich = hskhuyenkhich;
        this.gnnkk = gnnkk;
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

    public double getHsluong() {
        return hsluong;
    }

    public void setHsluong(double hsluong) {
        this.hsluong = hsluong;
    }

    public String getHskhuyenkhich() {
        return hskhuyenkhich;
    }

    public void setHskhuyenkhich(String hskhuyenkhich) {
        this.hskhuyenkhich = hskhuyenkhich;
    }

    public int getGnnkk() {
        return gnnkk;
    }

    public void setGnnkk(int gnnkk) {
        this.gnnkk = gnnkk;
    }

    public int getSma() {
        return sma;
    }

    public void setSma(int sma) {
        this.sma = sma;
    }
    private double luonglinh(){
        double hskk=1;
        if(hskhuyenkhich.trim().toUpperCase().charAt(0)=='A'){
            hskk=1.5;
        }else if(hskhuyenkhich.trim().toUpperCase().charAt(0)=='B'){
            hskk=1.2;
        }
        double luong=hsluong*hskk*3000;
        if(gnnkk<=100){
            luong*=0.85;
        }else if(gnnkk<=350){
            luong*=0.9;
        }else if(gnnkk<500){
            luong*=0.95;
        }
        return luong;
    }
    @Override
    public String toString() {
        return ma+" "+hoten+" "+hsluong+" "+hskhuyenkhich+" "+gnnkk+" "+Math.round(luonglinh());
    }   
}