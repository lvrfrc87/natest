Simple package to run unit test for network automation python3 code.

Explanation by examples:

INPUT can be either a file or a return str() or list() Usually is the output of a show command
```
input = open('../fixtures/ssh_input', 'r')
```

HAVE is the return of you code run on top of INPUT
```
have = open('../fixtures/have', 'r')
```

WANT must be a file where you have your expected output
```
want = open('../fixtures/want', 'r')
```

Create an instance of NaTest
```
my_test = NaTest()
```

print the input. Ideally the input is saved in a variable and use to run your code (instead of run real ssh commands)
```
print(my_test.read(input))
```

print diff between what we HAVE and what we WANT
```
print(my_test.result(want, have))
```

Result (compared WANT against HAVE after running code using INPUT):
```
['+ This is an extra line\n']
['- This is a missing line\n']
```
