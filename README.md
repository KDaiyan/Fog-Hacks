
# Fog Hacks
This project creates a system for autonomous vehicles to detect objects and street signs in foggy environments to allow for safer driving under limited visibility conditions. This is intended to be a cheaper and more versatile solution than LiDAR.

It captures the vehicle's view using a camera and then performs object detection using the YOLOv10 model. This identifies key elements such as other vehicles, road obstacles, pedestrians, and street signs. If a street sign is identified, it performs a second scan using another model to extract the relevant information from the street sign and present it to the "driver."

This is a simulated model with a screen representing the vehicle's view and a fog machine creating artificial fog to simulate the intended environment. A prototype involving a moving model is planned for the future.

## Demo

The model can be run purely on the software side and does not have to be tested in a foggy setting.

![Software simulation on non-foggy setting](/figures/software_simulation_fogless.png)

The model was specifically optimized for low-visibility conditions caused by fog. The following shows a practical application of the system:

![Foggy setting test run](/figures/practical_simulation_foggy.png)
## Development Stages

The system was thoroughly planned and designed before development began. After the necessary hardware components were selected and an initial software framework was established, the physical frame was the first component to be created.

![Model design schematics](/figures/model_design.png)

The frame was 3D printed, and the necessary components such as the fog disks, Raspberry Pi 5, cameras, and displays were budgeted and purchased. The final assembled model is shown below:

![Final model implementation](/figures/complete_prototype.png)

Throughout the development process, images of foggy roads were collected whenever appropriate weather and road conditions were present. In addition, publicly available images and datasets of foggy roads were obtained and used in accordance with their respective licensing and usage permissions. Dataset annotation and management were performed using Roboflow Universe.

![Roboflow Data Training](/figures/roboflow_dataset.png)
## Software Requirements
- Docker Desktop 4.0+ (or Docker Engine on Linux)
- Python 3.9+ (for local development and utility scripts)
- Git
## Installation

**1**. Clone the repository:

```bash
git clone <repository-url>
cd FogHacks
```

**2**. Ensure Docker is installed and running on your system.

**3**. Build the Docker image using the provided Dockerfile:

```bash
docker build -t foghacks .
```

**4**. Start the Docker container:

```bash
docker run -it foghacks
```

**5**. Follow the project-specific instructions inside the container to train, evaluate, or run the object detection models.

## Notes

All required machine learning frameworks, libraries, and runtime dependencies are installed through the Docker environment. No additional package installation should be required on the host system.
## Authors

- [Alejandro Gomez](https://www.github.com/AleGomez15213)
- [Andrew Sagun](https://www.github.com/AndrewSagun)
- [Daiyan Kazi](https://www.github.com/KDaiyan)
- [Jordon Xu](https://www.github.com/Jordon-Xu1)
- [Ryan Tran](https://www.github.com/octokatherine)
- [Sean Liem](https://www.github.com/syliem1)

## Acknowledgements

 - [Yolov10 Model](https://github.com/THU-MIG/yolov10)
 - [Foggy Data Set](https://app.roboflow.com/foghacks-pgihy/foggy-stumc-auyqa)



## License
This program is free to use under the [MIT](https://choosealicense.com/licenses/mit/) License and can be used, modified, and redistributed without permission.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



