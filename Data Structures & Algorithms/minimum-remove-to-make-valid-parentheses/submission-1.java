class Solution {
    public String minRemoveToMakeValid(String s) {
        
        StringBuilder out = new StringBuilder();
        int braces=0;
        Stack<Character> s1 = new Stack<Character>();
        Stack<Character> t = new Stack<Character>();
        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);

            if(ch == '(') {
                braces++;
            }
            if(ch == ')') {
                if(braces>0) {
                    --braces;
                } else {
                    continue;
                }
            }

            s1.push(ch);
        }

        while(s1.size() >0) {
            char ch = s1.pop();
            if(braces > 0 && ch == '(') {
                --braces;
                continue;
            }
            t.push(ch);
        }
        while(t.size() >0) {
            out.append(t.pop());
        }

        return out.toString();
    }
}