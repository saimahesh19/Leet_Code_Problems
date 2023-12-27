int maxScore(char* s) {
    int max = 0, sum, countr, countl;

    for (int i = 0; i < strlen(s) - 1; i++) {
        countr = 0;
        countl = 0;

        char* left = (char*)malloc((i + 1) * sizeof(char));
        char* right = (char*)malloc((strlen(s) - i) * sizeof(char));

        if (left == NULL || right == NULL) {
            exit(1);
        }

        for (int j = 0; j <= i; j++) {
            left[j] = s[j];
            if (left[j] == '0') {
                countl++;
            }
        }

        for (int k = i + 1; k < strlen(s); k++) {
            right[k - (i + 1)] = s[k];
            if (right[k - (i + 1)] == '1') {
                countr++;
            }
        }

        sum = countr + countl;
        if (sum > max) {
            max = sum;
        }

        free(left);
        free(right);
    }

    return max;
}
