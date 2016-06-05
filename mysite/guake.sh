a=$(pwd)
guake -n $a --execute-command="cd '$a'; python manage.py runserver"  -r "server";

guake -n $a --execute-command="cd '$a'"  -r "command";

guake -n $a --execute-command="cd '$a'"  -r "test";



# subl .;
# subl .;
# subl .;
# subl .;
google-chrome 127.0.0.1:8000;

google-chrome 127.0.0.1:8000/admin --incognito;