import cv2
import numpy as np
import os


def analyze_video(video_path, clip_duration=5, threshold=0.5):
    """
    Analyzes a video and generates a list of clips labeled as positive or negative.

    Args:
        video_path: Path to the input video file (.mp4).
        clip_duration: Duration of each clip in seconds.
        threshold: Confidence threshold for determining positive/negative.
                    (Example: If average frame positivity > threshold => positive clip)


    Returns:
        A list of lists, where each inner list contains:
            [label (str), clip_path (str)].
        Label is "positive" or "negative".
        clip_path is the path to the saved clip.
    """

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    clip_frames = int(clip_duration * fps)  # Number of frames in each clip

    clips = []
    clip_num = 0

    for i in range(0, frame_count, clip_frames):  # Iterate through the video in clip-sized chunks
        clip_positivity = []  # Store positivity scores for each frame in the clip

        out_clip_path = f"clip_{clip_num}.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use appropriate codec
        out = cv2.VideoWriter(out_clip_path, fourcc, fps, (int(video.get(3)), int(video.get(4))))

        for j in range(clip_frames):  # Process frames within the current clip
            ret, frame = video.read()
            if not ret:  # End of video
                break

            # *** Placeholder for Positivity Analysis ***
            # Replace with your actual analysis logic (e.g., object detection, sentiment analysis, etc.)
            # positivity = analyze_frame(frame)  # Your analysis function
            positivity = np.random.rand()  # Dummy positivity: Random value between 0 and 1
            # ******************************************
            clip_positivity.append(positivity)
            out.write(frame)  # write current frame to output clip

        out.release()  # release video writer after processing the clip

        # Determine clip label based on average positivity
        average_positivity = np.mean(clip_positivity) if clip_positivity else 0  # Handle potentially empty lists
        label = "positive" if average_positivity > threshold else "negative"

        clips.append([label, out_clip_path])
        clip_num += 1

    video.release()
    return clips


# Example Usage:
video_file = "1MB.mp4"  # Replace with your video file
clip_info = analyze_video(video_file)

for label, clip_path in clip_info:
    print(f"Clip: {clip_path}, Label: {label}")