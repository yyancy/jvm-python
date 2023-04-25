public class ParseIntTest {
  public static void main(String[] args) {
    // System.out.println(Character.digit('3', 10));
    // long limit = -Long.MAX_VALUE;
		// System.out.println(limit);

    // System.out.println(Integer.parseInt(args[0]));
    foo(args);
  }

  private static void foo(String[] args) {
    try {
      bar(args);
    } catch (NumberFormatException e) {
      System.out.println(e.getMessage());
    }
  }

  private static void bar(String[] args) {
    if (args.length == 0) {
      throw new IndexOutOfBoundsException("no args!");
    }
    int x = Integer.parseInt(args[0]);
    System.out.println(x);
  }
}