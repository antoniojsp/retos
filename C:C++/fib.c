#include <stdio.h>

int fibonacci(int num, int* memo){

    if (memo[num] == -1){
        memo[num] = fibonacci(num-1, memo) + fibonacci(num-2, memo);
    }

    return memo[num];
}

int main(){
    int N = 10;
    int cache[N];
    for(int i = 0; i < N; i++){
        cache[i] = -1;
    }

    for(int i = 0; i < N; i++){
        printf("%d", cache[i]);
    }    
    
    cache[0] = 1;
    cache[1] = 1;

    printf("\n%d\n", fibonacci(N-1, cache));
  
    return 0;
} 