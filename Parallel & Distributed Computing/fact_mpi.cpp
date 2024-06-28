#include <iostream>
#include <mpi.h>

long fact(int n) {
    if (n <= 1)
        return 1;
    else
        return n * fact(n - 1);
}

int main() {
    int n, rank, size;
    long local_ans, global_ans;

    MPI_Init(NULL, NULL);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        std::cout << "Enter the number: ";
        std::cin >> n;
    }

    // Broadcast the value of n to all processes
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    // Each process computes its local factorial
    local_ans = fact(n / size); // Divide the work equally among processes

    // Gather all local results to rank 0
    MPI_Reduce(&local_ans, &global_ans, 1, MPI_LONG, MPI_PROD, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        std::cout << "Computed answer: " << global_ans << std::endl;
    }
    else if (rank == 1) {
        std::cout << "Received answer: " << global_ans << std::endl;
    }

    MPI_Finalize();
    return 0;
}
