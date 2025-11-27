#include <iostream>

using namespace std;

int main() {
  string name;
  int planet;
  double weight;

  cout << "What is your name? ";
  cin >> name;
  cout << "What is your weight? ";    
  cin >> weight;
  cout << "What is the planet that you're on? ";
  cin >> planet;

  switch (planet){
    case 1:
      cout << "Your weight on " << planet << " is " << (weight * .38) << "kg.\
      n";
      break;
    case 2:
      cout << "Your weight on " << planet << " is " << (weight * .91) << "kg.\
      n";
      break;
    case 3:
      cout << "Your weight on " << planet << " is " << (weight * .38) << "kg.\
      n";
      break;
    case 4:
      cout << "Your weight on " << planet << " is " << (weight * 2.34) << "kg.\
      n";
      break;
    case 5:
      cout << "Your weight on " << planet << " is " << (weight * 1.06) << "kg.\
      n";
      break;
    case 6:
      cout << "Your weight on " << planet << " is " << (weight * .92) << "kg.\
      n";
      break;
    case 7:
      cout << "Your weight on " << planet << " is " << (weight * 1.19) << "kg.\
      n";
      break;
  }
  
}