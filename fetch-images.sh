#!/bin/bash -e

PI_USER="pi"
PI_IP="192.168.0.12"

PI_IMAGES_FOLDER="/home/pi/camera/images/*.png"
LOCAL_BACKUP_FOLDER="./camera-images/"

echo "Starting backup of images from Raspberry Pi"
scp -p ${PI_USER}@${PI_IP}:${PI_IMAGES_FOLDER} ${LOCAL_BACKUP_FOLDER}
echo "Image backup complete"

