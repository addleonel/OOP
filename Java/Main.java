package Java;

class Main{
    public static void main(String[] args) {
        //System.out.print("Hello");
        Account thomas = new Account(1, "Thomas Edison", "32123321");
        Account leonel = new Account(2, "Leonel", "10239999");

        Car marvel_car = new Car(1, "MDX-321", thomas, 4);
        Car my_car = new Car(2, "T-500", leonel, 2);
        
        marvel_car.printData();
        my_car.printData();

        UberX thomas_uberx = new UberX(1, "T-800", thomas, 3, "Ford", "Aspire");
        UberX my_uberx = new UberX(2, "RMD-MN", leonel, 2, "Chevrolet", "Blazer");

        thomas_uberx.printData();
        my_uberx.printData();
    }
}