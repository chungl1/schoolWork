#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <sys/resource.h>
#include <unistd.h>

#define N 50

extern unsigned long primeGap(const mpz_t a, const mpz_t b);

unsigned long primeGap(const mpz_t a, const mpz_t b){
 
  int value;
  mpz_t val1, val2, max, subValue;
  unsigned long newMax;

  mpz_init(max);
  mpz_init(subValue);
  mpz_init(val1);
  mpz_init(val2);

  mpz_set(val1, a);

  while(mpz_cmp(b,val1)>0){

    value = mpz_probab_prime_p(val1, N);
    if(value == 2 || value == 1){
      mpz_nextprime(val2, val1);
      mpz_sub(subValue, val2, val1); 
      if(mpz_cmp(subValue, max)>0){
         mpz_set(max, subValue);
         
      }
      mpz_set(val1, val2);
    } 
    else 
      mpz_add_ui(val1,val1,1);    
  }
  newMax = mpz_get_ui(max);

  return newMax;           
} 
  
 
