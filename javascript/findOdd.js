function findOdd(a) {
    var aArray = [];
    for (var i = 0; i < a.length; i++) aArray[a[i]] = 0;
    for (var i = 0; i < a.length; i++) aArray[a[i]] += 1;
    for (var i = 0; i < aArray.length; i++) {
        if (aArray[i] % 2 === 1) return i;
    }
    console.log(a, aArray);
    return -1;
}

console.log(findOdd([1, 2, 0, 2, 0, 1, 1]));