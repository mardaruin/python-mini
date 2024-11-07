
def format_table(benchmarks, algos, results):
    col_size = max(max(map(len, [f"{bench}" for bench in benchmarks])), max(map(len, [f"{alg}" for alg in algos])), len("Benchmark"))
    separator = "-" * ((col_size + 2) * (len(algos) + 1) + len(algos) + 2)
    header = f"| " + f"{'Benchmark':<{col_size}}" + f" | " + " | ".join(f"{alg:<{col_size}}" for alg in algos) + " |"
    #f"| {" ".join(f"{name:<{col_size}}" for name in ["Benchmark"] + algos)} |"
    print(header)
    print(separator)

    for benchmark, result in zip(benchmarks, results):
        string = f"| {benchmark:<{col_size}} | " + " | ".join(f"{value:<{col_size}}" for value in result) + " |"
        print(string)

if __name__ == '__main__':
    print (format_table(["best case", "worst case"],["quick sort", "merge sort", "bubble sort"],[[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(format_table(["3", "4"], ["2", "5", "7"], [["6", "15", "21"], ["8", "20", "28"]]))