import timeit
from pathlib import Path

from boyer_moore import boyer_moore_search
from kmp import kmp_search
from rabin_karp import rabin_karp_search


def benchmark_algo(search_func, main_string, patter, number):
    timer = timeit.Timer(lambda: search_func(main_string, patter))
    return timer.timeit(number=number)


def run_benchmark_for_main_str(main_str, patterns):
    search_algos = [
        ("boyer moore", boyer_moore_search),
        ("kmp", kmp_search),
        ("rabin karp", rabin_karp_search),
    ]

    for pattern in patterns:
        pattern_name, pattern_str = pattern

        for algo in search_algos:
            search_name, search_fn = algo
            res = benchmark_algo(search_fn, main_str, pattern_str, 100)
            print(f"Run bench for {search_name.capitalize()} for pattern: {pattern_name}: {res}")

        print("\n")
        

def run_benchmark():
    script_dir = Path(__file__).parent
    main_str_1 = (script_dir / "testdata/article_1.txt").read_text(encoding="utf-8")
    print("Run benchmark for article 1")
    run_benchmark_for_main_str(main_str_1, [
        ("existing", "Java"),
        ("non-existent", "private"),
    ])
    print("\n\nRun benchmark for article 2")
    main_str_2 = (script_dir / "testdata/article_2.txt").read_text(encoding="utf-8")
    run_benchmark_for_main_str(main_str_2, [
        ("existing", "розташовується"),  # existing pattern
        ("existing long pattern", "максимальна кількість вподобань 2048"),
        ("non-existent", "конвертація")  # non-existing pattern
    ])
