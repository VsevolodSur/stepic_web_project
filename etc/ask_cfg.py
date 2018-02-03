# bind = 'localhost:8080'
bind = 'localhost:8000'
# bind = '192.168.1.201:8080'
worker = 3

#   Logging
#
#   logfile - The path to a log file to write to.
#
#       A path string. "-" means log to stdout.
#
#   loglevel - The granularity of log output
#
#       A string of "debug", "info", "warning", "error", "critical"
#
errorlog = '/home/box/web/gunicorn_error.log'
loglevel = 'debug'
accesslog = '/home/box/web/gunicorn_access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
