import cv2

def play_video(video_path, speed, window_name):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30

    delay = max(1, int(1000 / (fps * speed)))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow(window_name, frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Normal speed
play_video("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/3 minute sample video - Google Search.mp4", 1.0, "Normal Speed")

# Slow motion (0.5x)
play_video("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/3 minute sample video - Google Search.mp4", 0.5, "Slow Motion")

# Fast motion (2x)
play_video("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/3 minute sample video - Google Search.mp4", 2.0, "Fast Motion")
