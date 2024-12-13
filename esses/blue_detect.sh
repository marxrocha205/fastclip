ffmpeg -y -hide_banner -loglevel error -i $1 -vf "crop=200:200" out.mp4 && ffprobe -f lavfi movie=out.mp4,signalstats -show_entries frame_tags=lavfi.signalstats.HUEAVG -of flat 2>&1 | grep frames.frame | sed 's/[^"]*"\([^"]*\)".*/\1/' | awk 'BEGIN {max = 0; min = 999999} {if ($1>max) max=$1; if ($1<min) min=$1} END {print (max-min < 1 && max>290 && max<310 ? "blue" : "ok")}'
