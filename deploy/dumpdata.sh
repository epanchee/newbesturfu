source /home/best-admin/newbesturfu/venv/bin/activate
python /home/best-admin/newbesturfu/manage.py dumpdata --exclude=contenttypes --exclude=auth.permission --indent=4 --natural-foreign > /home/best-admin/newbesturfu/dumps/dump$$.json
deactivate
