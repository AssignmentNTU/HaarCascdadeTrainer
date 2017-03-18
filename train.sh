#!/usr/bin/env bash
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 1000 -numStages 10 -w 30 -h 30
