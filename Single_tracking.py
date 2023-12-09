import cv2
import sys
from random import randint

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']

tracker_type = tracker_types[1]

# Qual ferramenta usar
if int(minor_ver) < 3:
    tracker = tracker_type
else:
    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    if tracker_type == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
    if tracker_type == 'MCSRT':
        tracker = cv2.TrackerMCSRT_create()

print(tracker)
