# UrtDemoRecorder

## Project's goal

This is a tool to record or watch demos from Urban Terror.
Recording demos in Urban Terror takes a long time when you have to do it one by one.
The recorder works with two demo's format :

- .dm68
- .urtdemo

You can change several parameters such as :

- DemoFov (Field of view used in the demo)
- aviframerate (frame per second when recording)
- Gun params ( size, position )

## Video-pipe

Video pipe allows you to record your demos a lot faster and with better quality

How to use it :

- https://github.com/BtbN/FFmpeg-Builds/releases
- Download the GPL version for your OS, example for a Windows user: https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
- Take the `ffmpeg.exe` and add it in your Urban Terror Folder
- Set this value in Urban Terror : -`cl_aviPipeFormat "-preset medium -crf 5 -vcodec libx264 -flags +cgop -pix_fmt yuv420p -bf 2 -codec:2 aac -strict -2 -b:a 160k -r:a 22050 -movflags faststart"`
  - Param that can be changed :
    -The range of the CRF scale is 0–51, where 0 is lossless (for 8 bit only, for 10 bit use -qp 0), 23 is the default, and 51 is worst quality possible. A lower value generally leads to higher quality, and a subjectively sane range is 17–28. Consider 17 or 18 to be visually lossless or nearly so; it should look the same or nearly the same as the input but it isn't technically lossless. We did some tests and 5 or lower give the best results for Urt.
- Use the video-pipe instead of normal video command (video-pipe checkbox)

# Svelte-Kit + Vite

This template should help get you started developing with Tauri and Svelte-Kit in Vite.

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Svelte](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode) + [Tauri](https://marketplace.visualstudio.com/items?itemName=tauri-apps.tauri-vscode) + [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer).
