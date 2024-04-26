#include <iostream>
#include <cmath>
#include <vector>
#include <cstdlib>


int main() {
    int Nx = 10;
    int Ny = 5;
    int Nt = 100;

    int alfa = 1;

    double dtdx  = 0.20;
    double dtdy  = 0.20;

    //create a vector that holds a 3d matrix of doubles
    std::vector<std::vector<std::vector<double>>> u(Nx, std::vector<std::vector<double>>(Ny, std::vector<double>(Nt, 23.8)));
    //Initialize the matrix
    for(int j = 0; j < Ny; j++) {
        for(int n = 0; n < Nt; n++) {
            u[0][j][n] = 77;
        }
    }
    


    int ddx = 0;
    int ddy = 0;
    for(int n = 0; n < Nt; n++) {
        for(int i = 1; i < Nx - 1; i++) {
            for(int j = 1; j < Ny - 1; j++) {
                ddx = (u[i + 1][j][n] - 2 * u[i][j][n] + u[i - 1][j][n]);
                ddy = (u[i][j + 1][n] - 2 * u[i][j][n] + u[i][j - 1][n]);
                u[i][j][n + 1] = u[i][j][n] + alfa * dtdx * ddx + alfa * dtdy * ddy;
            }
        }
    }


    //write u to a file
    FILE *f = fopen("heat_equation.txt", "w");
    fprintf(f, "%d\n%d\n%d\n", Nx, Ny, Nt);
    for(int n = 0; n < Nt; n++) {
        for(int i = 0; i < Nx; i++) {
            for(int j = 0; j < Ny; j++) {
                fprintf(f, "%f\n", u[i][j][n]);
            }
        }
    }
    fclose(f);
    system("python3 animator.py");
}