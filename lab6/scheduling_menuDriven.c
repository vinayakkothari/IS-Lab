#include<stdio.h>

void main()
{
    int n;
    while (1)
    {
        printf("Choose a scheduling algorithm: ");
        printf("\n1. Preemptive Shortest Job First");
        printf("\n2. Round Robin");
        printf("\n3. Non-preemptive Priority Scheduling");
        scanf("%d", &n);

        switch (n)
        {
        case 1:
            presjf();
            break;

        case 2:
            roro();
            break;

        case 3:
            nonpresjf();
            break;
        
        default:
            printf("Enter a valid number");
        }
    }
}

void presjf(){
    int n, p[10], at[10], rem_bt[10], bt[10];
    printf("Enter number of processes: ");
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        p[i] = i;
        printf("Enter burst time and arrival time of process %d", n);
        scanf("%d %d", &at[i], &bt[i]);
        rem_bt[i] = bt[i];
    }

    
}