#include <stdio.h>

void print(int* memo, int size){
    printf("\n");
   for (int i =0; i < size-1; i++){
        printf("%d ", memo[i]);
    };
    printf("\n");

}

int fibonacci(int num, int* memo, int size){

    // print(memo, size);

    if (memo[num] == -1){
        memo[num] = fibonacci(num-1, memo, size) + fibonacci(num-2, memo, size);
    }

    return memo[num];
}

int main(){
    int N = 15;
    int cache[N];
    for(int i = 0; i < N; i++){
        cache[i] = -1;
    }

    // print(cache, N);
    
    cache[0] = 1;
    cache[1] = 1;

    printf("\n%d\n", fibonacci(N-1, cache, N));
    // print(cache, N);
  
    return 0;
} 