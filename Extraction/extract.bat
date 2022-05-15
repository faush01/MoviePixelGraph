mkdir images

C:\Install\ffmpeg\ffmpeg-5.0.1-full_build\bin\ffmpeg.exe ^
-i "\\192.168.0.16\Media\Movies\Gravity (2013)\Gravity.2013.720p.BluRay.x264-SPARKS.mkv" ^
-vf scale=1:1 ^
-sws_flags area ^
-f image2 ^
"images\test-%%07d.bmp"
