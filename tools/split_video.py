from pathlib import Path
from typing import Union

import cv2
from tqdm import tqdm


def split_video(path: Path, cnt_max=900):
    video_path = str(path / "test.mp4")
    split_images_path = str(path / "split_images")

    # 获得视频的格式
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print("Unable to open: " + video_path)
        exit(0)

    fps = video_capture.get(cv2.CAP_PROP_FPS)
    cnt = 0
    ret = True

    for i in tqdm(range(cnt_max)):
        ret, frame = video_capture.read()
        cv2.imwrite(split_images_path + f"/{i + 1}.jpg", frame)

        if not ret:
            raise Exception("Video is too short!")

    video_capture.release()


if __name__ == "__main__":
    video_data_path = Path("../data/video")
    split_images_dir = video_data_path / "split_images"
    test_video_path = video_data_path / "test.mp4"
    if not split_images_dir.exists():
        split_images_dir.mkdir(parents=True, exist_ok=True)

    split_video(video_data_path)
