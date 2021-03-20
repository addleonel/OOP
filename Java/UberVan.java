package Java;

import java.util.Map;
import java.util.ArrayList;

public class UberVan extends Car{

    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterials;

    public UberVan(Integer id, String license, Account driver, Integer passengers,
    Map<String, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatsMaterials){
        super(id, license, driver, passengers);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterials = seatsMaterials;
    }
    
}
