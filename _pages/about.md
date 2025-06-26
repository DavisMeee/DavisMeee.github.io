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

# **Welcome to My Page!**

I am currently a Ph.D. Candidate in the [Faculty of Electrical Information Engineering](https://www.sydney.edu.au/engineering/about/our-people/research-students/tong-chen-494.html) at **The University of Sydney** (Supervised by Associate Prof. Luping Zhou and Dr. Dong Yuan). My research interests include Brain Decoding, Video Generation, and Medical Imaging.

<!-- <img src="images/my.jpg" alt="sym" width="50%" style="display: block; margin: 0 auto;"> -->


# 🔥 News
<style>
.scroll-container {
    height: 280px;
    overflow-y: auto;
    padding: 10px;
    border: 1px solid #ddd;
    background-color: #f9f9f9;
    border-radius: 5px;
}

.scroll-container ul {
    padding: 0;
    margin: 0;
    list-style-type: none;
}

.scroll-container li {
    margin-bottom: 10px;
}
</style>

<div class="scroll-container">
    <ul>
        <li>*2025.06*: &nbsp;🎉🎉 Three papers <strong>SurgSora</strong>, <strong>WiD-PET</strong>, and <strong>Endo-4DGX</strong> are accepted by <strong>MICCAI2025</strong>!</li>
        <li>*2025.03*: &nbsp;🎉🎉 Our work <strong>DiN: Diffusion Model for Robust Medical VQA with Semantic Noisy Labels</strong> has been accepted at <strong>CVPR2025</strong>!</li>
        <li>*2024.09*: &nbsp;🎉🎉 <strong>LighTDiff: Surgical Endoscopic Image Low-Light Enhancement with T-Diffusion</strong> win the <span style="color:red;">Best Paper Runner-Up Award</span> at <strong>MICCAI2024</strong>!</li>
        <li>*2024.09*: &nbsp;🎉🎉 <strong>LighTDiff: Surgical Endoscopic Image Low-Light Enhancement with T-Diffusion</strong> received <span style="color:red;">Oral Presentation</span> at <strong>MICCAI2024</strong>!</li>
        <li>*2024.07*: &nbsp;🎉🎉 I received my Ph.D. Offer from the University of Sydney！</li>
        <li>*2024.07*: &nbsp;🎉🎉 Our work <strong>EndoUIC: Promptable Diffusion Transformer for Unified Illumination Correction in Capsule Endoscopy</strong> has been accepted at <strong>MICCAI2024</strong>!</li>
        <li>*2024.05*: &nbsp;🎉🎉 Our work <strong>LighTDiff: Surgical Endoscopic Image Low-Light Enhancement with T-Diffusion</strong> has been <strong>Early Accepted</strong> at <strong>MICCAI2024</strong>!</li>
        <li>*2024.02*: &nbsp;🎉🎉 Our work <strong>MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data</strong> has been accepted at <strong>ICML2024</strong>!</li>
        <li>*2023.07*: &nbsp;🎉🎉 Our work <strong>LLCaps: Learning to Illuminate Low-Light Capsule Endoscopy with Curved Wavelet Attention and Reverse Diffusion</strong> received <span style="color:red;">Oral Presentation</span> at <strong>MICCAI2023</strong>!</li>
    </ul>
</div>

<!-- - *2023.03*: &nbsp;🎉🎉 I received my M.Phil. Offer from the University of Sydney！ -->

# 💻 Experience
- 2025.04 - Present, [Research Intern] [Alibaba DAMO Academy](https://damo.alibaba.com/research-areas?language=en), Alibaba Group, Hangzhou, China.
- 2023.10 - 2025.01, [Researcher] [MedARC Neuroimaging](https://www.medarc.ai/) Leads by [Paul S. Scotti](https://paulscotti.github.io/), Stability AI.
- 2022.03 - 2024.03, [External Collaborator] Department of Electronic Engineering, The Chinese University of Hong Kong, Hong Kong. Supervised by [Prof. Hongliang Ren](https://www.ee.cuhk.edu.hk/en-gb/people/academic-staff/professors/prof-ren-hongliang), PI of [RenLab](http://www.labren.org/mm/)
- *2021.11 - 2022.06*, [Research Intern], MengShi Automatic Driving Lab, Tsinghua University, Beijing. Supervised by [A/Prof. Xinyu Zhang](https://scholar.google.com.hk/citations?user=0Q7pN4cAAAAJ&hl=zh-CN).
- *2021.06 - 2022.06*, [Research Intern], UV Lab of Ministry of Education for Photoelectronic Imaging Technology and System, Beijing Institute of Technology, Beijing. Supervised by [A/Prof. Yi Tang](https://www.researchgate.net/profile/Yi-Tang-73).


# 📝 Publications 
*†represents co-first authors*
**SurgSora: Object-Aware Diffusion Model for Controllable Surgical Video Generation**<br>
**T Chen†**, S Yang†, J Wang†, L Bai†, H Ren, L Zhou<br>
Medical Image Computing and Computer Assisted Intervention (**MICCAI**), 2025. <br>
- [Project Page](https://surgsora.github.io)\| [Paper](https://arxiv.org/abs/2412.14018)\| [Code](https://github.com/DavisMeee/SurgSora)

**SurgSora: Object-Aware Diffusion Model for Controllable Surgical Video Generation**<br>
Q Lyu†, **T Chen†**, E Guo†, Y Wang, L Zhou<br>
Medical Image Computing and Computer Assisted Intervention (**MICCAI**), 2025. <br>
- Paper and Code Coming Soon!

**LighTDiff: Surgical Endoscopic Image Low-Light Enhancement with T-Diffusion**<br>
**T Chen†**, Q Lyu†, L Bai†, E Guo, H Gao, X Yang, H Ren, L Zhou<br>
Medical Image Computing and Computer Assisted Intervention (**MICCAI**), 2024. <span style="color:red;">*[Best Paper Runner-Up Award, Oral, 3/2771]*</span><br>
- [Paper](https://arxiv.org/abs/2405.10550)\| [Code](https://github.com/DavisMeee/LighTDiff)
<!-- -  \| [Demo](https://github.com/lofrienger/Single_SurgicalScene_For_Segmentation) -->


**EndoUIC: Promptable Diffusion Transformer for Unified Illumination Correction in Capsule Endoscopy**<br>
L Bai†, **T Chen†**, Q Tan†, W.J Nah, Y Li, Z He, S Yuan, J Wu, Z Chen, M Islam, Z Li, H Liu, H Ren<br>
Medical Image Computing and Computer Assisted Intervention (**MICCAI**), 2024. <br>
- [Paper](https://arxiv.org/abs/2406.13705)\| [Code](https://github.com/longbai1006/EndoUIC)



**MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data**<br>
P.S Scotti†, M Tripathy†, C.K.T Villanueva†, R Kneeland†, **T Chen**, A Narang, C Santhirasegaran, J Xu, T Naselaris, K.A Norman, T.M Abraham<br>
The Forty-first International Conference on Machine Learning (**ICML**), 2024.
- [Project Page](https://medarc-ai.github.io/mindeye2/)\| [Paper](https://arxiv.org/abs/2403.11207)\| [Code](https://github.com/MedARC-AI/MindEyeV2)

**LLCaps: Learning to Illuminate Low-Light Capsule Endoscopy with Curved Wavelet Attention and Reverse Diffusion**<br>
L Bai†, **T Chen†**, Y Wu, A Wang, M Islam, H Ren<br>
Medical Image Computing and Computer Assisted Intervention (**MICCAI**), 2023. <span style="color:red;">*[Oral, Top 3%]*</span><br>
- [Paper](https://arxiv.org/pdf/2307.02452)\| [Code](https://github.com/longbai1006/LLCaps)

# 🎖 Honors and Awards
- *2024.09* **Best Paper Runner-Up Award at MICCAI 2024**
- *2024.09* **Oral Presentation Award at MICCAI 2024**
- *2023.07* **Oral Presentation Award at MICCAI 2023**

# 📖 Educations
- *2023.03 - 2026.9(expected)*, Ph.D., Electrical Information Engineering, the University of Sydney, Sydney, Australia.
- *2018.09 - 2022.07*, B.S., Opto-electrical Engineering, Beijing Insititute of Technology, Beijing, China.

# 📚 Teaching
**Teaching Assistant:**
- 2023-2024 Fall ELEC5622 Signals, Software and Health
- 2024-2025 Fall ELEC5622 Signals, Software and Health

<hr class="horizontal-line">
<div style="width: 30%; margin: 0 auto;">
	<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=a&t=tt&d=pUwp76-FPWZ_9p-R6BSJ--0FAcHR9spdMm0_5h4Eyak'></script>
	<p style="text-align: center; color: grey; font-size: small;">
    &copy; Tong CHEN | Last updated: Oct 2024
	</p>

</div>
		


