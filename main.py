import argparse

import cv2


def get_config():
    parser = argparse.ArgumentParser(description="Tracking Test.")
    parser.add_argument(
        "-p", "--path", type=str, default="./data/video/test.mp4", help="path to video"
    )
    parser.add_argument(
        "--show", type=str, default="./data/video/test.mp4", help="show the video"
    )

    args = parser.parse_args()

    return args


def show_video(path):
    # 获得视频的格式
    videoCapture = cv2.VideoCapture(path)
    if not videoCapture.isOpened():
        print("Unable to open: " + path)
        exit(0)

    # 获得码率及尺寸
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (
        int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)),
    )
    fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

    # 读帧
    success, frame = videoCapture.read()
    while success:
        cv2.imshow("windows", frame)  # 显示
        cv2.waitKey(int(1000 / int(fps)))  # 延迟
        success, frame = videoCapture.read()  # 获取下一帧

    videoCapture.release()


if __name__ == "__main__":
    args = get_config()

    show_video(args.path)
