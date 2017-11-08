#!/bin/sh

while [ 1 = 1 ]
do
      i3-msg "[class=.] border none; [id=$(xdotool getactivewindow)] border pixel 2"
      sleep 0.07
done
      
