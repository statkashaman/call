#!/usr/bin/env python
import os
import os.path
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "call.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
