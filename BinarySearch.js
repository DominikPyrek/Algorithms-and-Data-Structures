
let LL = []
let x = 0
while (x < 100) {
  LL.push(x);
  x++;
  x++;
}


function Binarysearch(List, searchFor) {
  let startOfList = 0;
  let endOfList = List.length - 1;
  while (startOfList <= endOfList) {
    let middleOfList = Math.floor((startOfList + ((endOfList - startOfList) / 2)))
    if (List[middleOfList] == searchFor) {
      return middleOfList;
    }
    else if (List[middleOfList] < searchFor) {
      startOfList = middleOfList + 1;
    }
    else {
      endOfList = middleOfList - 1;
    }
  }
  return "nie znaleziono liczby"
}

console.log(Binarysearch(LL, 2))

