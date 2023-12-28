int compress(char* chars, int charsSize) {
    if (charsSize <= 1) {
        return charsSize;
    }

    char* result = (char*)malloc(2 * charsSize * sizeof(char));
    int resultIndex = 0, count = 1;

    for (int i = 1; i <= charsSize; i++) {
        if (i < charsSize && chars[i] == chars[i - 1]) {
            count++;
        } else {
            result[resultIndex++] = chars[i - 1];

            if (count > 1) {
                char countStr[5];  // Assuming the count won't exceed 9999
                int digits = 0;

                // Convert count to characters
                while (count > 0) {
                    countStr[digits++] = '0' + (count % 10);
                    count /= 10;
                }

                // Append count characters to the result array
                while (digits > 0) {
                    result[resultIndex++] = countStr[--digits];
                }
                
                count = 1;
            }
        }
    }

    // Null-terminate the result string
    result[resultIndex] = '\0';

    // Update the original chars array
    strcpy(chars, result);

    free(result);

    return strlen(chars);
}
