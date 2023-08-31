# Motion Filtering with OpenCV and Python

## Overview

This project demonstrates motion filtering using OpenCV and Python. Motion filtering is a technique used in computer vision to enhance or suppress motion in a video. It's commonly used for applications like video stabilization, object tracking, and noise reduction.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Video](#video)
- [Usage](#usage)
  - [Input Video](#input-video)
  - [Output Video](#output-video)
- [Motion Filtering Techniques](#motion-filtering-techniques)
  - [Background Subtraction](#background-subtraction)
  - [Optical Flow](#optical-flow)
- [Contributing](#contributing)
- [contact](#contact)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later installed on your system.
- Required Python packages installed (see [Installation](#installation)).
- Input video file (e.g., `input_video.mp4`) for motion filtering.

### Installation

-  Clone this repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/motion-filtering-with-opencv.git
   ```

## Video

1. output video

<video width="640" height="360" controls>
  <source src="output_video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

2. output video 2

<video width="640" height="360" controls>
  <source src="output_video 2.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Usage

### Input Video

The input video should contain scenes with motion that you want to enhance or suppress. The script will process this video and apply motion filtering techniques as specified.

### Output Video

The output video will be generated with the motion filtering applied. You can view the processed video to observe the effects of the chosen motion filtering technique.

## Motion Filtering Techniques

This project supports two motion filtering techniques:

### Background Subtraction

Background subtraction is a technique used to isolate moving objects from a video stream. It subtracts the background from each frame to highlight the moving objects.

### Optical Flow

Optical flow estimates the motion of pixels between consecutive frames. It can be used to detect and track motion in a video.

You can choose the motion filtering technique by specifying the appropriate command-line argument when running the script.

## Contributing

Contributions to this project are welcome. To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Open a pull request, describing your changes in detail.

## Contact

- Email : umairh1819@gmail.com
