package datastructure.sequential;

import java.util.EmptyStackException;

public class Stack<T> {
    class Node {
        T data;
        Node lower;

        Node(T data) {
            this.data = data;
        }
    }

    private Node top;

    public void push(T data) {
        Node node = new Node(data);
        node.lower = top;
        top = node;
    }

    public T pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        T item = top.data;
        top = top.lower;
        return item;
    }

    public T peek() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return top.data;
    }

    public boolean isEmpty() {
        return top == null;
    }

}
