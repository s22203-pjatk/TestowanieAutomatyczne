package pl.pjatk;

        import java.util.ArrayList;
        import java.util.List;

public class ShoppingList {

    private List<String> items = new ArrayList<>();

    public void addItem(String item) {
        items.add(item);
    }

    public boolean containsItem(String item) {
        return items.contains(item);
    }

    public double calculateTotal() {
        double total = 0;
        // Przyjmujemy, że każdy produkt ma cenę 10 zł dla uproszczenia
        for (String item : items) {
            total += 10.0;
        }
        return total;
    }

    public List<String> getItems() {
        return items;
    }

    public void removeItem(String item) {
        items.remove(item);
    }
}
