print('     *')
print('   *  *')
print('  *    *')
print(' *      *')
print('***    ***')
print("  *    *")
print("  *    *")
print('  ******\n\n\n')
#Here we print an arrow by using the pwint function and printing "*" and spaces to make an arrow.

print("    *\n   *  *\n  *    *\n *      *\n***    ***\n  *    *\n  *    *\n  ******\n\n\n\n")
#Here we print an arrow exactly like the one before it, but here we use "\n" to move to the next line with printing. This help us to reduce the number of lines of code.

print("        *        ")
print("      *   *      ")
print("     *     *     ")
print("    *       *    ")
print("   *         *   ")
print("  *           *  ")
print(" *             * ")
print("*****       *****")
print("    *       *    ")
print("    *       *    ")
print("    *       *    ")
print("    *       *    ")
print("    *********    ")
#Here I made the arrow twice as large.

print(("     *      ")*2,"\n",("   *  *    ")*2,"\n",("  *    *   ")*2,"\n",(" *      *  ")*2,"\n",("***    *** ")*2,"\n",("  *    *   ")*2,"\n",("  *    *   ")*2,"\n",("  *    *   ")*2,"\n",("  *    *   ")*2,"\n",("  *    *   ")*2,"\n",("  *    *   ")*2,"\n",("  ******   ")*2)
#Here I print two arrows by multipliying the different sections of the arrow by 2 to print two arros side by side.

'''
If you remove the quotes of the following line of code:
print("***    ***")
The following error will show:

print(***    ***)
            ^
SyntaxError: invalid syntax

this is because you need the quotes to indicate that youre going to print a string (Unless you're triying to print a variable with a string stored in it).
'''

'''
If you remove the parentheses, the following error will show:

print"  ******\n\n\n"
    ^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

As the Terminal indicates, you need the parentheses when calling a function.
'''

'''
If I change the word print for something else, the following error will show:

 testing("  ******\n\n\n")
    ^^^^^^^
NameError: name 'testing' is not defined

This is because, when using the syntax "text()", the "text" represents the name of a function. So in this case, we are triying to call a function called "test", but since I didn't define it, it shows an error.
'''

'''
If i change the quotes for apostrophes, the code will still work:
In line 1 of the script, used apostrophes instead:
print('     *')
The code still works and prints the symbols just like using quotes.
'''