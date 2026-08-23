GitHub Command :
$Create and Switch to Your BranchIf you have not created your personal branch yet, create it and switch to it immediately:
git checkout -b my-personal-branch
# Stage all modified and new files
git add .

# Save the changes with a clear description
git commit -m "Add my custom code updates"
git push -u origin my-personal-branch
4. Future PushesFor any future updates you make on this exact same branch, you do not need to type the full command or the branch name again. You can simply run:
git push
