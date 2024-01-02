int triangularSum(int* nums, int numsSize) {
    int n = numsSize;

    // Create a 2D array to store intermediate results
    int a[n][n];

    // Initialize the first row of the array
    for (int i = 0; i < n; i++) {
        a[0][i] = nums[i];
    }

    // Perform the triangular sum calculation
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            a[i][j] = (a[i - 1][j] + a[i - 1][j + 1]) % 10;
        }
    }

    // Return the triangular sum
    return a[n - 1][0];
}
