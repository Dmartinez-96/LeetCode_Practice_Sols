#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to compute the greatest common divisor (GCD) of two integers
int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

char* gcdOfStrings(char* str1, char* str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);

    // Allocate memory for concatenated strings
    char* concat1 = (char*)malloc(len1 + len2 + 1);
    char* concat2 = (char*)malloc(len1 + len2 + 1);

    if (!concat1 || !concat2) {
        // Memory allocation failed
        free(concat1);
        free(concat2);
        return NULL;
    }

    // Concatenate str1 + str2 into concat1
    strcpy(concat1, str1);
    strcat(concat1, str2);

    // Concatenate str2 + str1 into concat2
    strcpy(concat2, str2);
    strcat(concat2, str1);

    // Check if the two concatenated strings are equal
    if (strcmp(concat1, concat2) != 0) {
        // They are not equal; free memory and return empty string
        free(concat1);
        free(concat2);
        char* empty = (char*)malloc(1);
        if (empty) {
            empty[0] = '\0';
        }
        return empty;
    }

    // They are equal; compute GCD of lengths
    int max_len = gcd(len1, len2);

    // Allocate memory for the result string
    char* result = (char*)malloc(max_len + 1);
    if (!result) {
        // Memory allocation failed
        free(concat1);
        free(concat2);
        return NULL;
    }

    // Copy the prefix of str1 up to max_len into result
    strncpy(result, str1, max_len);
    result[max_len] = '\0'; // Null-terminate the result string

    // Free the concatenated strings
    free(concat1);
    free(concat2);

    return result;
}
