#!/usr/bin/env python3
"""
Performance Benchmarking Script

Measures and compares the performance of different solution approaches.
"""

import time
import sys
import importlib.util
from pathlib import Path
from typing import Dict, List, Callable, Any
import statistics


class PerformanceBenchmark:
    """Benchmarks solution performance."""
    
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.results = {}
    
    def benchmark_problem(self, difficulty: str, problem_name: str, 
                        test_cases: List[tuple], iterations: int = 1000) -> Dict[str, Dict]:
        """Benchmark a specific problem."""
        
        problem_dir = self.root_dir / "src" / "problems" / difficulty / problem_name
        main_file = problem_dir / f"{problem_name}.py"
        
        if not main_file.exists():
            print(f"❌ Problem file not found: {main_file}")
            return {}
        
        # Import the module
        try:
            spec = importlib.util.spec_from_file_location("module", main_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"❌ Failed to import {problem_name}: {e}")
            return {}
        
        results = {}
        
        # Benchmark each solution approach
        approaches = [
            ("brute_force", f"{problem_name}_brute_force"),
            ("optimized", f"{problem_name}_optimized"),
            ("main", problem_name)
        ]
        
        for approach_name, function_name in approaches:
            func = getattr(module, function_name, None)
            if func is None:
                continue
            
            approach_results = []
            
            for test_input, expected in test_cases:
                times = []
                
                # Warm up
                for _ in range(10):
                    try:
                        func(*test_input)
                    except:
                        break
                
                # Benchmark
                for _ in range(iterations):
                    start_time = time.perf_counter()
                    try:
                        result = func(*test_input)
                        end_time = time.perf_counter()
                        times.append(end_time - start_time)
                    except Exception:
                        # Function not implemented or has bugs
                        break
                
                if times:
                    approach_results.append({
                        "test_case": test_input,
                        "expected": expected,
                        "mean_time": statistics.mean(times),
                        "median_time": statistics.median(times),
                        "min_time": min(times),
                        "max_time": max(times),
                        "std_dev": statistics.stdev(times) if len(times) > 1 else 0
                    })
            
            if approach_results:
                results[approach_name] = {
                    "function_name": function_name,
                    "results": approach_results,
                    "total_tests": len(approach_results),
                    "successful_tests": len([r for r in approach_results if r["mean_time"] > 0])
                }
        
        return results
    
    def print_benchmark_results(self, problem_name: str, results: Dict[str, Dict]):
        """Print formatted benchmark results."""
        
        print(f"🚀 Performance Benchmark: {problem_name}")
        print("=" * 60)
        
        if not results:
            print("❌ No results to display")
            return
        
        # Compare approaches
        approaches = list(results.keys())
        if len(approaches) < 2:
            print("⚠️ Need at least 2 approaches to compare")
            return
        
        print(f"\n📊 Performance Comparison:")
        print("-" * 40)
        
        for approach_name, data in results.items():
            if not data["results"]:
                continue
                
            avg_time = statistics.mean([r["mean_time"] for r in data["results"]])
            print(f"{approach_name:15}: {avg_time*1000000:8.2f} μs (avg)")
        
        # Find the fastest approach
        fastest_approach = min(results.keys(), 
                            key=lambda x: statistics.mean([r["mean_time"] for r in results[x]["results"]]) 
                            if results[x]["results"] else float('inf'))
        
        print(f"\n🏆 Fastest Approach: {fastest_approach}")
        
        # Calculate speedup
        if len(approaches) >= 2:
            slowest_time = max(statistics.mean([r["mean_time"] for r in results[x]["results"]]) 
                             for x in results.keys() if results[x]["results"])
            fastest_time = min(statistics.mean([r["mean_time"] for r in results[x]["results"]]) 
                             for x in results.keys() if results[x]["results"])
            
            if fastest_time > 0:
                speedup = slowest_time / fastest_time
                print(f"⚡ Speedup: {speedup:.1f}x faster")
        
        # Detailed results
        print(f"\n📈 Detailed Results:")
        print("-" * 40)
        
        for approach_name, data in results.items():
            if not data["results"]:
                continue
                
            print(f"\n{approach_name.upper()} ({data['function_name']}):")
            for i, result in enumerate(data["results"][:3]):  # Show first 3 test cases
                print(f"  Test {i+1}: {result['mean_time']*1000000:6.2f} μs "
                      f"(±{result['std_dev']*1000000:4.2f} μs)")


def create_test_cases_for_problem(problem_name: str) -> List[tuple]:
    """Create appropriate test cases for benchmarking."""
    
    if problem_name == "two_sum":
        return [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
            ([1, 2, 3, 4, 5], 8),
            ([0, 4, 3, 0], 0),
            # Larger test cases for performance
            (list(range(100)) + [199, 200], 399),
            (list(range(1000)) + [1999, 2000], 3999),
        ]
    
    # Add more problems as needed
    return []


def main():
    """Main function to run benchmarks."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Benchmark DSA solution performance")
    parser.add_argument("--problem", type=str, help="Benchmark specific problem (e.g., 'easy/two_sum')")
    parser.add_argument("--iterations", type=int, default=1000, help="Number of iterations per test")
    parser.add_argument("--all", action="store_true", help="Benchmark all implemented problems")
    
    args = parser.parse_args()
    
    # Get the root directory
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    benchmark = PerformanceBenchmark(root_dir)
    
    if args.problem:
        # Benchmark specific problem
        difficulty, problem_name = args.problem.split('/')
        test_cases = create_test_cases_for_problem(problem_name)
        
        if not test_cases:
            print(f"❌ No test cases defined for {problem_name}")
            return
        
        results = benchmark.benchmark_problem(difficulty, problem_name, test_cases, args.iterations)
        benchmark.print_benchmark_results(problem_name, results)
    
    elif args.all:
        # Benchmark all problems
        print("🔍 Finding all problems...")
        
        for difficulty in ["easy", "medium", "hard"]:
            difficulty_dir = root_dir / "src" / "problems" / difficulty
            if not difficulty_dir.exists():
                continue
            
            for problem_dir in difficulty_dir.iterdir():
                if problem_dir.is_dir() and not problem_dir.name.startswith('__'):
                    problem_name = problem_dir.name
                    test_cases = create_test_cases_for_problem(problem_name)
                    
                    if test_cases:
                        print(f"\n{'='*60}")
                        results = benchmark.benchmark_problem(difficulty, problem_name, test_cases, args.iterations)
                        benchmark.print_benchmark_results(problem_name, results)
    
    else:
        print("❌ Please specify --problem or --all")
        print("Example: python scripts/benchmark.py --problem easy/two_sum")


if __name__ == "__main__":
    main()
