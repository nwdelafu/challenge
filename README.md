## Coding Challenge for Data Incubator


## Challenge Description
Write a program that reads a list of numbers and for each number outputs an estimate of the running mean, running standard deviation, and running median.  The input should be read from standard in, with one number per line.  For each line of input, the program should print to standard out the estimated running mean, running standard deviation, and running median.  That is, given the input:

```python
1
2
3
137.036
```

The program should output values close to
```python
1,0,1

1.5,0.5,1.5

2,0.816,2

35.759,58.477,2.5
```

#### Some notes:

* Using either the biased or unbiased estimate of the standard deviation is fine, but you should report a number even for the first step.
* There are several ways to define the median for an even number of samples; you may use any of these definitions.
Output numbers at a reasonable precision.
* You will probably have to strike a balance between the accuracy of the results and  resources your program requires.  Choose a sensible tradeoff.  Better yet, allow this to be configurable.
* Ideally, this program should be able to handle arbitrarily long lists of inputs.  It would be nice for it to output results as soon as possible, instead of needing to wait for all of standard in to be read.  You do not have to worry about malicious input (there won’t be 10 GB on a single line), but gracefully handling malformed input lines is a plus.
* Upload your solution to the public DVCS host of your choice, and send us a link to the repository.  You may use any programming language or packages you like, but if you use anything outside of Python 3, Pandas, or Numpy, please include instructions to help us run your code.

 