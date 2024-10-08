import time
import logging
logger = logging.getLogger(__name__)

def main():
{% if cookiecutter.resource_type == 'deployment' %}
    while True:
        logger.info('Dummy deployment is up and running')
        time.sleep(10)
{ % elif cookiecutter.resource_type == 'cronjob' %}
    for i in range(10):
        logger.info('Dummy cronjob is up and running')
        time.sleep(10)
{ % else %}
    logger.error('Unsupported resource type')
{ % endif %}


if __name__ == '__main__':
    main()