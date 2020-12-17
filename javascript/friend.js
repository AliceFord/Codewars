function friend(friends){
  var output = [];
  for (var i = 0; i < friends.length; i++) {
    if (friends[i].length === 4) output.push(friends[i]);
  }
  return output
}

console.log(friend(["Ryan", "Kieran", "Mark"]));