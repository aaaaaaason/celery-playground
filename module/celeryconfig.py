# https://docs.celeryproject.org/en/stable/userguide/configuration.html

accept_content = ['json']

result_accept_content =['json']

# This setting can be used to rewrite any task attribute from the configuration.
# The setting can be a dict, or a list of annotation objects that filter for 
# tasks and return a map of attributes to change.
task_annotations = None

# Task hard time limit in seconds. The worker processing the task will 
# be killed and replaced with a new one when this is exceeded.
#task_time_limit

# The SoftTimeLimitExceeded exception will be raised when this is exceeded. 
# The task can catch this to clean up before the hard time limit comes
#task_soft_time_limit

# Late ack means the task messages will be acknowledged after the task has
# been executed, not just before (the default behavior).
task_acks_late = True

# When enabled messages for all tasks will be acknowledged even if they fail or time out.
# Only if task_acks_late is enabled.
task_acks_on_failure_or_timeout = False

# Default: No rate limit.
#task_default_rate_limit

result_backend = 'mongodb://localhost:27017'

mongodb_backend_settings = {
    'database': 'celery',
    'taskmeta_collection': 'celery_taskmeta',
    'username': 'root',
    'password': 'password',
    'authSource': 'admin'
}

# If enable, backend will try to retry on the event of recoverable exceptions
# instead of propagating the exception. It will use an exponential backoff
# sleep time between 2 retries.
result_backend_always_retry = True

#result_backend_max_sleep_between_retries_ms = 10000
#result_backend_base_sleep_between_retries_ms = 10
result_backend_max_retries = 3

# Time (in seconds, or a timedelta object) for when after stored task tombstones will be deleted.
# A built-in periodic task will delete the results after this time (celery.backend_cleanup), 
# assuming that celery beat is enabled. The task runs daily at 4am.
# For the moment this only works with the AMQP, database, cache, Couchbase, and Redis backends.
# result_expires

# A list of routers, or a single router used to route tasks to queues. 
# When deciding the final destination of a task the routers are consulted in order.
# A router can be specified as either:
#   - A function with the signature (name, args, kwargs, options, task=None, **kwargs)
#   - A string providing the path to a router function.
#   - A dict containing router specification:
#       Will be converted to a celery.routes.MapRoute instance.
#   - A list of (pattern, route) tuples:
#      Will be converted to a celery.routes.MapRoute instance.
#task_routes

broker_url = 'amqp://root:password@localhost:5672'