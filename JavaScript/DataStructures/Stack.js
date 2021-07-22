// Stack class
class Stack {
  // Array is used to implement stack
  constructor() {
    this.items = [];
  }

  // Functions to be implemented
  push(item) {
    this.items.push(item);
  }

  pop() {
    if (this.items.length > 0) {
      this.items.pop();
    } else {
      return "Item cannot be popped. Stack is empty.";
    }
  }

  peek() {
    let len = this.items.length;
    return this.items[len - 1];
  }

  isEmpty() {
    let len = this.items.length;
    if (len === 0) {
      return true;
    } else {
      return false;
    }
  }

  printStack() {
    str = "";
    let len = this.items.length;

    for (i = 0; i < len; i++) {
      str += this.items[i] + " ";
    }

    return str;
  }
}

// creating object for stack class
var stack = new Stack();

// testing isEmpty and pop on an empty stack

// returns false
console.log(stack.isEmpty());

// returns Underflow
console.log(stack.pop());
