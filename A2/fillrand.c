#include <stdio.h>
#include <stdlib.h>

void fill_random(int m, int n, int p, double A[], double B[]){

  int i=0, j=0;

  for(i=0;i<m*n;i++){
    A[i] = drand48();
  }
  for(j=0;j<n*p;j++){
    B[j] = drand48();
  }

}
