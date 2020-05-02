# flask_skeleton
# bash aliases
alias activate_venv='cd /var/www/chatur/flask_skeleton/dev; source /var/www/chatur/venvs/bin/activate;'
alias start_flask='uwsgi --py-autoreload 1 -s /opt/uwsgi/uwsgi.12.sock -w manage:app  --chmod-socket=666 --master --processes 1 --threads 1 --ignore-sigpipe --ignore-write-errors --disable-write-exception --buffer-size=4096'

