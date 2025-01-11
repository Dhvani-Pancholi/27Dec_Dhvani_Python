##### Difference between yield and return.

|Yield|Return|
| --- | --- |
|Yield is generally used to convert a regular Python function into a generator.|Return is generally used for the end of the execution and “returns” the result to the caller statement.
|It replace the return of a function to suspend its execution without destroying local variables.|It exits from a function and handing back a value to its caller.
|It is used when the generator returns an intermediate result to the caller.|It is used when a function is ready to send a value.
|Code written after yield statement execute in next function call.|while, code written after return statement wont execute.
|It can run multiple times.|It only runs single time.
