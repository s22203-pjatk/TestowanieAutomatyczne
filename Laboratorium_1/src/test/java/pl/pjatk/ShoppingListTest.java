package pl.pjatk;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class ShoppingListTest {

    private ShoppingList shoppingList;

    @Before
    public void setUp() {
        shoppingList = new ShoppingList();
    }

    @Test
    public void testAddItem() {
        shoppingList.addItem("Milk");
        assertTrue(shoppingList.containsItem("Milk"));
    }

    @Test
    public void testContainsItem() {
        shoppingList.addItem("Bread");
        assertTrue(shoppingList.containsItem("Bread"));
        assertFalse(shoppingList.containsItem("Eggs"));
    }

    @Test
    public void testCalculateTotal() {
        shoppingList.addItem("Apple");
        shoppingList.addItem("Banana");
        assertEquals(20.0, shoppingList.calculateTotal(), 0.01);
    }

    @Test
    public void testCalculateTotalEmptyList() {
        assertEquals(0.0, shoppingList.calculateTotal(), 0.01);
    }

    @Test
    public void testGetItems() {
        shoppingList.addItem("Coffee");
        shoppingList.addItem("Tea");
        assertArrayEquals(new String[]{"Coffee", "Tea"}, shoppingList.getItems().toArray());
    }

    @Test
    public void testAddDuplicateItem() {
        ShoppingList shoppingList = new ShoppingList();
        shoppingList.addItem("Chips");
        shoppingList.addItem("Chips");
        assertTrue(shoppingList.getItems().contains("Chips"));
    }

    @Test
    public void testAddMultipleItems() {
        shoppingList.addItem("Chicken");
        shoppingList.addItem("Beef");
        shoppingList.addItem("Fish");
        assertEquals(3, shoppingList.getItems().size());
    }

    @Test
    public void testRemoveItem() {
        shoppingList.addItem("Sugar");
        assertTrue(shoppingList.containsItem("Sugar"));
        shoppingList.getItems().remove("Sugar");
        assertFalse(shoppingList.containsItem("Sugar"));
    }

    @Test
    public void testRemoveItems() {
        ShoppingList shoppingList = new ShoppingList();
        shoppingList.addItem("Sugar");
        assertTrue(shoppingList.containsItem("Sugar"));
        shoppingList.removeItem("Sugar");
        assertFalse(shoppingList.containsItem("Sugar"));
    }

    @Test
    public void testCalculateTotalEmptyList1() {
        ShoppingList shoppingList = new ShoppingList();
        assertEquals(0.0, shoppingList.calculateTotal(), 0.01);
    }
}
