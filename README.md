create a new repository on the command line
echo "# Pycharm" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/GhiaurLeonard1/Pycharm.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/GhiaurLeonard1/Pycharm.git
git branch -M main
git push -u origin main