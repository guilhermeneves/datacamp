# Scheduler

Commercial schedulers: Airflow, Luigi, Rundeck, etc...
Cron scheduler: free, simple, customizable.

Cron is a time-based job scheduler.

### Crontab: is a central file to keep track of cron jobs.

`crontab -l`: will display all tasks scheduled via cron

We have two options to add a cron to crontab.

**Method 1**: modify crontab using texteditor (nano, vi, etc..)
**Method 2**: echo the scheduler command in crontab
`echo "* * * * * python create_model.py" | crontab`

**CRON has a 60-second granularity limit, which means the most frequent job we can schedule is one run every minute**

"*MINUTE *HOUR *DAY-MONTH *MONTH *DAY-WEEK"