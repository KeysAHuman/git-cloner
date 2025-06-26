import os
import subprocess

# Path to the text file containing GitHub repository URLs
file_path = "github_links.txt"

# Directory where the repositories will be cloned
clone_dir = "git_clone/"

# Create the target directory if it doesn't exist
if not os.path.exists(clone_dir):
    os.makedirs(clone_dir)

# Read the file and get the list of GitHub repository links
with open(file_path, "r") as file:
    repo_links = file.readlines()

# Clone each repository
for link in repo_links:
    link = link.strip()  # Remove any leading/trailing whitespaces or newlines
    if link:  # Ignore empty lines
        print(f"Cloning repository: {link}")
        try:
            # Run the git clone command
            subprocess.run(["git", "clone", link], cwd=clone_dir, check=True)
            print(f"Successfully cloned {link}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone {link}: {e}")
        except Exception as e:
            print(f"An error occurred while cloning {link}: {e}")

print("All repositories have been processed.")
