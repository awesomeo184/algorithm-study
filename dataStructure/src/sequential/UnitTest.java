package sequential;

public class UnitTest {

    public static void main(String[] args) {
        SinglyLinkedList list = new SinglyLinkedList();

        list.addFirst(1);
        list.addFirst(2);
        list.addFirst(3);
        list.addFirst(4);

        list.deleteLast();
        list.deleteLast();
        list.deleteLast();

        System.out.println(list);
    }
}
