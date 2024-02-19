# Recursion

## What is recursion

Recursion is a fundamental concept in computer science, cropping up in names like PHP and GNU, and finding its way into many algorithms. It's crucial to grasp because it offers a powerful strategy for problem-solving.

In essence, recursion involves solving a problem by breaking it down into smaller, more manageable sub-problems, repeatedly, until you reach a base case that you know how to solve outright. In programming, this translates to creating a function that calls itself to tackle these sub-problems, eventually leading to the solution of the larger problem.

Let's take a concrete example: summing all the numbers from 5 down to 1. We can view this as the sum of 5 plus the sum of all numbers from 4 down to 1, and so on, until we reach 1. Once we hit that base case of 1, we know the answer 1.  We then pass this solution back up the chain of function calls until we've pieced together the solution of the entire problem.

Here's how it looks in code:

```c
int sum(int n){
    if (n == 1){
        return 1;
    } else{
        return n + sum(n-1);
    }
}
```

A recursive function typically consists of two parts: the base case and the recursive case. The base case is the simplest subproblem that we can solve outright, serving as the termination point to prevent endless recursion. Without a proper base case, recursive functions could potentially run indefinitely, leading to program crashes. Our example above establishes the base case when the value of n is equal to 1.

The recursive case involves the function calling itself on a smaller sub-problem to contribute to solving the larger problem. With each iteration, the recursive case moves closer to the base case. In our example, the recursive case occurs when n is any value other than 1. The function breaks down the problem further by calling sum(n-1) and incorporating its solution.

## Why use recursion when we have loops?
Recursion can initially be challenging to grasp, leading newcomers to favor iterative methods like loops. Since loops are typically introduced first and seem more intuitive, recursion may not seem necessary at first glance. However, both recursion and loops are tools, each with its own strengths. There are situations where a recursive solution is simpler than using iteration, particularly for problems involving trees and graphs. While iteration can solve some tree and graph problems, it often results in more complex and harder-to-understand code. Sometimes, the simplest solution is the best, and it's up to the programmer to determine whether recursion or iteration is the most suitable tool for the task at hand.

## When to use recursion
Recursion is particularly well-suited for solving problems that can be broken down into smaller, repetitive sub-problems, especially those with multiple possible branches. Problems involving hierarchical or nested data structures like trees and graphs are prime candidates for recursion.

## When not to use recursion
Recursion may not be suitable in situations where memory is limited. Each recursive function call adds a new function call to the call stack, potentially consuming excessive memory. Additionally, recursion may not be ideal for problems where the same sub-problem is recomputed multiple times, leading to inefficiencies in both computation and memory usage.

## Memoization
Despite the computational intensity of recursive solutions, strategies like memoization can help make them more practical. Memoization involves storing the results of sub-problems to avoid recomputation. This approach significantly improves efficiency, as demonstrated in problems like the Fibonacci sequence. However, memoization comes with a trade-off of increased space complexity due to storing each solution.

Overall, recursion is a valuable tool that you'll encounter frequently in your programming journey, sometimes without even realizing it. It's essential to recognize that, like any tool, recursion has its appropriate applications and limitations. Understanding when to use recursion and when to explore alternative approaches is key to writing efficient and maintainable code. While recursion may not always be the optimal choice, it's a powerful technique worth mastering.







