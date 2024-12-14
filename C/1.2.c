#include <stdio.h>
#include <stdlib.h>

// Funkce pro porovnání čísel (pro qsort)
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    FILE *file = fopen("1.txt", "r"); // Otevření souboru
    if (file == NULL) {
        perror("Chyba při otevírání souboru");
        return 1;
    }

    int left[1002], right[1002]; // Předpokládáme maximálně 100 hodnot v každém seznamu
    int left_count = 0, right_count = 0;

    // Čtení čísel ze souboru
    while (!feof(file)) {
        int l, r;
        if (fscanf(file, "%d %d", &l, &r) == 2) {
            left[left_count++] = l;
            right[right_count++] = r;
        }
    }

    fclose(file);

    // Seřazení obou seznamů
    qsort(left, left_count, sizeof(int), compare);
    qsort(right, right_count, sizeof(int), compare);

    // Výpočet součtu vzdáleností
    int total_distance = 0;
    for (int i = 0; i < left_count; i++) {
        total_distance += abs(left[i] - right[i]);
    }

    // Výstup výsledku
    printf("Celková vzdálenost mezi seznamy: %d\n", total_distance);

    return 0;
}

