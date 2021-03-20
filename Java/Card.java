package Java;

public class Card extends Payment{
    
    Integer number;
    String cvv;
    String date;

    public Card(Integer id, String cvv, String date){
        super(id);
        this.cvv = cvv;
        this.date = date;
    }
}
