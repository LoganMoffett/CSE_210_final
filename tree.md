## Introduction

You can view the video and see the reading for a review of what the video covers [Tree](tree_1.mp4)

Part two of the tree videos are [tree_2](tree_2.mp4)

Have you ever wondered how your computer files system works? The simple answer is a really cool data  structure called a tree. A tree is a simply put just like a tree outside. It has a root or trunk that holds all the information and off of that trunk or root is branches and on those branches are more branches till you get out to the leaves. This is how a tree works in programming, just like a linked list that has pointers pointing to the next place in memory a tree has many pointers pointing to different data sets.

## Different tree's

There are two different types of trees we are going to talk about. A binary and non-binary tree. A Binary tree is a tree that has at most two branches attached to each node. It can have less then two but never more then two branches, while a binary tree can have an infinite amount of branches attached too each node.

## Binary Tree

Like discussed above a Binary Tree has only up too 2 branches attached to it. There are many advantages to using a binary tree. When storing information you can create a key or way of identifing where data is in the tree. For instance you can set it up so that left < right, which means if you are putting numbers in a tree that if the number is less then the node it will go to the left branch while if it is larger it goes to the right branch. When we build a tree this way, so long as it is balanced, it takes O(logn) time to find any information wihtin the tree! How cool is that, it makes it the fastest to find information out of arrays and linked lists, unless you know the index which would make an array win out. 

As you may have noticed I mentioned so long as the tree is balanced. You may be wonding what that means? I know I did when I first heard it. What it means is that no branch is larger or at least significantly larger then another branch. The instant you get one branch that is too big, it reduces the O(logn) time to navigate and it becomes O(n) time. At that point you might as well us a linked list as there are no more pros or cons other then it is harder to program. Many people will us what is called an AVL tree which is a self balancing tree or they will orginize the data before they start putting it into the tree.

## Non-binary tree

This is where the meat of this discussion is going to take place. The non-binary tree is used a lot esspecially in orginzing data. One downside is it is harder to create a key for non-binary tree's. However if you do create a key you can maintain the O(logn) time of the tree. However they are a lot harder to program than you binary tree. Because of this the example and homework problem that I am going to give you focus more on non-binary tree's rather then binary tree's simply because if you can program a non-binary tree then you can program a binary tree.

## Recursion

Before we get into programming tree's there is something that needs to be understood first, which is recursion. Recursion is a simple concept that is easy to grasp but hard to master, just like the piano. Recursion is when you call a function within itself. A simple example of it is below:

```python
def count(count):
    count(count + 1)
```

While this is a trivil example, you can see how the count function calls itself and then passes in count + 1 rather then count. However can you see a problem with this example? When will it end? This one never does, this is an example of where people often times mess up in recursion, which is not setting and end case or having an end case that will never be called. A better example would be

```python
def count(count):
    if count > 10:
        return count
    else:
        count(count + 1)
```

In this case we have an end statment that will eventually end the count function so that we can continue on the code without breaking it.

We are going to use recursion for navigating out tree's which is why I bring it up now. rather then leave you lost in the dust if you have never seen it before.

## Example

Here is the example code of tree's. You are going to see that there is a binary and non-binary tree exmaple.

[tree example](tree_example.py)

for a detailed explanation, see video 2 posted at the begining.

## Practice

What is the point in learning if you don't practice.

Your assignement is to build either code in the tree class or build a seperate class that will allow you to navigate the non-binary tree. This means that you can add information and go between the different branches to find different information. 

Use [practice](tree_practice.py) as your code to modify

## solution

Here is my [solution](tree_solution.py) to the practice

You can also view [solution video](tree_3.mp4) to watch a descriptive solution to the problem

Here is an updated [solution](tree_new_solution.py) that impliments the interface class functions into the tree class.

## Back to home

If you want to return to [home page](introduction.md)