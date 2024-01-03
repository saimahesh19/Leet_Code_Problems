
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    if (nums == NULL || numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    int leftProducts[numsSize];
    int rightProducts[numsSize];

    leftProducts[0] = 1;
    for (int i = 1; i < numsSize; i++) {
        leftProducts[i] = leftProducts[i - 1] * nums[i - 1];
    }

    rightProducts[numsSize - 1] = 1;
    for (int i = numsSize - 2; i >= 0; i--) {
        rightProducts[i] = rightProducts[i + 1] * nums[i + 1];
    }
    for (int i = 0; i < numsSize; i++) {
        nums[i] = leftProducts[i] * rightProducts[i];
    }
    *returnSize = numsSize;
    return nums;
}
