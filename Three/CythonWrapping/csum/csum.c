double csum(double* a){
    double total = 0.0;
    int i;
    for (i = 0; i < 100000000; i++){
        total += a[i];
    }
    return total;
}
