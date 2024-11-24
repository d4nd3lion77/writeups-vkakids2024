import java.util.*;

class Check {
    public static void main(String args[]) {
        Check Check = new Check();
        Scanner scanner = new Scanner(System.in); 
        System.out.print("Enter check password: ");
        String userInput = scanner.next();
        if (userInput.startsWith("vka{") && userInput.endsWith("}")) {
            String input = userInput.substring("vka{".length(), userInput.length() - 1);
            if (Check.checkPassword(input)) {
                System.out.println("Good job!!!");
            } else {
                System.out.println("Try harder");
            }
        } else {
            System.out.println("Nope :(");
        }
    }
    public boolean checkPassword(String password) { 
        boolean part1 = password.startsWith("java_code_");
        boolean part3 = password.endsWith("sy_to_read");
        boolean part2 = password.contains("is_that_ea");        
        return part1 && part3 && part2;
    }
}
