
bool isSubsequence(char* s, char* t) {
    int count = 0;
    int j = 0;  // Use a separate index for the second string

    for (int i = 0; i < strlen(s); i++) {
        while (j < strlen(t)) {
            if (s[i] == t[j]) {
                count++;
                j++;  // Move to the next character in the second string
                break;
            }
            j++;
        }
    }

    return count == strlen(s);
}
