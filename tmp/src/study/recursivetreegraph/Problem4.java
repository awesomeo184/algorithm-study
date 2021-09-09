package study.recursivetreegraph;

import java.util.LinkedList;
import java.util.Queue;


/*
* BFS 레벨 탐색*/
public class Problem4 {

    Node root;

    public void BFS(Node root) {
        Queue<Node> queue = new LinkedList<>();
        int L = 0;
        queue.add(root);
        while (!queue.isEmpty()) {
            System.out.print(L + " : ");
            int len = queue.size();
            for (int i = 0; i < len; i++) {
                Node cur = queue.poll();
                System.out.print(cur.data + " ");
                if (cur.lt != null) {
                    queue.add(cur.lt);
                }
                if (cur.rt != null) {
                    queue.add(cur.rt);
                }
            }
            L++;
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Problem4 tree = new Problem4();
        tree.root = new Node(1);
        tree.root.lt = new Node(2);
        tree.root.rt = new Node(3);
        tree.root.lt.lt = new Node(4);
        tree.root.lt.rt = new Node(5);
        tree.root.rt.lt = new Node(6);
        tree.root.rt.rt = new Node(7);
        tree.BFS(tree.root);
    }

}


