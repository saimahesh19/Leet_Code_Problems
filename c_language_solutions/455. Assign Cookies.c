
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int findContentChildren(int* g, int gSize, int* s, int sSize) {
    int count = 0;
    
    // Sort both arrays
    qsort(g, gSize, sizeof(int), compare);
    qsort(s, sSize, sizeof(int), compare);

    // Iterate through the sorted arrays
    int i = 0, j = 0;
    while (i < gSize && j < sSize) {
        if (g[i] <= s[j]) {
            count++;
            i++; // Move to the next child
        }
        j++; // Move to the next cookie
    }

    return count;
}
