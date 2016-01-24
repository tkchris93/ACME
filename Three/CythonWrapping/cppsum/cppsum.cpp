double cppsum(double* a) {
    double total = 0.0;
    for (int i = 0; i < 100000000; i++){
        total += a[i];
    }
    return total;
}
