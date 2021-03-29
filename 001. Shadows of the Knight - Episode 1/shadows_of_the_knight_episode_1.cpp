#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


int main()
{
    //Instanciation des variables
    int W; // width of the building.
    int H; // height of the building.
    cin >> W >> H; cin.ignore();
    int N; // maximum number of turns before game over.
    cin >> N; cin.ignore();
    int X0;
    int Y0;
    int min_x = 0;
    int min_y = 0;
    int max_x = W;
    int max_y = H;
    cin >> X0 >> Y0; cin.ignore();

    // game loop
    while (1) {
        string bombDir; // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        cin >> bombDir; cin.ignore();

        if (bombDir.find("U") != std::string::npos) {
            max_y = Y0;
        }

        if (bombDir.find("D") != std::string::npos) {
            min_y = Y0;
        }

        if (bombDir.find("L") != std::string::npos) {
            max_x = X0;
        }

        if (bombDir.find("R") != std::string::npos) {
            min_x = X0;
        }

        if (bombDir.find("U") || bombDir.find("D")) {
            X0 = ceil((min_x + max_x) / 2);
        }

        if (bombDir.find("L") || bombDir.find("R")) {
            Y0 = ceil((min_y + max_y) / 2);
        }

        // the location of the next window Batman should jump to.
        cout << std::to_string(X0) + " " + std::to_string(Y0) << endl;
    }
}