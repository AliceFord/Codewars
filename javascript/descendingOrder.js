function descendingOrder(n){
    n = Array.from(String(n), Number);
    n = n.sort((a, b)=>{return b-a})
    return n.toString();
}

console.log(descendingOrder(12));