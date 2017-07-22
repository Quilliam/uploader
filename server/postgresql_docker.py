"""
This creates a docker file for the postgres configuration
"""
import os
from app import create_app
from setup_environment import setup_environment_variables

setup_environment_variables()

config_name = os.getenv("FLASK_CONFIG") or "default"

app = create_app(config_name)

# Postgres Initialization Files
docker_file = 'Dockerfile'
source_dir = os.path.abspath(os.curdir)
destination_dir = os.path.join(source_dir, '../postgresql')

# Before creating files, check that the destination directory exists
if not os.path.isdir(destination_dir):
    os.makedirs(destination_dir)

# Create the 'Dockerfile' for initializing the Postgres Docker image
with open(os.path.join(destination_dir, docker_file), 'w') as postgres_dockerfile:
    postgres_dockerfile.write('FROM postgres:9.6')
    postgres_dockerfile.write('\n')
    postgres_dockerfile.write('\n# Set environment variables for postgres')
    postgres_dockerfile.write('\nENV POSTGRES_USER {}'.format(app.config.get('POSTGRES_USER')))
    postgres_dockerfile.write('\nENV POSTGRES_PASSWORD {}'.format(app.config.get('POSTGRES_PASSWORD')))
    postgres_dockerfile.write('\nENV POSTGRES_DB {}'.format(app.config.get('POSTGRES_DB')))
    postgres_dockerfile.write('\n')
