#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double potential(double x);
double gaussian_kernel(double x, double sigma);

int main()
{
    FILE *file = fopen("output_data.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file for writing\n");
        return EXIT_FAILURE;
    }

    extern double potential(double x);
    extern double gaussian_kernel(double x, double sigma);

    double *potential_array = NULL;
    double *boltz_array = NULL;
    double *boltz_array_conv = NULL;
    double *potential_array_conv = NULL;
    double *kernel_array = NULL;

    double dx = 0.01;

    double xlower_pot = -2.;
    double xupper_pot = 2.;
    double range_pot = xupper_pot - xlower_pot;
    int npoints_pot = 0;
    npoints_pot = (int)((range_pot - 0.1 * dx) / dx) + 2;

    potential_array = (double *)calloc(npoints_pot, sizeof(double));
    boltz_array = (double *)calloc(npoints_pot, sizeof(double));
    boltz_array_conv = (double *)calloc(npoints_pot, sizeof(double));
    potential_array_conv = (double *)calloc(npoints_pot, sizeof(double));

    double sigma = 0.5;
    int npoints_kernel = 0;
    npoints_kernel = (int)((sigma - 0.1 * dx) / dx) + 1;
    npoints_kernel = 2 * npoints_kernel + 1;  /* odd per construction */

    kernel_array = (double *)calloc(npoints_kernel, sizeof(double));

    int kount = 0;
    double x = 0.;

    for (kount = 0; kount < npoints_pot; ++kount)
    {
        x = xlower_pot + kount * dx;
        potential_array[kount] = potential(x);
        boltz_array[kount] = exp(-potential_array[kount]);
        boltz_array_conv[kount] = 0.;
    }

    int kount_kernel = 0;

    for (kount_kernel = 0; kount_kernel < npoints_kernel; ++kount_kernel)
    {
        x = -sigma + kount_kernel * dx;
        kernel_array[kount_kernel] = gaussian_kernel(x, sigma);
    }

    int kount_target = 0;
    int kount_kernel_shifted = 0;

    /* this calculates the convolution */

    for (kount = 0; kount < npoints_pot; ++kount)
    {
        for (kount_kernel = 0; kount_kernel < npoints_kernel; ++kount_kernel)
        {
            kount_kernel_shifted = -(npoints_kernel - 1) / 2 + kount_kernel;
            kount_target = kount + kount_kernel_shifted;
            if (kount_target >= 0 && kount_target < npoints_pot)
            {
                boltz_array_conv[kount_target] +=
                    boltz_array[kount] * kernel_array[kount_kernel] * dx;
            }
        }
    }

    for (kount = 0; kount < npoints_pot; ++kount)
    {
        potential_array_conv[kount] = -log(boltz_array_conv[kount]);
    }

    /* Write headings to the file */
    fprintf(file, "X\tPotential(X)\tExp(-Potential(X))\tConvolved Exp(-Potential(X))\tPotential from Convolved Density\n");

    for (kount = 0; kount < npoints_pot; ++kount)
    {
        x = xlower_pot + kount * dx;
        fprintf(file, "%.4f\t%.4f\t%.4f\t%.4f\t%.4f\n", x, potential_array[kount],
                boltz_array[kount], boltz_array_conv[kount], potential_array_conv[kount]);
    }

    fclose(file);

    free(potential_array);
    free(boltz_array);
    free(boltz_array_conv);
    free(potential_array_conv);
    free(kernel_array);

    return EXIT_SUCCESS;
}

double potential(double x)
{
    return x*x*x*x - 4*x*x + 0.2*x;
}

double gaussian_kernel(double x, double sigma)
{
    double coeff = 1.0 / (sqrt(2.0 * M_PI) * sigma);
    double exponent = -0.5 * (x * x) / (sigma * sigma);
    return coeff * exp(exponent);
}

