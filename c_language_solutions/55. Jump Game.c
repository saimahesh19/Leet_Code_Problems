#include <stdbool.h>

bool canJump(int* nums, int numsSize) {
    int i = 0;
    if(numsSize==1){
        return true;
    }
    while (i < numsSize) {
        // If the current element is 0, find the next non-zero element to jump
        if (nums[i] == 0) {
            int j = i - 1;
            while (j >= 0 && nums[j] <= i - j) {
                j--;
            }

            // If no such element is found, return false
            if (j < 0) {
                return false;
            }

            i = j; // Jump to the new position
        } else {
            int jump = nums[i];

            // If the jump takes us to or beyond the end of the array, return true
            if (i + jump >= numsSize - 1) {
                return true;
            }

            // Update the position using the jump value
            i += jump;
        }
    }

    return false;
}
