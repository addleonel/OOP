package Java;

import java.util.ArrayList;
import java.util.Map;

public class UberBlack extends Car{
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterials;

    public UberBlack(Integer id, String license, Account driver, Integer passengers,
    Map<String, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatsMaterials){
        super(id, license, driver, passengers);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterials = seatsMaterials;
    } 
}
