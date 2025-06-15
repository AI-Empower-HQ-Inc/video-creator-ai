from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video(images, audio_file, output_path, duration_per_image=5):
    clips = [ImageClip(img).set_duration(duration_per_image) for img in images]
    final_clip = concatenate_videoclips(clips)
    audio = AudioFileClip(audio_file)
    final = final_clip.set_audio(audio)
    final.write_videofile(output_path, fps=24)