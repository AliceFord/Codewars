function songDecoder(song){
  song = song.split("WUB").join(" ");
  song += ' ';
  output = "";
  for (let i = 0; i < song.length - 1; i++) {
    if (!(song[i] === ' ' && song[i+1] === ' ')) output += song[i];
  }
  return output.trim();
}

console.log(songDecoder("AWUBWUBWUBBWUBWUBWUBC"))