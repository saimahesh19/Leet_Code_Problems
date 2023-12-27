int maxArea(int* height, int heightSize) {
    int maxArea = 0;
    int left = 0, right = heightSize - 1;

    while (left < right) {
        int h = fmin(height[left], height[right]);
        int w = right - left;
        int area = h * w;
        maxArea = fmax(maxArea, area);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea;
}
