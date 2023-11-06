from pathlib import Path

import cv2
from tqdm import tqdm


def show_video(path, cnt_max=900):
    # 获得视频的格式
    video_capture = cv2.VideoCapture(path)
    if not video_capture.isOpened():
        print("Unable to open: " + path)
        exit(0)

    fps = video_capture.get(cv2.CAP_PROP_FPS)
    cnt = 0
    ret = True

    for i in tqdm(range(cnt_max)):
        ret, frame = video_capture.read()
        cv2.imwrite(f"../data/video/split_images/{i + 1}.jpg", frame)

        if not ret:
            raise Exception("Video is too short!")

    video_capture.release()


if __name__ == "__main__":
    base_path = Path("../data/video")
    Path("../data/video/split_images").mkdir(parents=True, exist_ok=True)

    show_video("../data/video/test.mp4")
