public class binarysum {
    public static void main(String[] args) {
        String binary1 = "0110";
        String binary2 = "0101";
        // Convert binary strings to integers
        int num1 = Integer.parseInt(binary1, 2);
        int num2 = Integer.parseInt(binary2, 2);
        // Perform addition
        int sum = num1 + num2;
        // Convert sum back to binary string
        String binarySum = Integer.toBinaryString(sum);
        System.out.println("Binary number 1: " + binary1);
        System.out.println("Binary number 2: " + binary2);
        System.out.println("Sum in binary: " + binarySum);
    }
}