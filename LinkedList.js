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

  deleteAtTheStart() {
    this.head = this.head.next;
  }
  deleteAtTheEnd() {
    let currentNode = this.head;
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
    console.log("Lenght is " + len);
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
LL.deleteAtTheStart()
LL.deleteAtTheEnd()
LL.deleteAtTheEnd()
LL.logIt()
LL.lenght()


