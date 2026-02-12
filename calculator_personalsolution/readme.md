
this is basically a calculator that reads a math expression from a string and evaluates it.
It’s kinda like a manual, DIY version of the Shunting Yard algorithm, but built using my own personal approach.

Honestly… I don’t even know why I made this. 
it
Reads numbers and operators (+, -, *, /) directly from input.

Sorts them manually by operator precedence (* and / first, then + and -).

Calculates step by step with a stack.

Prints the result with 4 decimal places.

Keeps running until you say “no”.

🧠 How It Works (my weird way)

Parse the input → separate numbers into one list, operators into another.

Sort operators by precedence → first * and /, then + and -. Push related numbers/operators into “final” vectors.

Calculate → use a stack to process everything in order.

It’s not the classic algorithm, it’s my own mix of brute force + sorting + stack.
Hardcore? Yes. Efficient? Maybe not. But fun? Absolutely.

🚀 Example

Input:

3+5*2-8/4


Process (behind the scenes):

Numbers: [3, 5, 2, 8, 4]

Operators: [+, *, -, /]

Sorted into → Numbers: [5, 2, 8, 4, 3], Ops: [* , / , + , -]

Output:

Result: 2.2500

⚠️ Limitations

No parentheses support.

Only integers as input (no decimals yet).

Doesn’t handle negative numbers at the start.

🛠️ Compile & Run
g++ calculator.cpp -o calculator
./calculator
idk. 
I spent 4 days making this.
90% of the time was me staring at the code, overthinking solutions.
Eventually, I gave up and asked GPT for help with the last 30%. That’s when it suggested:

Use used[] to avoid duplicates.

Use a stack to handle calculations.

…and yeah, it worked.
But then GPT casually said: “btw there’s a cleaner way that takes like a quarter of your code.”

