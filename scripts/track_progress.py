#!/usr/bin/env python3
"""
Learning Progress Tracker

Tracks your learning progress and provides insights on your DSA journey.
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import subprocess


class LearningTracker:
    """Tracks learning progress and provides insights."""
    
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.progress_file = root_dir / "learning_progress.json"
        self.load_progress()
    
    def load_progress(self):
        """Load progress data from file."""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                self.progress_data = json.load(f)
        else:
            self.progress_data = {
                "start_date": datetime.now().isoformat(),
                "problems_completed": [],
                "daily_goals": {},
                "learning_streak": 0,
                "total_time_spent": 0,
                "notes": []
            }
    
    def save_progress(self):
        """Save progress data to file."""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress_data, f, indent=2)
    
    def mark_problem_completed(self, difficulty: str, problem_name: str, 
                              approaches_completed: List[str], time_spent: int):
        """Mark a problem as completed."""
        
        completion_entry = {
            "date": datetime.now().isoformat(),
            "difficulty": difficulty,
            "problem_name": problem_name,
            "approaches_completed": approaches_completed,
            "time_spent_minutes": time_spent
        }
        
        self.progress_data["problems_completed"].append(completion_entry)
        self.progress_data["total_time_spent"] += time_spent
        
        # Update learning streak
        self.update_learning_streak()
        
        self.save_progress()
        print(f"✅ Marked {difficulty}/{problem_name} as completed!")
    
    def update_learning_streak(self):
        """Update the current learning streak."""
        today = datetime.now().date()
        streak = 0
        
        # Check recent completions
        for completion in reversed(self.progress_data["problems_completed"]):
            completion_date = datetime.fromisoformat(completion["date"]).date()
            days_diff = (today - completion_date).days
            
            if days_diff == streak:
                streak += 1
            elif days_diff > streak:
                break
        
        self.progress_data["learning_streak"] = streak
    
    def get_progress_summary(self) -> Dict:
        """Get a summary of learning progress."""
        
        total_problems = len(self.progress_data["problems_completed"])
        total_time = self.progress_data["total_time_spent"]
        streak = self.progress_data["learning_streak"]
        
        # Count by difficulty
        difficulty_counts = {}
        for completion in self.progress_data["problems_completed"]:
            diff = completion["difficulty"]
            difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
        
        # Calculate average time per problem
        avg_time = total_time / total_problems if total_problems > 0 else 0
        
        return {
            "total_problems_completed": total_problems,
            "total_time_spent_hours": total_time / 60,
            "average_time_per_problem": avg_time,
            "current_streak_days": streak,
            "difficulty_breakdown": difficulty_counts,
            "learning_start_date": self.progress_data["start_date"]
        }
    
    def print_progress_report(self):
        """Print a formatted progress report."""
        
        summary = self.get_progress_summary()
        
        print("📚 DSA Learning Progress Report")
        print("=" * 50)
        
        print(f"🎯 Problems Completed: {summary['total_problems_completed']}")
        print(f"⏱️  Total Time Spent: {summary['total_time_spent_hours']:.1f} hours")
        print(f"📈 Average per Problem: {summary['average_time_per_problem']:.1f} minutes")
        print(f"🔥 Current Streak: {summary['current_streak_days']} days")
        
        print(f"\n📊 Difficulty Breakdown:")
        for difficulty, count in summary['difficulty_breakdown'].items():
            print(f"  {difficulty.capitalize()}: {count} problems")
        
        # Recent activity
        print(f"\n📅 Recent Activity:")
        recent_completions = self.progress_data["problems_completed"][-5:]
        for completion in reversed(recent_completions):
            date = datetime.fromisoformat(completion["date"]).strftime("%Y-%m-%d")
            print(f"  {date}: {completion['difficulty']}/{completion['problem_name']} "
                  f"({completion['time_spent_minutes']} min)")
        
        # Learning insights
        self.print_learning_insights(summary)
    
    def print_learning_insights(self, summary: Dict):
        """Print learning insights and recommendations."""
        
        print(f"\n💡 Learning Insights:")
        
        if summary['current_streak_days'] >= 7:
            print("  🔥 Great streak! Keep it up!")
        elif summary['current_streak_days'] >= 3:
            print("  📈 Good momentum! Try to maintain consistency.")
        else:
            print("  🚀 Start a new streak today!")
        
        if summary['average_time_per_problem'] < 30:
            print("  ⚡ You're solving problems quickly! Consider tackling harder ones.")
        elif summary['average_time_per_problem'] > 120:
            print("  🐌 Taking your time is good! Focus on understanding the concepts.")
        else:
            print("  ⚖️ Good pacing! You're balancing speed and understanding.")
        
        # Recommendations
        print(f"\n🎯 Recommendations:")
        
        easy_count = summary['difficulty_breakdown'].get('easy', 0)
        medium_count = summary['difficulty_breakdown'].get('medium', 0)
        hard_count = summary['difficulty_breakdown'].get('hard', 0)
        
        if easy_count > 0 and medium_count == 0:
            print("  📈 Ready to try medium difficulty problems!")
        elif medium_count > 0 and hard_count == 0:
            print("  🚀 Challenge yourself with hard problems!")
        elif hard_count > 0:
            print("  🏆 You're tackling advanced problems! Consider teaching others.")
        
        if summary['total_problems_completed'] < 5:
            print("  🎯 Focus on consistency - aim for 1 problem per day")
        elif summary['total_problems_completed'] < 20:
            print("  📚 Great progress! Consider reviewing previous solutions")
        else:
            print("  🎓 You're building strong DSA skills! Keep practicing!")
    
    def add_note(self, note: str):
        """Add a learning note."""
        note_entry = {
            "date": datetime.now().isoformat(),
            "note": note
        }
        self.progress_data["notes"].append(note_entry)
        self.save_progress()
        print("📝 Note added to your learning journal!")
    
    def set_daily_goal(self, goal: str):
        """Set a daily learning goal."""
        today = datetime.now().strftime("%Y-%m-%d")
        self.progress_data["daily_goals"][today] = goal
        self.save_progress()
        print(f"🎯 Daily goal set: {goal}")


def main():
    """Main function for the learning tracker."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Track your DSA learning progress")
    parser.add_argument("--report", action="store_true", help="Show progress report")
    parser.add_argument("--complete", type=str, help="Mark problem as completed (format: difficulty/problem_name)")
    parser.add_argument("--approaches", type=str, nargs="+", help="Approaches completed")
    parser.add_argument("--time", type=int, help="Time spent in minutes")
    parser.add_argument("--note", type=str, help="Add a learning note")
    parser.add_argument("--goal", type=str, help="Set daily goal")
    
    args = parser.parse_args()
    
    # Get the root directory
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    tracker = LearningTracker(root_dir)
    
    if args.report:
        tracker.print_progress_report()
    
    elif args.complete:
        if not args.approaches or not args.time:
            print("❌ Usage: --complete difficulty/problem_name --approaches approach1 approach2 --time minutes")
            return
        
        difficulty, problem_name = args.complete.split('/')
        tracker.mark_problem_completed(difficulty, problem_name, args.approaches, args.time)
    
    elif args.note:
        tracker.add_note(args.note)
    
    elif args.goal:
        tracker.set_daily_goal(args.goal)
    
    else:
        # Default: show progress report
        tracker.print_progress_report()


if __name__ == "__main__":
    main()
