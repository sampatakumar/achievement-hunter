# Achievement Hunter 🏆

A simple automation script to help you unlock various GitHub profile achievements (badges) through automated actions.

## 🚀 About the Project

This project provides a Python script that uses the GitHub CLI (`gh`) and Git to perform specific actions that trigger GitHub's achievement system. It's designed for educational purposes and for those who want to showcase their technical activity on their profile.

### Triggered Achievements:
- **Heart On Your Sleeve**: React to an issue or pull request with a ❤️.
- **YOLO**: Merge a pull request without any code review.
- **Quickdraw**: Create and close an issue within 5 minutes.
- **Pair Extraordinaire**: Co-author commits on a merged pull request.
- **Pull Shark**: Open and merge multiple pull requests to reach tier milestones.

---

## 🛠️ How to Run

### Prerequisites
1. **GitHub CLI (`gh`)**: Ensure you have it [installed](https://cli.github.com/).
2. **Git**: Ensure Git is installed and configured.
3. **Python 3**: The script is written in Python.

### Setup & Execution

1. **Authenticate with GitHub**:
   ```bash
   gh auth login
   ```
   *Follow the prompts to log in via your web browser.*

2. **Clone this repository** (if you haven't already):
   ```bash
   gh repo clone sampatakumar/achievement-hunter
   cd achievement-hunter
   ```

3. **Run the automation script**:
   ```bash
   python unlock_achievements.py
   ```

---

## 📖 How it Works

The script `unlock_achievements.py` automates the following workflow:
- **Auth Check**: Verifies that you are logged into the GitHub CLI.
- **Issue Creation**: Creates an issue and immediately applies a 'heart' reaction.
- **Branching & PRs**: Creates featured branches, adds minimal changes, creates Pull Requests, and merges them using the CLI.
- **Co-authoring**: Adds `Co-authored-by: Octocat <octocat@github.com>` to a commit message to trigger the Pair Extraordinaire badge.

---

## ⚠️ Notes
- **Processing Time**: GitHub achievements are not instant. It may take anywhere from 10 minutes to 24 hours for the badges to appear on your profile.
- **Profile Display**: Ensure that "Show achievements on your profile" is enabled in your GitHub profile settings.

---

## 🤝 Connect
- GitHub: [@sampatakumar](https://github.com/sampatakumar)
- Portfolio: [sampatakumar.github.io](https://sampatakumar.github.io/)