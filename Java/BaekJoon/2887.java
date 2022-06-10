import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {

  static class Node implements Comparable<Node> {
    int site;
    int id;

    public Node(int site, int id) {
      this.site = site;
      this.id = id;
    }

    @Override
    public int compareTo(Node o) {
      return this.site - o.site;
    }
  }

  static class Line implements Comparable<Line> {
    int cost;
    int u;
    int v;

    public Line(int cost, int u, int v) {
      this.cost = cost;
      this.u = u;
      this.v = v;
    }

    @Override
    public int compareTo(Line o) {
      return this.cost - o.cost;
    }
  }


  static Node[] xAry;
  static Node[] yAry;
  static Node[] zAry;
  static int[] parent;

  public static void main(String[] args) throws IOException {
    // input
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    xAry = new Node[N];
    yAry = new Node[N];
    zAry = new Node[N];
    for (int i = 0; i < N; i++) {
      String[] values = br.readLine().split(" ");
      xAry[i] = new Node(Integer.parseInt(values[0]), i);
      yAry[i] = new Node(Integer.parseInt(values[1]), i);
      zAry[i] = new Node(Integer.parseInt(values[2]), i);
    }

    // initialize parent
    parent = new int[N];
    for (int id = 0; id < N; id++) {
      parent[id] = id;
    }

    Arrays.sort(xAry);
    Arrays.sort(yAry);
    Arrays.sort(zAry);

    List<Line> lines = new ArrayList<>();
    for (int i = 0; i < N - 1; i++) {
      lines.add(new Line(Math.abs(xAry[i].site - xAry[i + 1].site), xAry[i].id, xAry[i + 1].id));
      lines.add(new Line(Math.abs(yAry[i].site - yAry[i + 1].site), yAry[i].id, yAry[i + 1].id));
      lines.add(new Line(Math.abs(zAry[i].site - zAry[i + 1].site), zAry[i].id, zAry[i + 1].id));
    }
    Collections.sort(lines);

    int total = 0;
    for (Line line : lines) {
      if (unionFind(parent, line.u, line.v))
        total += line.cost;
    }
    System.out.println(total);
  }

  static int findParent(int[] parent, int u) {
    if (parent[u] != u)
      parent[u] = findParent(parent, parent[u]);
    return parent[u];
  }

  static boolean unionFind(int[] parent, int u, int v)
  {
    if (findParent(parent, u) == findParent(parent, v))
      return false;

    u = findParent(parent, u);
    v = findParent(parent, v);
    if (u < v) {
      parent[v] = u;
    } else {
      parent[u] = v;
    }
    return true;
  }
}