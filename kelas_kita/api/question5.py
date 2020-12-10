import os

#converter = os.system('ffmpeg -i input.mp4 output.m3u8')
converter = os.system('ffmpeg -i input.mp4 -g 60 -hls_time 2 -hls_list_size 0 -hls_segment_size 500000 output.m3u8')
#converter = os.system('ffmpeg -i input.mp4 -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls filename.m3u8')