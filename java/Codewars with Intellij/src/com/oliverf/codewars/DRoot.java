public class DRoot {
    public static int digital_root(int n) {
        while (Integer.toString(n).length() != 1) {
            n = addAndReturn(n);
        }
        return n;
    }
    public static int addAndReturn(int n) {
        int ans = 0;
        for (int i = 0; i < Integer.toString(n).length(); i++) {
            ans += Integer.parseInt(Character.toString((Integer.toString(n).charAt(i)))); 
        }
        return ans;
    }
    public static void main(String[] args) {
        System.out.println(digital_root(111));
    }
}
