# Git command

### To check files
```
git status
git log
git diff -> To check differences between most recents versions versus modification
```

### To check remote
```
git remote
git remote -v
```

### To initialize a project
```
git init
git add nameOfTheFile.py OR git add . OR git add --all (to add all files)
git commit -m "messages"
git remote add origin https://github.com/example/Git-CheatSheet.git
```
### To push a project
```
git add nameOfTheFile.py OR git add . OR git add --all (to add all files)
git commit -m "messages"
git push -u origin main
```

### To delete a commit
git log -> To get the commit's number
git reset db92823dff820db7da9b637e49f6fbaa9ad73491 --hard -> To delete this commit