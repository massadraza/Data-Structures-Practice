// Massad Raza


public class timeComplexityPrograms{

    public static void main(String[] args) {

        System.out.println("Here are examples of Big O algorithms");
        System.out.println(constantOperation());
        System.out.println(linearOperation());

    }

    // O(1) Time Complexity --> Accessing an element in an array is constant time

    public static int constantOperation(){

        int[] one = {1, 2, 3, 4};

        return one[1];
    }

    // O(n) Time Complexity 

    public static boolean linearOperation(){

        int key = 3;
        int[] values = {1, 2, 3, 4, 5};

        for(int i = 0; i < values.length; i++){
            if(values[i] == key){
                return true;
            }
        }

        return false;

        
    }







}
