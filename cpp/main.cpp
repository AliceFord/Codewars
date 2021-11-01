#include <bits/stdc++.h>

using namespace std;

class Ball {
public:
  static int maxBall(float v0) {
    v0 = v0 / 3.6;
    const float g = 9.81;
    pair<float, int> max = make_pair(0,0);
    float current = 0;
    for (float t=0;;t+=0.1) {
      current = (v0 * t) - (0.5 * g * t * t);
      if (current < max.first) {
        if (current > 22)
          return max.second + 1;
        else
          return max.second;
      }
      max.first = current;
      max.second = (t*10);
    }
  }
};

unsigned long long numPrimorial (unsigned short int number ) {
  int primeCount = 0;
  int i = 1;
  int currentTotal = 1;
  while (primeCount < number) {
    i++;
    bool f = true;
    for (int j=2;j<i;j++)
      if (i%j==0)
        f = false;
    if (f) {
      primeCount++;
      currentTotal *= i;
    }
  }
  return currentTotal;
}

vector<string> dup(vector<string> arr) {
  vector<string> ans(arr.size(), "");
  for (int i=0;i<arr.size();i++) {
    string word = arr[i];
    char prevChar = ' ';
    for (char c : word) {
      if (prevChar != c)
        ans[i] += c;
      prevChar = c;
    }
  }
  return ans;
} // My answer
vector<string> dupA(vector<string> ss) {
  for (auto& s : ss)
    s.erase(unique(s.begin(), s.end()), s.end());
  return ss;
} // Best answer

int skipToNextBracket(int pos, const string &code) {
  int depth = 0;
  while (1) {
    pos++;
    if (code[pos] == '[') {
      depth++;
    }
    if (code[pos] == ']') {
      if (depth == 0) {
        return ++pos;
      }
      else {
        depth--;
      }
    }
  }
}

int skipBackBracket(int pos, const string &code) {
  int depth = 0;
  while (1) {
    pos--;
    if (code[pos] == ']') {
      depth++;
    }
    if (code[pos] == '[') {
      if (depth == 0) {
        return pos;
      }
      else {
        depth--;
      }
    }
  }
}

string brainLuck(const string &code, string input) {
  const int MxN = 1000;
  unsigned char data[MxN]{0};
  int pos = 0;
  unsigned long i=0;
  string output = "";
  while (i < code.size()) {
    //for (int j=0;j<20;j++) cout << (int)data[j] << " ";
    //cout << "\n";
    char ins = code[i];
    switch (ins) {
    case '>':
      pos++;
      break;
    case '<':
      pos--;
      break;
    case '+':
      data[pos]++;
      break;
    case '-':
      data[pos]--;
      break;
    case ',':
      data[pos] = input[0];
      input.erase(input.begin());
      break;
    case '.':
      output += data[pos];
      break;
    case '[':
      if (data[pos] == 0) {
        i = skipToNextBracket(i, code);
      }
      break;
    case ']':
      if (data[pos] != 0) {
        i = skipBackBracket(i, code);
      }
      break;
    default:
      cout << 1 << "\n";
      break;
    }

    i++;
  }
  return output;
}



int main() {
  //cout << Ball::maxBall(99);
  //cout << numPrimorial(5);
  // for (string s : dup(vector<string>{"kelless","keenness"})) {
  //   cout << s << "\n";
  // }
  //cout << get_order("pizzachickenfriesburgercokemilkshakefriessandwich");
  std::string dw;
  dw.append(1, (char) 7);
  dw.append(1, (char) 3);
  std::string result;
  result.append(1, (char)21);
  cout << brainLuck(",>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.",dw) << "\n";
  cout << result << "\n";
}
