#!/bin/bash
opencv_createsamples -img first.jpg -bg bg.txt -info info/info$1.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1400
