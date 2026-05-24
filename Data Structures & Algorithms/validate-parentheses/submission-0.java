class Solution {
    public boolean isValid(String s) {
        boolean isValid=true;

        Stack<Character> stack = new Stack<>();

        for(int i=0; i<s.length(); i++) {
            Character curr = s.charAt(i);
            if(curr == '(' || 
                curr == '{' ||
                curr == '[') {
                    stack.push(curr);
                }
            else if (curr == ')'|| 
                curr == '}' ||
                curr == ']') {
                    if(stack.size() == 0) {
                        isValid=false;
                        break;
                    }
                        
                    Character top = stack.pop();

    // System.out.println("calc: " + !((top == '(' && curr == ')') ||
    //                     (top == '{' && curr == '}') ||
    //                     (top == '[' && curr == ']')));
                    if(!((top == '(' && curr == ')') ||
                        (top == '{' && curr == '}') ||
                        (top == '[' && curr == ']'))) {
                        isValid=false;
                        break;
                    }

                }
            else {
                continue;
            }
        }

        System.out.println("isValid: " + isValid);
        if(stack.size() > 0) {
            isValid = false;
        }

        return isValid;
    }
}
