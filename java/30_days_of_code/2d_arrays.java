import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for(int i=0; i < 6; i++){
            for(int j=0; j < 6; j++){
                arr[i][j] = in.nextInt();
            }
        }
      int max_value = Integer.MIN_VALUE;
      int sum = 0;
      for(int row = 0; row < arr.length-2; row++){
        for(int column = 0; column < arr.length-2; column++){
          sum = 0;
          sum += arr[row][column] + arr[row][column+1] + arr[row][column+2];
          sum += arr[row+1][column+1];
          sum += arr[row+2][column] + arr[row+2][column+1] + arr[row+2][column+2];
          
          if(sum >= max_value){
            max_value = sum;
          }
        }
      }
      System.out.println(max_value);

    }
}
