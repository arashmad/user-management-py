"""
Initialization module for the tests package.

This module is responsible for setting up the testing environment and making
test-related functionality available to other parts of the project.
"""

import os

os.environ['service_namespace'] = 'test-service'

os.environ['ROOT_PATH'] = ''
os.environ['APP_PORT'] = "8000"
os.environ['ALLOWED_CLIENT'] = "*"
