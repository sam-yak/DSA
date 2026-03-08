# Git Setup & Daily Workflow Guide

## Daily Workflow (The Only Commands You Need)

After each coaching session with Claude:

```bash
cd ~/Desktop/DSA
git add -A
git commit -m "Day X: [topic] - completed Y/Z problems"
git push origin main
```

## Example Commit Messages

```bash
git commit -m "Day 1: Arrays & Hash Maps - 6/6 problems solved"
git commit -m "Day 6: Backtracking - 5/5 problems, first Hard solved!"
git commit -m "Day 18: Weakness day - revisited 8 failed problems"
```

## Quick Reference

| What You Want              | Command                          |
|----------------------------|----------------------------------|
| See what changed           | `git status`                     |
| Stage everything           | `git add -A`                     |
| Commit                     | `git commit -m "message"`        |
| Push                       | `git push origin main`           |
| Pull latest                | `git pull origin main`           |
| See commit history         | `git log --oneline`              |
| Undo last commit (keep changes) | `git reset --soft HEAD~1`  |

## Troubleshooting

**"Updates were rejected"** — Pull first:
```bash
git pull origin main --rebase
git push origin main
```

**"Branch 'main' not found"** — Try `master`:
```bash
git push origin master
```
