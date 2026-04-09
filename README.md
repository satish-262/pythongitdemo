# Git Practice Project — Task Manager

A simple Flask todo app built specifically to **learn Git and GitHub**.

## Tech Stack
- **Backend**: Python + Flask
- **Frontend**: HTML, CSS, JavaScript
- **Data**: JSON file (local storage)

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000 in your browser.

---

## 🎓 Git Learning Exercises

Work through these in order. Each one teaches a real Git concept.

### Exercise 1 — Initialize & First Commit
```bash
git init
git add .
git commit -m "Initial commit: add task manager app"
```

### Exercise 2 — Explore History
```bash
git log           # see all commits
git log --oneline # compact view
git status        # what's changed?
```

### Exercise 3 — Make a Change & Commit It
Edit `static/style.css` — change the background color or font.
```bash
git diff                    # see what changed
git add static/style.css
git commit -m "style: change background color"
```

### Exercise 4 — Create a Branch
```bash
git checkout -b feature/dark-mode
# Make some CSS changes for dark mode...
git add .
git commit -m "feat: add dark mode styles"
git checkout main            # switch back
```

### Exercise 5 — Merge the Branch
```bash
git merge feature/dark-mode
git branch -d feature/dark-mode   # clean up
```

### Exercise 6 — Push to GitHub
```bash
# Create a new repo on github.com first, then:
git remote add origin https://github.com/YOUR_USERNAME/git-practice.git
git branch -M main
git push -u origin main
```

### Exercise 7 — Pull Requests
1. On GitHub, create a new branch via the UI
2. Edit `README.md` directly on GitHub
3. Open a Pull Request
4. Merge it
5. Run `git pull` locally to sync

### Exercise 8 — Undo Mistakes
```bash
git restore style.css          # undo unsaved file changes
git reset HEAD~1               # undo last commit (keep changes)
git revert <commit-hash>       # safely undo a pushed commit
```

---

## File Structure
```
git-practice/
├── app.py              ← Flask backend (Python)
├── requirements.txt    ← Dependencies
├── .gitignore          ← Files Git should ignore
├── README.md           ← This file
├── templates/
│   └── index.html      ← HTML template
└── static/
    ├── style.css       ← Styling
    └── main.js         ← Frontend JavaScript
```
