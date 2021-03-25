package sequential;

import java.util.LinkedList;
import java.util.NoSuchElementException;

public class SinglyLinkedList {

    Node head;
    int size = 0;

    static class Node {

        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }



    /*
     * add first element
     * */
    public void addFirst(int data) {
        Node newNode = new Node(data);

        if (!isEmpty()) {
            newNode.next = head;
        }
        head = newNode;
        size++;
    }

    /*
     * add last element
     * */
    public void addLast(int data) {
        if (isEmpty()) {
            head = new Node(data);
        } else {
            Node node = head;
            while (node.next != null) {
                node = node.next;
            }
            node.next = new Node(data);
        }
        size++;
    }

    /*
     * delete first element
     * */
    public void deleteFirst() {
        if (isEmpty()) {
            throw new NoSuchElementException("The List is empty");
        }
        head = head.next;
        size--;
    }

    /*
     * delete last element
     * */
    public void deleteLast() {
        Node prev = null;
        Node node = head;

        if (isEmpty()) {
            throw new NoSuchElementException("The List is empty");
        }

        // when list has a single element
        if (node.next == null) {
            head = null;
        } else {
            while (node.next != null) {
                prev = node;
                node = node.next;
            }
            prev.next = null;
        }
        size--;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    // Tells if the argument is the index of a valid position for an add operation.
    public boolean isPositionIndex(int index) {
        return index >= 0 && index <= size;
    }

    public void checkPositionIndex(int index) {
        if (!isPositionIndex(index)) {
            throw new IndexOutOfBoundsException();
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node node = head;

        if (node != null) {
            sb.append(node.data);
            while (node.next != null) {
                node = node.next;
                sb.append(" -> ");
                sb.append(node.data);
            }
        }
        return sb.toString();
    }

}
