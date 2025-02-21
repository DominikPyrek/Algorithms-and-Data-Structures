class Node {
  constructor(data) {
    this.next = null;
    this.data = data;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  addAtTheStart(data) {
    let node = new Node(data);
    if (this.head === null) {
      this.head = node;
    } else {
      node.next = this.head;
      this.head = node;
    }
  }

  addAtTheEnd(data) {
    let node = new Node(data);
    if (this.head === null) {
      this.head = node;
    }
    let currentNode = this.head;
    while (currentNode.next) {
      currentNode = currentNode.next;
    }
    currentNode.next = node;
  }

  addAtTheIndex(data, index) {
    let node = new Node(data);
    let indexNow = 0;
    let currentNode = this.head;
    if (index < 0 || index > (this.lenght() + 1)) {
      console.log("Nie poprawny index")
      return;
    }
    while (currentNode.next && index > indexNow) {
      currentNode = currentNode.next;
    }
    currentNode.next = node;
  }

  deleteAtTheStart() {
    if (this.head === null) {
      return
    }
    this.head = this.head.next;
  }

  deleteAtTheEnd() {
    let currentNode = this.head;
    if (this.head === null) {
      return;
    }
    if (this.head.next === null) {
      this.head = null;
      return;
    }
    while (currentNode.next.next) {
      currentNode = currentNode.next;
    }
    currentNode.next = null;
  }


  lenght() {
    let len = 0;
    let currentNode = this.head;
    while (currentNode) {
      len += 1
      currentNode = currentNode.next;
    }
    return len;
  }

  logIt() {
    let str = "";
    let currentNode = this.head;
    while (currentNode) {
      if (currentNode.next === null) {
        str += currentNode.data;
        break;
      }
      str += currentNode.data + "-->";
      currentNode = currentNode.next;
    }
    console.log(str);
  }
}

let LL = new LinkedList

LL.addAtTheStart(8)
LL.addAtTheStart(12)
LL.addAtTheEnd(16)
LL.addAtTheIndex(21, 2)
LL.logIt()
LL.deleteAtTheStart()
LL.deleteAtTheEnd()
LL.logIt()
console.log(LL.lenght())


