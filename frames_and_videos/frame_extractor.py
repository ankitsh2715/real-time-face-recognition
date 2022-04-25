#Code reused from project developed for Mobile computing course

import cv2
import os
import random

width = 160
height = 160
dim = (width, height)

def frameExtractor(path_to_video_files, path_to_frames):
    print("video files "+path_to_video_files)
    print("frames "+path_to_frames)

    video_files = os.listdir(path_to_video_files)

    for file in video_files:
        try:
            if os.path.splitext(file)[1] !='.mp4':
                continue
            print('extracting frames for video {}'.format(file));
            video = cv2.VideoCapture(os.path.join(path_to_video_files, file))
            print(video)
            count = 0
            success = 1
            arr_img = []
            
            # If such a directory doesn't exist, creates one and stores its Images
            if not os.path.isdir(os.path.join(path_to_frames, os.path.splitext(file)[0])):
                os.mkdir(os.path.join(path_to_frames, os.path.splitext(file)[0]))
            new_path = os.path.join(path_to_frames, os.path.splitext(file)[0])
            print("saving to : "+new_path)

            print("reading frames...")
            while success:
                success, image = video.read()
                arr_img.append(image)
                count += 1
                
            count = 0
            print("processing frames...")
            for i in range(len(arr_img)-1):
                image_path = os.path.join(new_path,"%d.png" % count)
                cv2.imwrite(image_path, arr_img[i])
                image_original = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
                resized_image = cv2.resize(image_original, dim, interpolation=cv2.INTER_LINEAR)
                image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
                cv2.imwrite(image_path, image_rgb)

                count += 1
                if count>100:
                    print("100 frames done. Stopping!")
                    break
        except:
            continue

video_file_path = os.path.dirname(os.path.abspath(__file__))+"/videos"
frame_path = os.path.dirname(os.path.abspath(__file__))+"/frames"

def main():
    print("Running frame extractor...")
    frameExtractor(video_file_path,frame_path)


if __name__ == "__main__":
    main()