---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

🔥**Welcome to My Page!**🔥

I am currently a first-Year Master student in the [Department of Mechanical Engineering](https://me.stanford.edu) at **Stanford University**. I received my Bachelor degree in Robotics Engineering at the [College of Mechanical and Electrical Engineering](https://mech.buct.edu.cn), Beijing University of Chemical Technology (BUCT). My research interests include soft robots, robot navigation, robot learning, medical mechatronics, and healthcare robots.

<!-- <img src="images/my.jpg" alt="sym" width="50%" style="display: block; margin: 0 auto;"> -->


# 🔥 News
- *2023.04*: &nbsp;🎉🎉 Our poster **Concentric Agonist-antagonist Robots for Neurosurgical Applications** has been accepted as **Best submission for lighting talk** at RoboSoft2024: Soft Robotics Inspired Biology Workshop 2024!
- *2024.04*: &nbsp;🎉🎉 MOur paper on **Sim2Real-RL soft robotic navigation** has been accepted by **ARSO 2024** to be held in Hong Kong!
- *2023.07*: &nbsp;🎉🎉 My first paper as a co-first author "Sim-to-Real Transfer of Soft Robotic Navigation Strategies That Learns from the Virtual Eye-in-Hand Vision" has been published on **IEEE Transactions on Industrial Informatics**!
- *2023.07*: &nbsp;🎉🎉 Our work "Sim-to-Real Segmentation in Robot-assisted Transoral Tracheal Intubation" win the **Best Poster Award** at ICRA 2023 Workshop!
- *2023.07*: &nbsp;🎉🎉 Our work "Domain Adaptive Sim-to-Real Segmentation of Oropharyngeal Organs" has been published on **MBEC**！

<!-- # 📝 Ongoing Project


<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">CAD</div><img src='images/ONE.png' alt="sym" width="100%"></div></div>
<div class='paper-box-image'><div><div class="badge">Real Machine</div><img src='images/onecable.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-image'><div><div class="badge">SOFA Simulation</div><img src='images/onesim.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**OneCable Continuum Robot Project**


- Using only one cable to achieve 3 motions: Pushing, Pulling and Twisting
- Will submit to a top-tier journal!
</div>
</div>
 -->


# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE-TII</div><img src='images/sim2.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Sim-to-Real Transfer of Soft Robotic Navigation Strategies That Learns From the Virtual Eye-in-Hand Vision**

J. Lai, **T.-A. Ren (Co-first author)**, W. Yue, S. Su, J. Y. K. Chan, and H. Ren

- Medical scene 3D reconstruction in [SOFA Framework](https://www.sofa-framework.org/)
- Soft robot modeling and navigation with [SOFTROBOTS plugin](https://project.inria.fr/softrobot/)
- Closed-loop soft robot navigation with that **learns** from the virtual eye-in-hand vision
- [Supply Video](https://youtu.be/vQ4xzFM9iwk)\| [Paper](https://ieeexplore.ieee.org/abstract/document/10171986)
<!-- -  \| [Demo](https://github.com/lofrienger/Single_SurgicalScene_For_Segmentation) -->

</div>
</div>

<!-- <div class='paper-box'> -->
<div class='paper-box' style="display: flex; justify-content: space-between;">
<div class='paper-box-image'><div><div class="badge">Experiment Setup</div><img src='images/Experiment_Setup.png' alt="sym" width="150%"></div></div>
<div class='paper-box-image'><div><div class="badge">Autonomous Navigation</div><img src='images/Autonomous_Navigation.gif' alt="sym" width="150%"></div></div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MBEC</div><img src='images/domain.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Domain Adaptive Sim-to-Real Segmentation of Oropharyngeal Organs**

Guankun Wang, **Tian-Ao Ren**, Jiewen Lai, Long Bai, and Hongliang Ren

- [Paper](https://link.springer.com/article/10.1007/s11517-023-02877-0)

</div>
</div>

# 💬 Projects
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CharmLab 24Winter</div><img src='images/charm24spring.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Concentric Agonist-antagonist Robots for Neurosurgical Applications**

**Tian-Ao Ren**, Zhongchun Yu, Brian Vuong, Antonio Meola, and Allison M. Okamura

- Develop a miniature end effector equipped with two CAARs, designed to carry out surgical actions as directed by a surgeon, through its end-mounted gripper.
- RoboSoft2024: Soft Robotics Inspired Biology Workshop 2024
- [Best submission for lightning talks](https://www.colorado.edu/lab/jayaram/RoboSoft2024)
- [Poster](https://drive.google.com/file/d/1_OrWDOYpiKpdDFcmk0fL9glgCR9Nf2Y1/view?usp=sharing)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CharmLab 23Fall</div><img src='images/charm23fall.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Wearable for High Precision Elbow Angle Measurement**

- Motion Capture System to collect ground truth data of elbow angle
- Soft Sensor System to collect sensor data
- Design experiments to verify the accuracy of mapping method

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Final Year Project</div><img src='images/fyp.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**A SOFA-based Gravity-Aware Portable Soft Robot**
- Designed a 7-driven soft robot: 6 cable-driven actuator and 1 Sliding actuator
- Work on simulation, design, embedded coding and communication to build a Sim2Real verify platform
- Build a real machine to verify the feasibility of the platform
- IMU-Gravity-SOFA-Real-machine Performance
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Final Year Project</div><img src='images/fyp_sim2real.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**A SOFA-based Sim2Real System that can Verify Soft Continuum Robot Fast**
- Calibrate sim2real Gap
- Socket-UDP/CAN BUS/Serial Port to build the communication system
- Kinematics and dynamics of soft robots can be quickly verified
- Video Speed 15x

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Cruising</div><img src='images/crusing.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Floor Cruising with Dynamic Obstacle Avoidance**
- Maximum speed of 2 m/s
- TEB algorithm for local planning
- Multi-sensor fusion positioning to increase localization accuracy
- [Supply Video](https://youtu.be/cD4d4wI3bkI)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Sim2Real</div><img src='images/rm.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**[ICRA2022 RoboMaster University Sim2Real Challenge](https://air.tsinghua.edu.cn/robomaster/sim2real_icra22.html)**
- Team *777* - on behalf of Beijing University of Chemical Technology (Third Prize)
- Use VINS-Mono location algorithm
- D435 + IMU mode to improve motion tracking performance and make up gaps in illumination changes
- [Supply Video](https://youtu.be/BxEthzIn8SQ)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SwarmingRobot</div><img src='images/muliti.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Swarming Robot Navigation: Sim2Real Transfer**
- Migrated multi-machine cooperative operation composite robot model in IsaacSIM
- High stability and obstacle avoidance ability
- [Supply Video](https://youtu.be/3UGTcBENg5Y)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Robotics Arm</div><img src='images/arm.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Sim2Real Transfer of ARX-5s robot (a 6-DOF robotic arm)**
- [Supply Video](https://youtu.be/jVsMxDsDUM4)
<!-- - [Robotics Arm Dancing](https://www.youtube.com/watch?v=NW4ZE4y-8hU) -->
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">HASEL</div><img src='images/HASEL.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">


**Design and Characteristics of A Hydraulic Amplification-Based Soft-Exoskeleton Robotic Module**
- Specially designed the casting mold to adapt to different application scenarios
- Simulated the deformation of soft beam with pneumatic-HASELs and the assembled soft gripper in SOFA

</div>
</div>

<!-- <div class='paper-box' style="display: flex; justify-content: space-between;">
<div class='paper-box-image' ><div><div class="badge">Intro PouchJacket</div><img src='images/pounchPic.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-image' ><div><div class="badge">Simulation</div><img src='images/pounch.gif' alt="sym" width="100%"></div></div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tensegrity Robot</div><img src='images/rod.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">


**Tensegrity Robot Simulation(2 rods)**

</div>
</div> -->

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">IPR Model</div><img src='images/mcm.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Bitcon or Gold? --- An investment strategy of IPR(Imatation-Prediction-Risk) model based on ARIMA**
- Compared ARIMA and LSTM models, resulted in ARIMA achieving better accuracy, even when adding the less effective LSTM model to our Imitation model and Risk model.

</div>
</div> -->


# 🎖 Honors and Awards
- *2023.07* **Best Poster Award at ICRA 2023 Workshop**
- *2023.07* **Outstanding Graduates in Beijing** 
- *2021-2022* National Scholarship of China (**TOP 0.2% in China**)
- *2019-2020* Li Wen & Yang Yan Scholarship (**TOP 1**)
- *2020-2021* Jinfa Technological Scholarship (**TOP 0.5% in College of Mechanical and Electrical Engineering**)  
- *2021-2022* First Prize Scholarship of BUCT  

# 📖 Educations
- *2023.09 - 2025.07(expected)*, M.S., Mechanical Engineering, Stanford University, California, U.S.
- *2019.09 - 2023.07*, B.Eng., Robotics Engineering, Beijing University of Chemical Technology, Beijing, China


# 💻 Internships
- *2024.04 - present*, [Research Assistant] BDML, Stanford University, CA. Supervised by [Prof. Mark Cutkosky](http://bdml.stanford.edu/Profiles/MarkCutkosky), PI of [BDML](http://bdml.stanford.edu/)
- *2023.10 - 2024.03*, [Research Assistant] Charm Lab, Stanford University, CA. Supervised by [Prof. Allison Okamura](https://charm.stanford.edu/Main/AllisonOkamura), PI of [Charm Lab](https://charm.stanford.edu/)
- *2023.01 - 2023.09*, [Research Assistant] Shenzhen Research Institute, The Chinese University of Hong Kong, Hong Kong. Supervised by [Prof. Hongliang Ren](https://www.ee.cuhk.edu.hk/en-gb/people/academic-staff/professors/prof-ren-hongliang), PI of [MMLab](http://www.labren.org/mm/)

- *2022.06 - 2022.12*, [Summer Research Intern] Dept of Electronic Engineering, The Chinese University of Hong Kong, Hong Kong. Supervised by [Prof. Hongliang Ren](https://www.ee.cuhk.edu.hk/en-gb/people/academic-staff/professors/prof-ren-hongliang), PI of [MMLab](http://www.labren.org/mm/)

- *2021.12 - 2023.05*, [Research Intern], [Institute of AI Industry Research (AIR)](https://air.tsinghua.edu.cn/en/index.htm), Tsinghua University, Beijing. Supervised by [Prof. Guyue Zhou](https://air.tsinghua.edu.cn/en/info/1046/1196.htm), PI of AIR DISCOVER Lab.