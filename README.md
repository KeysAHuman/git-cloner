# GitHub Repo Cloner 🧬

A super simple Python script that clones multiple GitHub repositories listed in a text file.

## 🚀 Features

   - Reads a list of GitHub repository URLs from a text file
   - Clones each repo into a designated folder
   - Handles basic errors gracefully
   - No external Python dependencies

## 📁 File Structure

├── git_cloner.py # The main script
├── github_links.txt # Text file with GitHub repo URLs (one per line)
└── git_clone/ # Output directory for cloned repositories

## 🛠 Requirements:

   - Python 3.x
   - `git` installed and accessible from the command line

## 📝 Usage:

1. **Create a `github_links.txt` file**  
   Add one GitHub repo URL per line, like:

	https://github.com/username/repo1.git
	https://github.com/username/repo2.git
	https://github.com/username/repo3.git

2. **Run the script**

```
	python clone_repos.py
	Check the git_clone/ directory
	All repositories will be cloned into this folder (it’s created automatically).
```
🧠 Notes:

   - Empty lines in github_links.txt are ignored.
   - If a repo fails to clone, an error message will be printed, but the script will continue.


✅ Example Output:

```
	Cloning repository: https://github.com/username/repo1.git
	Successfully cloned https://github.com/username/repo1.git
	Cloning repository: https://github.com/username/repo2.git
	Failed to clone https://github.com/username/repo2.git: ...
	All repositories have been processed.
```

Feel free to fork, improve, or use this script in your own projects!
