package Java;

public class Car {
    Integer id;
    String license;
    Account driver;
    Integer passengers;

    public Car(Integer id, String license, Account driver, Integer passengers){
        this.id = id;
        this.license = license;
        this.driver = driver;
        this.passengers = passengers;
    }

    public void printData(){
        System.out.println("id: " + this.id+ ", License: " + this.license+", Driver: "
        + this.driver.name + ", Passengers: " + this.passengers);
    }
}
