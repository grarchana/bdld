#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()
{
  extern double potential (double x);
  extern double kernel (double x, double sigma);
  
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
  npoints_pot = (int) ( (range_pot - 0.1 * dx) / dx ) + 2;
  
  potential_array = (double *) calloc(npoints_pot, sizeof (double));
  boltz_array = (double *) calloc(npoints_pot, sizeof (double));
  boltz_array_conv = (double *) calloc(npoints_pot, sizeof (double));
  potential_array_conv = (double *) calloc(npoints_pot, sizeof (double));
  
  double sigma = 0.5;
  int npoints_kernel = 0;
  npoints_kernel = (int) ( (sigma - 0.1 * dx) / dx ) + 1;
  npoints_kernel = 2 * npoints_kernel + 1;  /* odd per construction */
  
  kernel_array = (double *) calloc( npoints_kernel, sizeof (double));

  int kount = 0;
  double x = 0.;

  for (kount = 0; kount < npoints_pot; ++kount)
    {
      x = xlower_pot + kount * dx;
      potential_array[kount] = potential(x);
      boltz_array[kount] = exp (- potential_array[kount]);
      boltz_array_conv[kount] = 0.;
    }

  int kount_kernel = 0;

  for (kount_kernel = 0; kount_kernel < npoints_kernel; ++kount_kernel)
    {
      x = - sigma + kount_kernel * dx;
      kernel_array[kount_kernel] = kernel(x, sigma);
      printf("%f %f\n", x, kernel_array[kount_kernel]);
    }

  int kount_target = 0;
  int kount_kernel_shifted = 0;

  /* this calculates the convolution */
  
  for (kount = 0; kount < npoints_pot; ++kount)
    {
      for (kount_kernel = 0; kount_kernel < npoints_kernel; ++kount_kernel)
	{
	  kount_kernel_shifted = - (npoints_kernel - 1) / 2 + kount_kernel;
	  kount_target = kount + kount_kernel_shifted;
	  if (kount_target >= 0 && kount_target < npoints_pot)
	    {
	      boltz_array_conv[kount_target] += \
		boltz_array[kount] * kernel_array[kount_kernel] * dx;
	    }
	}
    }

  for (kount = 0; kount < npoints_pot; ++kount)
    {
      potential_array_conv[kount] = - log (boltz_array_conv[kount]);
    }
  
  for (kount = 0; kount < npoints_pot; ++kount)
    {
      x = xlower_pot + kount * dx;
      printf("%f %f %f %f %f\n", x, potential_array[kount], \
	     boltz_array[kount], \
	     boltz_array_conv[kount], \
	     potential_array_conv[kount]);
    }
  
  exit(0);
}

double potential (double x)
{
  double potential_value = 0.;
  potential_value = x * x;
  potential_value = 0.25 * potential_value * potential_value \
    - 0.5 * potential_value;
  return (potential_value);
}

double kernel (double x, double sigma)
{
  double kernel_value = 0.;
  
  if (x <= - sigma)
    {
      return (kernel_value);
    }

  if (x >= sigma)
    {
      return (kernel_value);
    }

  if (x <= - 0.5 * sigma)
    {
      kernel_value = 1. + x / sigma;
      kernel_value = kernel_value * kernel_value;
      kernel_value = 2. * kernel_value / sigma;
      return (kernel_value);
    }

  if (x >= 0.5 * sigma)
    {
      kernel_value = 1. - x / sigma;
      kernel_value = kernel_value * kernel_value;
      kernel_value = 2. * kernel_value / sigma;
      return (kernel_value);
    }

  kernel_value = x / sigma;
  kernel_value = kernel_value * kernel_value;
  kernel_value = 1. - 2. * kernel_value;
  kernel_value = kernel_value / sigma;
  
  return (kernel_value);
} 
