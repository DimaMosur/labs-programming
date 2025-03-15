#include <stdio.h>
#include <stdlib.h>

void zigzag_traversal(int **garden, int row_count, int col_count, int *result) {
    int result_index = 0;
    for (int row = 0; row < row_count; row++) {
        if (row % 2 == 0) {
            for (int col = 0; col < col_count; col++) {
                result[result_index++] = garden[row][col];
            }
        } else {
            for (int col = col_count - 1; col >= 0; col--) {
                result[result_index++] = garden[row][col];
            }
        }
    }
}

int main() {
    int row_count = 4, col_count = 4;
    int garden_data[4][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    int **garden = (int **)malloc(row_count * sizeof(int *));
    for (int row = 0; row < row_count; row++) {
        garden[row] = (int *)malloc(col_count * sizeof(int));
        for (int col = 0; col < col_count; col++) {
            garden[row][col] = garden_data[row][col];
        }
    }

    int *result = (int *)malloc(row_count * col_count * sizeof(int));
    zigzag_traversal(garden, row_count, col_count, result);

    for (int index = 0; index < row_count * col_count; index++) {
        printf("%d ", result[index]);
    }

    for (int row = 0; row < row_count; row++) {
        free(garden[row]);
    }
    free(garden);
    free(result);

    return 0;
}
