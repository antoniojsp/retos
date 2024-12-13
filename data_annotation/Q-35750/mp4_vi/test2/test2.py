from moviepy.editor import VideoFileClip
import cv2
import os


# Function to label clips as positive or negative (placeholder)
def analyze_clip(clip_path):
    # Placeholder for sentiment analysis. Currently returns random.
    # In real scenarios, this would involve deep learning models or pre-tagged data.
    import random
    return "pos" if random.random() > 0.5 else "neg"


# Function to split video into clips based on criteria
def split_video(video_path, output_dir, clip_duration=5):
    # Load the video using MoviePy
    video = VideoFileClip(video_path)
    duration = video.duration

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    clips = []  # List to store information about clips

    # Process the video in chunks
    start = 0
    while start < duration:
        # Define end of the current clip
        end = min(start + clip_duration, duration)

        # Extract clip and save to file
        clip = video.subclip(start, end)
        clip_path = os.path.join(output_dir, f"clip_{int(start)}_{int(end)}.mp4")
        clip.write_videofile(clip_path, codec="libx264", audio_codec="aac")

        # Analyze the clip for sentiment
        sentiment = analyze_clip(clip_path)

        # Append result to clips list
        clips.append([sentiment, clip_path])

        # Move to next clip
        start = end

    return clips


# Example usage
video_path = "1MB.mp4"
output_dir = "output_clips"
clip_duration = 10  # seconds

clips = split_video(video_path, output_dir, clip_duration)

# Print the list of clips with sentiment
for clip in clips:
    print(clip)