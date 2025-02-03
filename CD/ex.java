public class ex {

    public static void switch_case_example(int value) {
        switch (value) {
            case 1:
                System.out.println("Case 1");
                break;
            case 2:
                System.out.println("Case 2");
                break;
            case 3:
                System.out.println("Case 3");
                break;
            default:
                System.out.println("Default case");
        }
    }

    public static void main(String[] args) {
        int value = 1;
        switch_case_example(value);
    }
}
