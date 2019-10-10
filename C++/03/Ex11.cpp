#include <iostream>
using namespace std;

int main() {
    double pennie, nickel, dime, quarter, half_dollar, one_dollar;
    cout << "How many pennies do you have?  ";
    cin >> pennie;
    cout << "How many nickels do you have?  ";
    cin >> nickel;
    cout << "How many dimes do you have?  ";
    cin >> dime;
    cout << "How many quarters do you have?  ";
    cin >> quarter;
    cout << "How many half dollars do you have?  ";
    cin >> half_dollar;
    cout << "How many one dollars do you have?  ";
    cin >> one_dollar;
    double total = pennie + 5 * nickel + 10 * dime + 25 * quarter + 50 * half_dollar + 100 * one_dollar;
    
    cout << "原始版本：\n";
    cout << "You have " << pennie << " pennies."
         << "\nYou have " << nickel << " nickels."
         << "\nYou have " << dime << " dimes."
         << "\nYou have " << quarter << " quarters."
         << "\nYou have " << half_dollar << " half dollars."
         << "\nYou have " << one_dollar << " one dollars."
         << "\nThe value of all of your coins is " << total << " cents.\n";
    
    string pennie_plural, nickel_plural, dime_plural, quarter_plural, half_dollar_plural, one_dollar_plural;
    pennie_plural = (pennie == 1) ? " pennie." : " pennies.";
    nickel_plural = (nickel == 1) ? " nickel." : " nickels.";
    dime_plural = (dime == 1) ? " dime." : " dimes.";
    quarter_plural = (quarter == 1) ? " quarter." : " quarters.";
    half_dollar_plural = (half_dollar == 1) ? " half_dollar." : " half dollars.";
    one_dollar_plural = (one_dollar == 1) ? " one_dollar." : " one dollars.";
    cout << "改进版本：\n";
    cout << "You have " << pennie << pennie_plural
         << "\nYou have " << nickel << nickel_plural
         << "\nYou have " << dime << dime_plural
         << "\nYou have " << quarter << quarter_plural
         << "\nYou have " << half_dollar << half_dollar_plural
         << "\nYou have " << one_dollar << one_dollar_plural
         << "\nThe value of all of your coins is $" << total/100.0 << "\n";
    return 0;
}