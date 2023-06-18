# Pose Estimation Keypoints Extraction Tutorial

This repository provides code examples for extracting keypoints features using different state-of-the-art (SOTA) pose estimation models. It covers both top-down and bottom-up approaches.

## Pose Estimation

Pose estimation is a computer vision task that involves detecting and locating human body keypoints, such as the joints of the arms, legs, and torso, in an image or video. It aims to infer the spatial position and orientation of a person's body from visual data.



## Repository Organization

The repository is organized as follows:

Pose Modules/

    - topdown/
        -Alphapose
    
    -bottomup/
        -openpifpaf/
        -openpose/
        -movenet/


### Top-Down Approach

In the `Pose Modules/topdown` directory, you will find the Alphapose code for top-down pose estimation.

- To use Alphapose, you need to first clone and install it from their official GitHub repository: [https://github.com/MVIG-SJTU/AlphaPose.git](https://github.com/MVIG-SJTU/AlphaPose.git).
- They have already provided the command for extracting features in the form of JSON from an image or video.
- Additionally, you will find a modified version of the `demo.py` file under the `scripts` folder in this repository. This modified code allows you to extract JSON pose features from folders containing multiple videos, which is often used when training on large datasets. Detailed instructions on how to use this modified code can be found in the `demo.txt` file.


### Bottom-Up Approach

In the `Pose Modules/bottomup` directory, you will find the following pose estimation models:

- **Openpose**: An open-source pose estimation library that provides accurate keypoints detection. 
    1. First, install tf_pose_estimation from this github repository: https://github.com/gsethi2409/tf-pose-estimation.git
    2. Inside 'Pose Modules/bottomup/openpose' folder contains openpose.py which contains function to return pose features. https://openpifpaf.github.io/intro.html

- **Openpifpaf**: Another pose estimation library that supports multi-person and crowd pose estimation.
    1. First install openpifpaf using *pip install openpifpaf* or you can visit this github for further information:  https://openpifpaf.github.io/intro.html
    2.  Inside 'Pose Modules/bottomup/openpifaf' contains openpifaf.py which contains function to extract keypoints features from an Image.

- **Movenet**: A lightweight and efficient pose estimation model suitable for real-time applications.

    1. In order to use Movenet first download the saved_model(movenet_singlepose_thunder_4) from: https://tfhub.dev/google/movenet/singlepose/lightning/4. 
    2. Then you can use movenet.py( inside 'Pose Modules/bottomup/Movenet' ) to extract keypoints features from an image.
    3. In this turtorial, another famous similar bottomup approach named "PoseNet" is not used because MoveNet shows better performance. 

Please refer to the individual directories for each pose estimation model to access the code examples, usage instructions, and any additional documentation specific to that model.

Feel free to explore, modify, and integrate the provided codes into your own projects!

## Qualitative Analysis

The below figure shows the qualitative comparison of different pose estimators. This qualitative analysis was conducted in a research paper in which I co-authored (equal contribution with the first author). You can access the full paper through this link: [(Exploring Human Pose Estimation and the Usage of Synthetic Data for Elderly Fall Detection in Real-World Surveillance)](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9870817). If you find the paper useful, please consider citing it.

![Pose estimation modules comparision.](images/Qualitative%20Analysis.jpg)


## Contributing

## Contributing

Contributions to this tutorial are welcome! If you have any improvements, suggestions, or additional pose estimation models that you would like to include, please submit a pull request.

Please read the [CONTRIBUTING.md](link-to-contributing-file) file for more details on how to contribute.

## License

This tutorial is distributed under the [MIT License](link-to-license-file).
