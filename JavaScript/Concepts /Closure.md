# Closure 

[Link to Mozilla Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)   
[https://hyunseob.github.io/2016/08/30/javascript-closure/](https://hyunseob.github.io/2016/08/30/javascript-closure/) 


A closure gives you access to an outer function’s scope from an inner function.   
In JavaScript, closures are created every time a function is created, at function creation time.

```
function init() {
  var name = 'Mozilla'; // name is a local variable created by init
  function displayName() { // displayName() is the inner function, a closure
    alert(name); // use variable declared in the parent function
  }
  displayName();
}
init();
``` 

- In the code, `displayName()` function is an inner function (defined inside `init()`)
- It is available only within the body of the `init()` function. 
- The inner function `displayName()` can have access to the variables of the outer functions,   
  it can access the variable `name` declared in the parent function `init()` 



**ex 2)** 
```
function makeFunc() {
  var name = "Mozilla";
  function displayName() {
    alert(name);
  }
  return displayName;
}

var myFunc = makeFunc();
// returns displayName to myFunc 
// also maintains the lexicographical scope 

myFunc();
// run the returned function displayName (accessing name variable)
```
- JS returns the function, and the function that returns the inner function forms a closure. 
- Closure is a combination of **function and the lexical environment** within which the funcion that was declared.  
  - The environment can consist of local variables that were in scope at the time the closure was created. 
  - `myFunc` is a **reference** to the instance of the function `displayName` that is created when `makeFunc` is run. 
  - The instance of `displayName` maintains a refernce to its lexical environment, within which the variable `name` exists. 


**ex 3)** 
```
var base = 'Hello, ';
function sayHelloTo(name) {
  var text = base + name;
  return function() {
    console.log(text);
  };
}

var hello1 = sayHelloTo('A');
var hello2 = sayHelloTo('B');
var hello3 = sayHelloTo('C');
hello1(); // 'Hello, A'
hello2(); // 'Hello, B'
hello3(); // 'Hello, C'
``` 
- It may seem that `text` might be changing dynamically, BUT, there are 3 different creation of `text` variable. 
- In other words, each function `hello1()`, `hello2()`, `hello3()` have different lexical environment. 


### Data Hiding (은닉화)
With OOP using JS, we might want to prevent private variables to be accessed. 
One way to do this is through using closures. 

```
function age(age) {
  var _age = age;         // the underbar(_) denotes that we want this variable to be a private one. 
  return function() {
    console.log('You are, ' + _age + ' years old');
  };
}

var age1 = age(57);
var age2 = age(25);
var age3 = age(1);

age1(); // 'You are, 57 years old'
age2(); // 'You are, 25 years old'
age3(); // 'You are, 1 years old'
``` 


  
### Other Useful Utilizations   
  
  
Printing out `i` from the anonymous function of the `setTimeout()` 
```
var i;
for (i = 0; i < 10; i++) {
  setTimeout(function() {
    console.log(i);
  }, 100);
}

// returns 10, ten times 
``` 
The code above returns 10, ten times, because the anonymous function that was passed to `setTimeout()` will be called after 0.1 secoond (100 millisecond), and by then the for loop had already finished executing, and the anonymous function will only be able to refer to `i`, which would be 10 already.  

Alternatively, closures can be used to properly print out the values. 

```
var i;
for (i = 0; i < 10; i++) {
  (function(j) {        // usage of IIFE or Immediately Invoked Function Expression 
    setTimeout(function() {
      console.log(j);
    }, 100);
  })(i);
}

// returns 
1 
2
3
...
``` 
Here, an IIFE (Immediately Invoked Function Expression) is used to make the anonymous function a closure. (A closure has access to the lexical environment that it was created)

In the code above, `i` would be passed as a parameter of value `j`, and each time the function is created, it would be in a different environment. 

In total, because the loop runs 10 times, there would be 10 environments created, and 10 different `j`s created. 

Most of the cases, passing `i` would be ideal, as we want to create different versions of `i` for the closure. 



### Performance 
Closures each have their own environment, which takes up spaces in the memory. While closures are being used, GC does not collect the memory that is occupied by the variables that the closure refers to. 

Ideally, it would be best to remove these references once the closures are done being used. 


```
function age(age) {
  var _age = age;         // the underbar(_) denotes that we want this variable to be a private one. 
  return function() {
    console.log('You are, ' + _age + ' years old');
  };
}

var age1 = age(57);
var age2 = age(25);
var age3 = age(1);

age1(); // 'You are, 57 years old'
age2(); // 'You are, 25 years old'
age3(); // 'You are, 1 years old'

age1 = null; 
age2 = null; 
age3 = null;
``` 