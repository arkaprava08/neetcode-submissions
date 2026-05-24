class Solution {
    public boolean isPalindrome(String s) {
        boolean palindrome=true;

        int i=0;
        int j=s.length()-1;

        while(i<=j) {
            System.out.println("i :" + i + " j : " + j);
            while(i<=j && (!('A' <= s.charAt(i) && 'Z' >= s.charAt(i)) && 
                    !('a' <= s.charAt(i) && 'z' >= s.charAt(i)) &&
                    !('0' <= s.charAt(i) && '9' >= s.charAt(i))) ) {
                        ++i;
                    }
            while(i<=j && (!('A' <= s.charAt(j) && 'Z' >= s.charAt(j)) && 
                    !('a' <= s.charAt(j) && 'z' >= s.charAt(j)) &&
                    !('0' <= s.charAt(j) && '9' >= s.charAt(j)) )) {
                        --j;
                    }

            
            System.out.println("after - i :" + i + " j : " + j);
            if(i<=j && !(Character.toLowerCase(s.charAt(i)) == Character.toLowerCase(s.charAt(j)))) {
                return false;
            }

            ++i;
            --j;
        }

        return palindrome;
    }
}
