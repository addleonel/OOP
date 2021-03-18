package Java;

public class UberPool extends Car{
    String brand;
    String model;
    public UberPool(Integer id, String license, Account driver, Integer passengers, String brand, String model){
        super(id, license, driver, passengers);
        this.brand = brand;
        this.model = model;    
    }

    public void printData(){
        System.out.println("id: " + this.id+ ", License: " + this.license+", Driver: "
        + this.driver.name + ", Passengers: " + this.passengers + ", Brand: "
        + this.brand + ", Model: " + this.model);
    }
}
