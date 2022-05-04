# E -> TE'
# E'-> +TE'|e
# T -> FT'
# T'-> *FT'|e
# F -> (E) |id

def E(Str, l):
    l = T(Str, l)
    l = Ed(Str, l)

    return l

def T(Str, l):
    l = F(Str, l)
    l = Td(Str, l)

    return l

def Ed(Str, l):
    if Str[l[0]] == "+":
        l[0] += 1
        l = T(Str, l)
        l = Ed(Str, l)

    return l

def F(Str, l):
    if Str[l[0]] == "(":
        l[0] += 1
        l = E(Str, l)
        if Str[l[0]] == ")":
            l[0] += 1
        else:
            l = error(l)
    
    elif Str[l[0]] == 'd':
        l[0] += 1
    
    else:
        error(l)
        
    return l

def Td(Str, l):
    if Str[l[0]] == "*":
        l[0] += 1
        l = F(Str, l)
        l = Td(Str, l)
    
    return l

def error(l):
    print("Error occured!")
    l[1] = 1

    return l


input = input("Enter a string: ") + "$"
l = [0, 0]
l = E(input, l)

if l[1] == 0:
    print("String is Valid")

else:
    print("String is invalid")

# i/o
# Enter a string: d + d
# String is Valid
# Enter a string: d +
# String is Valid


# import java.util.*;
# public class RDP{
#     static String input;
#     static int i;
#     public static void main(String[] args){
        
#     System.out.println("Grammer : S->aSb|e \n B->b|a\n");
#     System.out.println("input String");
#     Scanner sc = new Scanner (System.in);
#     input=sc.nextLine();
#     i=0;
#     input=input+"$";
#     S();
#     }
#     private static void S(){
#         if(input.charAt(i)=='a'){
#             i++;
#             B();
#             if(i>0){
#                 if(input.charAt(i)=='$')
#                     System.out.println("String is accepted");
#                 else{
#                     System.out.println("String is invalid");
#                     System.exit(0);
#                 }
#             }
#         }
#         else{
#             System.out.println("String is invalid");
#             System.exit(0);
#         }
#     }
#             private static void B(){
#                 if(input.charAt(i)=='a'){
#                     i++;
#                     B();
#                 }
#                 else
#                 if(input.charAt(i)=='b')
#                 {
#                     i++;
#                     if(input.charAt(i)!='$')
#                     B();
#                 }
#                 else{
#                     System.out.println("String is invalid");
#                     System.exit(0);
#                 }
#             }
# }
    
# //Output:-
# //Grammer : S->aSb|e 
#  //B->b|a

# //input String
# //ababb
# //String is accepted