
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

extern unsigned long primeGap(const mpz_t a, const mpz_t b);
extern double getTime();

int main(int argc, char** argv) {

    if(argc < 3){
        printf("Usage: ./primegap a b\n");
        return 0;
    }
    
    double time = getTime();
    
    mpz_t a, b;
    
    unsigned long int la, lb;
    sscanf(argv[1], "%lu", &la);
    sscanf(argv[2], "%lu", &lb);
    
    mpz_init_set_str(a, argv[1], 10);
    mpz_init_set_str(b, argv[2], 10);
    
    unsigned long max_gap = primeGap(a, b);
    printf("\nLargest prime gap in [%ld, %ld] is %ld\n", la, lb, max_gap);
    time = getTime()-time;
    printf("computed in %.1e seconds\n\n", time);
    return 0;
}

