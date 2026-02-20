import subprocess
import time
import os
import sys

REPO_NAME = "achievement-hunter"

def run_command(command, cwd=None):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
    return result.stdout.strip(), result.returncode

def main():
    # 1. Check gh auth
    status, code = run_command("gh auth status")
    if "Logged in to github.com" not in status:
        print("Error: You must be logged in to GitHub CLI. Run 'gh auth login' first.")
        return

    # 2. Get username
    username, code = run_command("gh api user --template '{{.login}}'")
    if not username:
        print("Error: Could not retrieve GitHub username.")
        return
    print(f"Logged in as: {username}")

    # 3. Create or clone repository
    base_dir = os.path.dirname(os.path.abspath(__file__))
    repo_path = os.path.join(base_dir, REPO_NAME)

    print(f"Checking for repository {REPO_NAME}...")
    # Check if repo exists on GitHub
    _, exists_code = run_command(f"gh repo view {REPO_NAME}")
    
    if exists_code != 0:
        print("Creating repository on GitHub...")
        run_command(f"gh repo create {REPO_NAME} --public --init")
        time.sleep(5) # Wait for GitHub to initialize
    else:
        print("Repository already exists on GitHub.")

    if not os.path.exists(repo_path):
        print(f"Cloning repository to {repo_path}...")
        run_command(f"gh repo clone {username}/{REPO_NAME}", cwd=base_dir)
    else:
        print(f"Local repository already exists at {repo_path}.")

    if not os.path.exists(repo_path):
        print("Error: Failed to set up local repository.")
        return

    # 4. Heart On Your Sleeve (React to an issue)
    print("Triggering 'Heart On Your Sleeve'...")
    issue_output, _ = run_command("gh issue create --title 'Heart Reaction' --body 'React to this'", cwd=repo_path)
    if "github.com" in issue_output:
        issue_url = issue_output.split('/')[-1]
        run_command(f"gh api repos/{username}/{REPO_NAME}/issues/{issue_url}/reactions -f content='heart'", cwd=repo_path)

    # 5. Quickdraw (Close within 5 mins)
    print("Triggering 'Quickdraw'...")
    qd_issue, _ = run_command("gh issue create --title 'Quickdraw Issue' --body 'Close fast'", cwd=repo_path)
    if "github.com" in qd_issue:
        qd_id = qd_issue.split('/')[-1]
        run_command(f"gh issue close {qd_id}", cwd=repo_path)

    # 6. YOLO (Merge without review)
    print("Triggering 'YOLO'...")
    run_command("git checkout main", cwd=repo_path)
    run_command("git pull origin main", cwd=repo_path)
    run_command("git checkout -b yolo-branch", cwd=repo_path)
    with open(os.path.join(repo_path, "yolo.txt"), "w") as f:
        f.write("YOLO!")
    run_command("git add yolo.txt", cwd=repo_path)
    run_command('git commit -m "YOLO commit"', cwd=repo_path)
    run_command("git push -u origin yolo-branch", cwd=repo_path)
    run_command("gh pr create --title 'YOLO PR' --body 'Merging without review'", cwd=repo_path)
    run_command("gh pr merge --merge --delete-branch", cwd=repo_path)

    # 7. Pair Extraordinaire (Co-authored commit)
    print("Triggering 'Pair Extraordinaire'...")
    run_command("git checkout main", cwd=repo_path)
    run_command("git pull origin main", cwd=repo_path)
    run_command("git checkout -b pair-branch", cwd=repo_path)
    with open(os.path.join(repo_path, "pair.txt"), "w") as f:
        f.write("Pairing with Octocat")
    run_command("git add pair.txt", cwd=repo_path)
    # The trailer must have two newlines before it
    commit_msg = "Add pair.txt\\n\\nCo-authored-by: Octocat <octocat@github.com>"
    run_command(f"git commit -m \"{commit_msg}\"", cwd=repo_path)
    run_command("git push -u origin pair-branch", cwd=repo_path)
    run_command("gh pr create --title 'Pair PR' --body 'Co-authored update'", cwd=repo_path)
    run_command("gh pr merge --merge --delete-branch", cwd=repo_path)

    # 8. Pull Shark (Tiers require many PRs, but let's do a few)
    print("Triggering 'Pull Shark' (Tier 1)...")
    run_command("git checkout main", cwd=repo_path)
    run_command("git pull origin main", cwd=repo_path)
    for i in range(1, 3):
        run_command(f"git checkout -b shark-branch-{i}", cwd=repo_path)
        with open(os.path.join(repo_path, f"shark_{i}.txt"), "w") as f:
            f.write(f"Shark {i}")
        run_command(f"git add shark_{i}.txt", cwd=repo_path)
        run_command(f"git commit -m \"Shark commit {i}\"", cwd=repo_path)
        run_command(f"git push -u origin shark-branch-{i}", cwd=repo_path)
        run_command(f"gh pr create --title 'Shark PR {i}' --body 'Beep beep'", cwd=repo_path)
        run_command("gh pr merge --merge --delete-branch", cwd=repo_path)
        run_command("git checkout main", cwd=repo_path)
        run_command("git pull origin main", cwd=repo_path)

    print("\nActions completed! Check your GitHub profile in a few minutes/hours.")
    print(f"Repository used: https://github.com/{username}/{REPO_NAME}")

if __name__ == "__main__":
    main()
