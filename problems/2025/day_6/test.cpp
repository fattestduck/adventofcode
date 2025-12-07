// Advent of Code 2025 Day 6
#include <math.h>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;


vector<string> initialVector{};
vector<vector<string>> Rows;
ifstream PuzzleInput("AdventOfCode25D6.txt");
string line;


void generateInitialVector() {
  if (PuzzleInput.is_open()) {
    while (getline(PuzzleInput, line)) {
      initialVector.push_back(line);
    }
  }
}


void separateInitalVector() {
  string value;
  vector<string> tempRow;


  for (string line : initialVector) {
    stringstream stream(line);
    for (char character : line) {
      while (stream >> value) {
        tempRow.push_back(value);
      }
    }
    Rows.push_back(tempRow);
    tempRow.clear();
  }
}


int main() {
  long total = 0;


  generateInitialVector();
  separateInitalVector();


  for (int i = 0; i <= Rows[0].size() - 1; i++) {
    if (Rows[4][i] == "+") {
      cout << "add" << endl;
      total += (stol(Rows[0][i]) + stol(Rows[1][i]) + stol(Rows[2][i]) + stol(Rows[3][i]));
    } else {
      cout << "mult" << endl;
      total += (stol(Rows[0][i]) * stol(Rows[1][i]) * stol(Rows[2][i]) * stol(Rows[3][i]));
    }
  }
  cout << total << endl;
}