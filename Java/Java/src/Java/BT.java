
package Java;
import java.util.Scanner;
public class BT {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        MS ms=new MS();
        ms.input(in);
        ms.out();
    }
}
class Vihicle{
    private String vin, manufacturer;
    private int year;
    private double cost;
    private String color;

    public Vihicle() {
    }

    public String getVin() {
        return vin;
    }

    public void setVin(String vin) {
        this.vin = vin;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public double getCost() {
        return cost;
    }

    public void setCost(double cost) {
        this.cost = cost;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String toString(){
        String st=vin+" "+manufacturer.toUpperCase()+" "+cost+" "+year+" "+color;
        return st;
    }
    public void input(Scanner in){
        vin=in.nextLine();
        manufacturer=in.nextLine();
        color=in.nextLine();
        year=Integer.parseInt(in.nextLine());
        cost=Double.parseDouble(in.nextLine());
    }
}
class MS{
    private Vihicle[] a;
    public MS(){
        
    }
    public void input(Scanner in){
        int n=Integer.parseInt(in.nextLine());
        a=new Vihicle[n];
        for(int i=0;i<n;i++){
            a[i]=new Vihicle();
            a[i].input(in);
        }
    }
    public void out(){
        for(Vihicle i:a){
            System.out.println(i);
        }
        System.out.println(a.length);
    }
}