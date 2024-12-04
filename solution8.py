
def format_table(benchmarks, algos, results):
    all_values = [f"{bench}" for bench in benchmarks]
    all_values.append('Benchmark')
    all_values.extend([f"{alg}" for alg in algos])
    all_values.extend([str(value) for row in results for value in row])
    col_size = max(map(len, all_values))
    separator = "-" * ((col_size + 2) * (len(algos) + 1) + len(algos) + 2)
    header = f"| " + f"{'Benchmark':<{col_size}}" + f" | " + " | ".join(f"{alg:<{col_size}}" for alg in algos) + " |"
    #f"| {" ".join(f"{name:<{col_size}}" for name in ["Benchmark"] + algos)} |"
    print(header)
    print(separator)

    for benchmark, result in zip(benchmarks, results):
        string = f"| {benchmark:<{col_size}} | " + " | ".join(f"{value:<{col_size}}" for value in result) + " |"
        print(string)

if __name__ == '__main__':
    print (format_table(["best", "worst"],["quick sort", "merge sort", "bubble sort"],[[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(format_table(["3", "4"], ["2", "5", "7"], [[122, 10 ** 11, 2.0], [3.3, 2.9, 3.9]]))