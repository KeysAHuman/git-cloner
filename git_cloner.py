import os
import subprocess

file_path = "github_links.txt"

clone_dir = "git_clone/"

if not os.path.exists(clone_dir):
    os.makedirs(clone_dir)

with open(file_path, "r") as file:
    repo_links = file.readlines()

for link in repo_links:
    link = link.strip()
    if link:
        repo_name = link.split("/")[-1].replace(".git", "")
        repo_path = os.path.join(clone_dir, repo_name)

        if os.path.exists(repo_path):
            print(f"Repository '{repo_name}' already exists. Skipping clone.")
        else:
            print(f"Cloning repository: {link}")
            try:
                subprocess.run(["git", "clone", link], cwd=clone_dir, check=True)
                print(f"Successfully cloned {link}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to clone {link}: {e}")
            except Exception as e:
                print(f"An error occurred while cloning {link}: {e}")

print("All repositories have been processed.")
