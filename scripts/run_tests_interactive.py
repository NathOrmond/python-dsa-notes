#!/usr/bin/env python3
"""
Interactive Test Runner for DSA Problems

This script provides an interactive command-line interface to select and run tests.
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Dict


class TestDiscovery:
    """Discovers available tests in the project."""
    
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.test_dir = root_dir / "tests" / "problems"
    
    def check_if_tests_pass(self, difficulty: str, problem_name: str) -> bool:
        """Check if tests for a problem pass (i.e., has implementation)."""
        test_file = self.test_dir / difficulty / f"test_{problem_name}.py"
        
        if not test_file.exists():
            return False
        
        try:
            # Run pytest on the specific test file with very minimal output
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(test_file), "-q", "--tb=no"],
                capture_output=True,
                text=True,
                cwd=self.root_dir,
                timeout=30  # Prevent hanging on tests that might be stuck
            )
            
            # Check if any tests passed
            return result.returncode == 0 and "PASSED" in result.stdout
        
        except (subprocess.TimeoutExpired, Exception):
            return False
    
    def list_test_files(self, only_passing: bool = True) -> Dict[str, List[str]]:
        """Return a dictionary mapping difficulty to list of test files.
        
        Args:
            only_passing: If True, only include tests that pass (have implementations)
        """
        result = {}
        
        for difficulty in ["easy", "medium", "hard"]:
            difficulty_dir = self.test_dir / difficulty
            if not difficulty_dir.exists():
                continue
            
            test_files = []
            for test_file in sorted(difficulty_dir.glob("test_*.py")):
                # Extract problem name from filename
                name = test_file.stem.replace("test_", "")
                
                # If only_passing is True, check if tests pass
                if only_passing:
                    print(f"  Checking {difficulty}/{name}...", end='\r')
                    if self.check_if_tests_pass(difficulty, name):
                        test_files.append(name)
                else:
                    test_files.append(name)
            
            if test_files:
                result[difficulty] = test_files
        
        if only_passing:
            print()  # Clear the progress line
        
        return result
    
    def get_test_classes_and_methods(self, difficulty: str, problem_name: str) -> List[str]:
        """Get all test classes and methods for a specific problem."""
        test_file = self.test_dir / difficulty / f"test_{problem_name}.py"
        
        if not test_file.exists():
            return []
        
        # Use pytest to collect test info
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(test_file), "--collect-only", "-q"],
                capture_output=True,
                text=True,
                cwd=self.root_dir
            )
            
            # Parse pytest output to extract test identifiers
            tests = []
            for line in result.stdout.split('\n'):
                line = line.strip()
                if line.startswith('<') and '::' in line:
                    # Parse line like: <Function test_basic_examples[param1-param2]>
                    # or: <Function test_basic_examples>
                    if '::' in line:
                        # Extract just the identifier part
                        parts = line.split(' ')
                        if len(parts) > 0 and '::' in parts[0]:
                            test_path = parts[0].split('::')
                            if len(test_path) > 1:
                                # Format: module::class::method
                                clean_path = '::'.join(test_path)
                                if clean_path.startswith('<'):
                                    clean_path = clean_path[1:].split(' ')[0]
                                tests.append(clean_path)
            
            return sorted(set(tests))
        
        except Exception as e:
            print(f"Error discovering tests: {e}")
            return []


class InteractiveMenu:
    """Simple interactive terminal menu."""
    
    def __init__(self, prompt: str, options: List[str]):
        self.prompt = prompt
        self.options = options
        self.selected = []
    
    def display(self):
        """Display the menu."""
        print(f"\n{self.prompt}")
        print("=" * (len(self.prompt) + 10))
        
        for i, option in enumerate(self.options, 1):
            marker = "[✓]" if i in self.selected else "[ ]"
            print(f"  {i}. {marker} {option}")
        
        print(f"\n  0. Done selecting (run {len(self.selected)} test(s))")
        print("  q. Quit without running")
    
    def get_selection(self) -> List[str]:
        """Get user selection."""
        self.display()
        
        choices = []
        while True:
            try:
                user_input = input("\nEnter your choice(s) separated by commas (or 0/q): ").strip()
                
                if user_input.lower() == 'q':
                    return []
                
                if user_input == '0':
                    if not self.selected:
                        print("Please select at least one option first!")
                        continue
                    break
                
                # Parse comma-separated choices
                for choice_str in user_input.split(','):
                    choice_str = choice_str.strip()
                    if choice_str.isdigit():
                        choice = int(choice_str)
                        if 1 <= choice <= len(self.options):
                            if choice in self.selected:
                                self.selected.remove(choice)
                            else:
                                self.selected.append(choice)
                            choices.append(choice)
                        else:
                            print(f"Invalid choice: {choice}. Please enter a number between 1 and {len(self.options)}")
                    else:
                        print(f"Invalid choice: {choice_str}. Please enter numbers only.")
                
                self.display()
                
            except (ValueError, KeyboardInterrupt):
                print("\nInvalid input or interrupted. Exiting.")
                return []
        
        # Return selected options
        selected_items = [self.options[i - 1] for i in sorted(self.selected)]
        return selected_items


def run_pytest(test_paths: List[str], verbose: bool = True):
    """Run pytest on selected test paths."""
    cmd = [sys.executable, "-m", "pytest"]
    
    if verbose:
        cmd.append("-v")
    
    cmd.extend(test_paths)
    
    print(f"\n{'='*60}")
    print("Running tests...")
    print(f"{'='*60}\n")
    
    # Run pytest
    result = subprocess.run(cmd, cwd=Path(__file__).parent.parent)
    
    return result.returncode == 0


def main():
    """Main function."""
    root_dir = Path(__file__).parent.parent
    discovery = TestDiscovery(root_dir)
    
    # Ask if user wants to see only passing tests or all tests
    print("\n" + "="*60)
    print("Test Runner Options:")
    print("="*60)
    print("1. Show only tests with implementations (recommended)")
    print("2. Show all tests (including not yet implemented)")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    only_passing = choice != "2"
    
    if only_passing:
        print("\n🔍 Scanning for implemented tests...\n")
    
    # Step 1: Select difficulty level
    difficulties = ["easy", "medium", "hard", "all"]
    menu = InteractiveMenu("Select difficulty level:", difficulties)
    difficulty_choice = menu.get_selection()
    
    if not difficulty_choice:
        print("Goodbye!")
        return
    
    selected_difficulty = difficulty_choice[0]
    
    # Step 2: Select problem(s)
    if selected_difficulty == "all":
        test_files_by_difficulty = discovery.list_test_files(only_passing=only_passing)
        all_problems = []
        for diff, problems in test_files_by_difficulty.items():
            for problem in problems:
                all_problems.append(f"{diff}/{problem}")
        
        if not all_problems:
            if only_passing:
                print("No implemented tests found! Try option 2 to see all tests.")
            else:
                print("No test files found!")
            return
        
        menu = InteractiveMenu("Select problem(s) to test:", all_problems)
        selected_problems = menu.get_selection()
        
    else:
        test_files = discovery.list_test_files(only_passing=only_passing).get(selected_difficulty, [])
        
        if not test_files:
            if only_passing:
                print(f"No implemented tests found for {selected_difficulty} difficulty!")
                print("Try selecting option 2 at the beginning to see all tests.")
            else:
                print(f"No test files found for {selected_difficulty} difficulty!")
            return
        
        menu = InteractiveMenu("Select problem(s) to test:", test_files)
        selected_problems = menu.get_selection()
    
    if not selected_problems:
        print("No problems selected. Exiting.")
        return
    
    # Step 3: Ask if they want to select specific test methods
    select_methods = input("\nDo you want to select specific test methods? (y/n): ").strip().lower()
    test_paths = []
    
    if select_methods == 'y':
        # For each selected problem, let user select test methods
        for problem in selected_problems:
            if '/' in problem:
                diff, prob = problem.split('/')
            else:
                diff = selected_difficulty
                prob = problem
            
            methods = discovery.get_test_classes_and_methods(diff, prob)
            
            if methods:
                menu = InteractiveMenu(f"Select test method(s) for {prob}:", methods)
                selected_methods = menu.get_selection()
                
                if selected_methods:
                    for method in selected_methods:
                        test_path = root_dir / "tests" / "problems" / diff / f"test_{prob}.py::{method}"
                        test_paths.append(str(test_path))
                else:
                    # Run all tests for this problem
                    test_path = root_dir / "tests" / "problems" / diff / f"test_{prob}.py"
                    test_paths.append(str(test_path))
            else:
                # No methods found, run the whole test file
                test_path = root_dir / "tests" / "problems" / diff / f"test_{prob}.py"
                test_paths.append(str(test_path))
    else:
        # Build test paths from selected problems
        for problem in selected_problems:
            if '/' in problem:
                diff, prob = problem.split('/')
            else:
                diff = selected_difficulty
                prob = problem
            
            test_path = root_dir / "tests" / "problems" / diff / f"test_{prob}.py"
            test_paths.append(str(test_path))
    
    # Step 4: Run the tests
    if test_paths:
        print(f"\nSelected {len(test_paths)} test(s) to run:")
        for path in test_paths:
            print(f"  - {path}")
        
        run_pytest(test_paths)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye!")
        sys.exit(0)

