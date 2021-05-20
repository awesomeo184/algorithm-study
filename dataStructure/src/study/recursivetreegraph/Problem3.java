package study.recursivetreegraph;

/*
* 이진트리 순회 (DFS)
* */
public class Problem3 {

    Node root;

    public void preorderTraversal(Node root) {
        if (root == null) {
            return;
        } else {
            System.out.print(root.data + " ");
            preorderTraversal(root.lt);
            preorderTraversal(root.rt);
        }
    }

    public void inorderTraversal(Node root) {
        if (root == null) {
            return;
        } else {
            inorderTraversal(root.lt);
            System.out.print(root.data + " ");
            inorderTraversal(root.rt);
        }
    }

    public void postorderTraversal(Node root) {
        if (root == null) {
            return;
        } else {
            postorderTraversal(root.lt);
            postorderTraversal(root.rt);
            System.out.print(root.data + " ");
        }
    }



    public static void main(String[] args) {
        Problem3 tree = new Problem3();
        tree.root = new Node(1);
        tree.root.lt = new Node(2);
        tree.root.rt = new Node(3);
        tree.root.lt.lt = new Node(4);
        tree.root.lt.rt = new Node(5);
        tree.root.rt.lt = new Node(6);
        tree.root.rt.rt = new Node(7);
        tree.postorderTraversal(tree.root);
    }

}

class Node {

    int data;
    Node lt, rt;

    public Node(int val) {
        data = val;
        lt = rt = null;
    }
}