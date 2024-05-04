void moveZeroes(int* nums, int numsSize) {
    int j = 0;
    int num[numsSize]; // Creating a new array to store non-zero elements

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != 0) {
            num[j] = nums[i];
            j++;
        }
    }

    // Fill remaining elements of num with zeroes
    for (int i = j; i < numsSize; i++) {
        num[i] = 0;
    }

    // Copy elements of num back to nums
    for (int i = 0; i < numsSize; i++) {
        nums[i] = num[i];
    }
}
