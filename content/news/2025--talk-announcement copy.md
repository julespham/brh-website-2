---
title: "Become a member! Get yourself on the website!"
date: 2025-09-09
excerpt: "If you're not a member, it's easy to join! If you are, let's get you listed on our member directory! If you have a cool project, we would love to showcase you on our site."
highlight: true
---
**Members**: If you have not yet done it, it would be great to see you on our [membership page](https://bostonrobothackers.com/members.html). It's so simple. Make a text file called yourname.md and email it to me.

```
---
name: "Johny Appleseed"
role: "Robot Hacker"
image: "images/people/ja.jpg"
featured: true
skills: ["ROS", "Software Engineering", "Robotics"]
github: "https://github.com/johnny"
linkedin: "https://www.linkedin.com/in/j_appleseed/"
projects: ["Apple Robot"]
opentowork: false
---
Johnny Appleseed, born John Chapman in 1988, is a modern software developer known for "planting seeds of open-source code" across the tech landscape. Working remotely from coffee shops throughout the American West in his signature flannel and worn boots, he specializes in creating lightweight programming libraries for startups and small development teams.
---

title: GreenThumb AI
date: 2025-03-15
status: prototype development
image: images/projects/greenthumb.png
text: Smart gardening assistant!
lead: Johnny Appleseed
members: 3
github: https://github.com/campusrover/greenthumb-ai
excerpt: An autonomous plant care robot that monitors soil conditions, waters plants, and provides growth recommendations using computer vision and machine learning.

An autonomous plant care robot designed to revolutionize indoor gardening through intelligent monitoring and care. This second-generation prototype combines computer vision, environmental sensing, and machine learning to create a comprehensive plant health management system.

### Software
Built on ROS2 Humble with custom navigation and manipulation packages. The system uses OpenCV for plant health analysis through leaf color and growth pattern recognition. Machine learning models trained on plant disease datasets provide early warning systems for common issues. The core AI pipeline integrates sensor fusion for optimal watering schedules.
### Hardware
The robot features a mobile base with omnidirectional wheels for greenhouse navigation. A 6-DOF robotic arm with a custom end-effector handles watering and light positioning tasks. Environmental sensors include soil moisture probes, pH meters, ambient light sensors, and a thermal camera for stress detection. The main compute unit is a Jetson Xavier NX connected to an Arduino Mega for low-level sensor management.
<img src="../images/projects/greenthumb.png" alt="GreenThumb robot" style="float: left; margin: 20px 20px 20px 0; border-radius: 8px; height: 250px;">

The modular design allows for different plant care attachments to be swapped based on plant type. A water reservoir system with precision pumps delivers exactly the right amount of water based on soil analysis. LED grow lights on adjustable arms can be positioned optimally for each plant's photosynthetic needs.
<img src="../images/projects/plant_sensor.jpeg" alt="Custom soil sensor" style="float: right; margin: 0 0 20px 20px; border-radius: 12px; height: 250px">
The custom soil sensor probe is entirely 3D printed with embedded conductivity sensors. It can measure moisture, pH, and basic nutrient levels simultaneously. The probe's modular design allows for easy cleaning and calibration, and different probe lengths can be printed for various pot sizes and root depths.