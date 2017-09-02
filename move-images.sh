#!/bin/bash -e

echo 'Backing up images'
mv -v $PWD/images/* $PWD/backup/
echo 'Backing up complete'
