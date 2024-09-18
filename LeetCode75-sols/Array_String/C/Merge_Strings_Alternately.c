#include <stdlib.h>
#include <string.h>

char * mergeAlternately(char * word1, char * word2){
    int len1 = strlen(word1);
    int len2 = strlen(word2);
    int total_len = len1 + len2;

    // Allocate memory for merged str with +1 for null terminator
    char *mergestr = (char *)malloc(total_len + 1);
    if (!mergestr) {
        return NULL; // failed allocation
    }
    
    // Index words and mergestr
    int i = 0;
    int k = 0;

    // Merge alternately
    while ((i < len1) || (i < len2)) {
        if (i < len1) {
            mergestr[k++] = word1[i];
        }
        if (i < len2) {
            mergestr[k++] = word2[i];
        }
        i++;
    }

    mergestr[k]='\0'; // Null-terminate the merged string
    return mergestr;
}
