#!/usr/bin/python3
"""init file for easy storage call"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
