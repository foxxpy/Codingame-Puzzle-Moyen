using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player
{
    static void Main(string[] args)
    {
        string[] inputs;
        inputs = Console.ReadLine().Split(' ');
        int W = int.Parse(inputs[0]); // width of the building.
        int H = int.Parse(inputs[1]); // height of the building.
        int N = int.Parse(Console.ReadLine()); // maximum number of turns before game over.
        inputs = Console.ReadLine().Split(' ');
        int X0 = int.Parse(inputs[0]);
        int Y0 = int.Parse(inputs[1]);
        int min_x = 0;
        int max_x = W;
        int min_y = 0;
        int max_y = H;

        // game loop
        while (true)
        {
            string bombDir = Console.ReadLine(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

            if (bombDir.Contains("U"))
            {
                max_y = Y0;
            }

            if (bombDir.Contains("D"))
            {
                min_y = Y0;
            }

            if (bombDir.Contains("L"))
            {
                max_x = X0;
            }

            if (bombDir.Contains("R"))
            {
                min_x = X0;
            }

            if (bombDir.Contains("U") || bombDir.Contains("D"))
            {
                Y0 = (min_y + max_y) / 2;
            }

            if (bombDir.Contains("L") || bombDir.Contains("R"))
            {
                X0 = (min_x + max_x) / 2;
            }

            Console.WriteLine(X0.ToString() + " " + Y0.ToString());
        }
    }
}