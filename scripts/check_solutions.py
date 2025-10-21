#!/usr/bin/env python3
"""
Solution Status Checker

This script checks the implementation status of all DSA problems
and shows which solutions are implemented, which pass tests, and which need work.
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class SolutionChecker:
    """Checks the status of DSA problem solutions."""
    
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.src_dir = self.root_dir / "src" / "problems"
        self.results = {}
    
    def check_all_problems(self) -> Dict[str, Dict[str, str]]:
        """Check all problems and return status summary."""
        results = {}
        
        for difficulty in ["easy", "medium", "hard"]:
            difficulty_dir = self.src_dir / difficulty
            if not difficulty_dir.exists():
                continue
                
            for problem_dir in difficulty_dir.iterdir():
                if problem_dir.is_dir() and not problem_dir.name.startswith('__'):
                    problem_name = problem_dir.name
                    results[f"{difficulty}/{problem_name}"] = self.check_problem(problem_dir)
        
        return results
    
    def check_problem(self, problem_dir: Path) -> Dict[str, str]:
        """Check a single problem's implementation status."""
        problem_name = problem_dir.name
        results = {
            "main": "⏳ Not Implemented",
            "brute_force": "⏳ Not Implemented", 
            "hash_map": "⏳ Not Implemented",
            "tests": "❌ Failed"
        }
        
        # Check main solution file
        main_file = problem_dir / f"{problem_name}.py"
        if main_file.exists():
            main_status = self.check_function_implementation(main_file, problem_name)
            if main_status == "implemented":
                results["main"] = "✅ Implemented"
            elif main_status == "has_bugs":
                results["main"] = "❌ Has Bugs"
            elif main_status == "not_implemented":
                results["main"] = "⏳ Not Implemented"
        
        # Check brute force solution
        brute_force_status = self.check_function_implementation(main_file, f"{problem_name}_brute_force")
        if brute_force_status == "implemented":
            results["brute_force"] = "✅ Implemented"
        elif brute_force_status == "has_bugs":
            results["brute_force"] = "❌ Has Bugs"
        elif brute_force_status == "not_implemented":
            results["brute_force"] = "⏳ Not Implemented"
        
        # Check optimized solution (could be hash_map, stack, etc.)
        optimized_status = self.check_function_implementation(main_file, f"{problem_name}_stack")
        if optimized_status in ["not_implemented", "not_found"]:
            # Try hash_map as fallback
            optimized_status = self.check_function_implementation(main_file, f"{problem_name}_hash_map")
        
        if optimized_status == "implemented":
            results["hash_map"] = "✅ Implemented"
        elif optimized_status == "has_bugs":
            results["hash_map"] = "❌ Has Bugs"
        elif optimized_status in ["not_implemented", "not_found"]:
            results["hash_map"] = "⏳ Not Implemented"
        
        # Check if tests pass
        test_status = self.check_test_status(problem_name)
        if test_status == "all_pass":
            results["tests"] = "✅ All Pass"
        elif test_status == "some_pass":
            results["tests"] = "⚠️ Some Pass"
        elif test_status == "all_fail":
            results["tests"] = "❌ All Fail"
        
        return results
    
    def check_function_implementation(self, file_path: Path, function_name: str) -> str:
        """Check if a function is implemented or just a stub."""
        if not file_path.exists():
            return "not_found"
        
        try:
            # Read the file content
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Look for the function definition
            lines = content.split('\n')
            in_function = False
            function_lines = []
            
            for i, line in enumerate(lines):
                if f"def {function_name}(" in line:
                    in_function = True
                    function_lines.append(line)
                    continue
                
                if in_function:
                    # Check if we've reached the next function or end of file
                    if line.strip() and not line.startswith(' ') and not line.startswith('\t') and not line.startswith('#'):
                        if line.strip().startswith('def ') or line.strip().startswith('class '):
                            break
                    
                    function_lines.append(line)
                    
                    # Check if function body contains actual implementation
                    if line.strip() == "pass" or line.strip().startswith("# TODO"):
                        continue
                    elif line.strip() and not line.startswith(' ') and not line.startswith('\t') and not line.startswith('#'):
                        if not line.strip().startswith('def ') and not line.strip().startswith('class '):
                            break
            
            # Analyze the function body
            function_body = '\n'.join(function_lines)
            
            # Check if function was found
            if not function_lines:
                return "not_found"
            
            if "pass" in function_body and "TODO" in function_body:
                return "not_implemented"
            elif "pass" in function_body:
                return "not_implemented"
            elif "raise NotImplementedError" in function_body:
                return "not_implemented"
            elif "return None" in function_body and len(function_body.strip().split('\n')) < 5:
                return "not_implemented"
            else:
                # Try to run the function to see if it has bugs
                try:
                    spec = importlib.util.spec_from_file_location("module", file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    func = getattr(module, function_name, None)
                    if func:
                        # Dynamically determine test parameters based on function signature
                        test_result = self._test_function_dynamically(func, function_name)
                        return test_result
                except Exception:
                    return "has_bugs"
                
                return "implemented"
        
        except Exception:
            return "error"
    
    def _test_function_dynamically(self, func, function_name: str) -> str:
        """Dynamically test a function based on its signature and return type."""
        import inspect
        
        try:
            # Get function signature
            sig = inspect.signature(func)
            params = list(sig.parameters.keys())
            
            # Get return type annotation
            return_annotation = sig.return_annotation
            
            # Generate test parameters based on parameter types
            test_args = self._generate_test_args(params, sig)
            
            if test_args is None:
                return "has_bugs"
            
            # Execute the function
            result = func(*test_args)
            
            # Check result based on return type annotation
            if return_annotation == inspect.Signature.empty:
                # No type annotation - check if result is None (likely not implemented)
                if result is None:
                    return "not_implemented"
                else:
                    return "implemented"
            elif return_annotation == bool:
                if result is None:
                    return "not_implemented"
                elif isinstance(result, bool):
                    return "implemented"
                else:
                    return "has_bugs"
            elif hasattr(return_annotation, '__origin__') and return_annotation.__origin__ is list:
                if result is None:
                    return "not_implemented"
                elif isinstance(result, list):
                    return "implemented"
                else:
                    return "has_bugs"
            else:
                # Generic check
                if result is None:
                    return "not_implemented"
                else:
                    return "implemented"
                    
        except Exception:
            return "has_bugs"
    
    def _generate_test_args(self, params: List[str], sig) -> Optional[List]:
        """Generate appropriate test arguments based on parameter names and types."""
        test_args = []
        
        for param_name in params:
            param = sig.parameters[param_name]
            param_type = param.annotation
            
            # Generate test data based on parameter name and type
            if param_name in ['nums', 'numbers', 'array', 'arr']:
                test_args.append([2, 7, 11, 15])  # Standard test array
            elif param_name in ['target', 'sum', 'goal']:
                test_args.append(9)  # Standard test target
            elif param_name in ['s', 'string', 'str', 'text']:
                test_args.append("()")  # Standard test string
            elif param_name in ['n', 'size', 'length']:
                test_args.append(5)  # Standard test size
            elif param_name in ['k', 'count']:
                test_args.append(2)  # Standard test count
            elif param_type == int:
                test_args.append(1)  # Default int
            elif param_type == str:
                test_args.append("test")  # Default string
            elif param_type == bool:
                test_args.append(True)  # Default bool
            elif hasattr(param_type, '__origin__') and param_type.__origin__ is list:
                test_args.append([])  # Default empty list
            else:
                # Unknown parameter type
                return None
        
        return test_args
    
    def check_test_status(self, problem_name: str) -> str:
        """Check if tests pass for a problem."""
        test_file = self.root_dir / "tests" / "problems" / "easy" / f"test_{problem_name}.py"
        
        if not test_file.exists():
            return "no_tests"
        
        try:
            # Run pytest on the specific test file
            result = subprocess.run([
                sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=no"
            ], capture_output=True, text=True, cwd=self.root_dir)
            
            output = result.stdout + result.stderr
            
            if "FAILED" in output:
                if "PASSED" in output:
                    return "some_pass"
                else:
                    return "all_fail"
            elif "PASSED" in output:
                return "all_pass"
            else:
                return "no_tests"
        
        except Exception:
            return "error"
    
    def print_status_report(self, results: Dict[str, Dict[str, str]], show_all: bool = False):
        """Print a formatted status report."""
        print("🔍 DSA Solution Status Report")
        print("=" * 50)
        
        total_problems = len(results)
        implemented_solutions = 0
        total_solutions = 0
        
        for problem_path, status in results.items():
            difficulty, problem_name = problem_path.split('/')
            
            print(f"\n📁 {difficulty.upper()}: {problem_name}")
            print("-" * 30)
            
            for solution_type, status_icon in status.items():
                if solution_type == "main":
                    print(f"  Main Solution:     {status_icon}")
                elif solution_type == "brute_force":
                    print(f"  Brute Force:      {status_icon}")
                elif solution_type == "hash_map":
                    print(f"  Hash Map:         {status_icon}")
                elif solution_type == "tests":
                    print(f"  Tests:            {status_icon}")
                
                # Count implementations
                if solution_type in ["main", "brute_force", "hash_map"]:
                    total_solutions += 1
                    if "✅" in status_icon:
                        implemented_solutions += 1
            
            if not show_all and all("⏳" in status_icon for status_icon in status.values()):
                print("  (All solutions not implemented - skipping details)")
        
        print(f"\n📊 Summary:")
        print(f"  Total Problems: {total_problems}")
        print(f"  Implemented Solutions: {implemented_solutions}/{total_solutions}")
        print(f"  Completion Rate: {(implemented_solutions/total_solutions*100):.1f}%" if total_solutions > 0 else "N/A")
        
        print(f"\n💡 Next Steps:")
        if implemented_solutions == 0:
            print("  - Start implementing solutions!")
            print("  - Begin with brute force approaches")
            print("  - Run tests frequently to check your progress")
        elif implemented_solutions < total_solutions:
            print("  - Continue implementing remaining solutions")
            print("  - Focus on optimizing your brute force solutions")
        else:
            print("  - Great job! All solutions implemented!")
            print("  - Consider adding more problems or optimizing further")


def main():
    """Main function to run the solution checker."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Check DSA solution implementation status")
    parser.add_argument("--all", action="store_true", help="Show all problems, even unimplemented ones")
    parser.add_argument("--problem", type=str, help="Check specific problem (e.g., 'easy/two_sum')")
    
    args = parser.parse_args()
    
    # Get the root directory (parent of scripts directory)
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    checker = SolutionChecker(root_dir)
    
    if args.problem:
        # Check specific problem
        difficulty, problem_name = args.problem.split('/')
        problem_dir = root_dir / "src" / "problems" / difficulty / problem_name
        if problem_dir.exists():
            results = {args.problem: checker.check_problem(problem_dir)}
        else:
            print(f"❌ Problem not found: {args.problem}")
            return
    else:
        # Check all problems
        results = checker.check_all_problems()
    
    checker.print_status_report(results, show_all=args.all)


if __name__ == "__main__":
    main()
