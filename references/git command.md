# Git command

### To check files
```
git status
git log -> To check the history of all commits
git diff -> To check differences between most recent commit versus modification
```

### To check remote
```
git remote
git remote -v
```

### To initialize a project
```
git init
git remote add origin https://github.com/example/Git-CheatSheet.git
git add nameOfTheFile.py OR git add . OR git add --all (to add all files)
git commit -m "messages"
```

### To push a project
```
git add nameOfTheFile.py OR git add . OR git add --all (to add all files)
git commit -m "messages"
git push -u origin main
```

### To delete a commit
```
git log -> To get the commit's number
git reset db92823dff820db7da9b637e49f6fbaa9ad73491 --hard -> To delete this commit
```

### To create branch
```
git checkout -b BranchName  #Create and move directly to the branch
git branch -#To check we are on the good branch
git fetch origin # fetch all changes
git pull origin main # pull changes from the origin remote, master branch and merge them into my_branch
git status #To check new or modified files
git add . #To add all your changes
git commit -m "Your message" #To indicate what you were working on
git push -u origin BranchName #Push your branch to remote
git checkout main #Change branch to main
git merge Branchname -m "your message" #Merge your branch on main
```
### To modify branch name
```
git branch -m oldname newname
```