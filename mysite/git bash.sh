git add -A .
git commit -m "Routine Update"
git push -u origin master
expect "Username for 'https://github.com': "
send "mdabdullahalalaminp@gmail.com"

echo e "\n\n\n\n"
read -p "********* Uploaded to GitHub Finished ********" a
