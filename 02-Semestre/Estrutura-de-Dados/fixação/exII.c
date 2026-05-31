
int main(){
    int x = 1;
    int *p = &x;
    *p = x;
    int a = (*p);
    int *k = &a;
    x = a;
    p = k;
    a = x;
    return 0;
}
