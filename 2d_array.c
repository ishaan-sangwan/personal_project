#include <stdio.h>

int main() {
    int matrix[3][3];
    int i, j;
    int tr_matrix[3][3];
    for (i=0; i<3;i++){
        for (j=0;j<3;j++){
            printf("please enter the the eleemet");
            scanf("%d", &matrix[i][j]);
        }
    }
    for (i=0;i<3;i++){
        for(j=0;j<3;j++){
            tr_matrix[j][i] = matrix[i][j];
        }
    }
    return 0;
}
