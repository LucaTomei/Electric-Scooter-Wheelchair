# Electric Scooter Wheelchair

## Introduction

*Before illustrating the various assembly phases, I would first of all like to express my sincere gratitude to my thesis advisor [Prof. Andrea Vitaletti](https://andreavitaletti.github.io/) for the continuous support of my thesis and related research, for his patience, motivation and knowledge.
In addition to my thesis advisor, I would like to thank Mr. Massimo from [aeo srl](https://www.aeosrl.com/) for providing us with a folding wheelchair on loan. 'use. Without their support it would not have been possible to conduct this research.*

In recent years there has been a rapid explosion in the spread of electric scooters, especially in cities and urban neighborhoods, by virtue of the fact that these retain benefits on several fronts: granting sustainable mobility while allowing easy access to the various areas of the city. or points of interest.
Until now, the use of these means is only possible for people who do not have a severe disability, therefore with this mechanical thesis work we intend to obtain this possibility also for people with disabilities, in particular by focusing on the integration between an electric scooter and a wheelchair and on the '' adaptation of the scooter control software to a type of load other than that of common use.

The goal of this thesis project was to produce a first working prototype that allows any wheelchair owner to take advantage of the additional possibilities and features offered by an electric scooter.

## First Assembly and Experimental Results

This section will show the various ways in which a mechanical coupling between the wheelchair and the electric scooter has been provided. Specifically, two main ways of interconnecting the parts have been identified, each of which however has advantages and disadvantages that we will also illustrate through photographs and videos that show the type of assembly. In both cases, the support that allows the connection between the two parts is the same, therefore the use of one mode over another does not affect the components and is at the discretion of the end user. More specifically, a support has been created that is installed at the base of the wheelchair structure near the rear wheels, thus becoming an integral part of the wheelchair structure. A mobile component is added to this support which, by means of a knob, allows the scooter to be fixed to the aforementioned support.

The photos that describe the prototype 0 of the bracket and its first implementation are shown below.

<p align="center">
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/primo_prototipo.jpg" width="45%" />
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/staffa_misure.jpg" width="45%" /> 
</p>
<p align="center">
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/cuscinetto.JPG" width="45%" />
</p>

Specifically, three knobs were used connected to three respective threaded bars and to three anti-vibration nylon pads designed and 3D printed. The threaded bars have been cut to size and, through a joint in the part that connects them to the anti-vibration mounts, allows the scooter to be kept firmly on the support with respect to the longitudinal and lateral movements produced by acceleration, braking and steering phenomena. Furthermore, the knob placed in a horizontal position with respect to the ground allows to raise the position of the front wheels of the wheelchair which, in both assembly modes, would create problems of a kinematic nature. In this sense they are "disabled" in their functionality and therefore the movement of the wheelchair will be subject only to the traction and steering imposed by the scooter. In addition, by means of a steel hinge, the moving part connected to the support allows the scooter to enter under the wheelchair without it having to be lifted or moved.
Furthermore, since electric scooters do not have reverse gear at the level of the electric motor, it is necessary to ensure that this is still done even by those with disabilities. In this sense, the structure created does not in any way interfere with the user's ability to reverse in the same way as he would do with a wheelchair not equipped with a scooter. Specifically, by acting on the rear wheels of the wheelchair and making the steering using the handlebar of the scooter, it is possible to reverse without any effort without the scooter being an obstacle in carrying out these actions.

<p align="center">
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/blob/master/static/img/projects/wheelchair/Bracket%20Movement.gif" width="45%" />
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/docs/Wheelchair%20Bracket_Horizontal.png" width="45%" /> 
</p>

<p align="center">
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/IMG_3766.jpg" width="45%" />
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/IMG_3765.jpg" width="45%" /> 
</p>


### First assembly method

The first assembly method foresees that the rear wheel of the scooter is located before the “x” structure, that is the one that allows the wheelchair to be folded. The use of this mode requires that the steering wheel of the scooter is folded because otherwise it would be too far from the wheelchair seat. In this sense, the use of the folded steering allows the user to enjoy a wide view and at the same time to carry out steering maneuvers easily and without fatigue. On the other hand, however, the turning radius is considerably reduced, or by about 30% of the steering of the scooter, which effectively reduces the steering capacity of the vehicle itself. In light of this problem, a further method of assembly has therefore been envisaged, although this is the one that has the most advantages at the current stage of development. Some images and videos relating to this method of assembly and its use will be shown below.


<div align="center">
  <a href="https://www.youtube.com/watch?v=pedpYrB-Tpg"><img src="https://img.youtube.com/vi/pedpYrB-Tpg/0.jpg" alt="First assembly method - Indoor" width="45%"></a>
  <a href="https://www.youtube.com/watch?v=0CFREP4uoyM"><img src="https://img.youtube.com/vi/0CFREP4uoyM/0.jpg" alt="First assembly method - Driving" width="45%"></a>
</div>

### Second assembly method

The second assembly method foresees that the position of the rear wheel is located before the “x” structure of the wheelchair described above. In this case, unlike the previous driving mode, the handlebar is much closer to the user so it is not necessary to use it folded and this allows you to take full advantage of the steering radius of the scooter. On the other hand, however, this configuration reduces the field of vision of the end user since the steering will be located at a height higher than his shoulders. This is because the scooter is designed to be used in an upright position. Obviously this problem would be solved when using a scooter with telescopic steering, therefore able to adjust the height of the steering itself.
Some images and videos relating to this method of assembly and its use will be shown below.

<div align="center">
  <a href="https://www.youtube.com/watch?v=v104yqsH2Jk"><img src="https://img.youtube.com/vi/v104yqsH2Jk/0.jpg" alt="Second assembly method - Indoor" width="45%"></a>
  <a href="https://www.youtube.com/watch?v=Zkwy78TF8J8"><img src="https://img.youtube.com/vi/Zkwy78TF8J8/0.jpg" alt="Second assembly method - Driving" width="45%"></a>
</div>

## Graphical Results

Below we will illustrate numerous graphs aimed at showing the performance of the scooter with the standard firmware, driven without a wheelchair, and with the custom firmware created in this thesis, coupled to the wheelchair. Specifically, the graphs relating to current, battery discharge, temperature, residual distance, voltage and power supplied by the motor will be shown.

<p align="center">
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/results/2_curr%2Btemp.png" width="33%" />
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/results/2_batt%2Bdist%2Bvolt.png" width="33%" /> 
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/results/2_power.png" width="33%" /> 
</p>

From this point on we will show the graphs relating to the physical quantities that it was possible to acquire regarding the operation of the electric scooter coupled to the wheelchair.

<p align="center">
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/results/1_curr%2Btemp.png" width="33%" />
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/results/1_batt%2Bdist%2Bvolt.png" width="33%" /> 
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/results/1_power.png" width="33%" /> 
</p>

The graphs below show the test drive with the relative distance traveled during the road test.

<p align="center">
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/results/gif1.gif" width="45%" />
  <img src="https://github.com/LucaTomei/LucaTomei.github.io/raw/master/static/img/projects/wheelchair/results/gif2.gif" width="45%" /> 
</p>


## Conclusions and future work

The goal of this thesis project was to produce a first working prototype that allows any wheelchair owner to take advantage of the additional possibilities and features offered by an electric scooter.
On the basis of the experiments carried out, encouraging results emerged as it was possible to achieve the mechanical coupling between the two bodies and the modification of the firmware without affecting the functioning of the electric scooter and without adding further problems for the user. Furthermore, it was possible to achieve this without having to distort the structure and nature of the scooter and wheelchair, in such a way as to guarantee their operation regardless of the connection between the two.
On the other hand, less encouraging results also emerged from the experiments since, as shown in the paragraph relating to assembly methods, both do not allow to have a 100% efficient and effective guide since both modes have advantages and limitations due to the structure. physics of the two so heterogeneous media. In particular, the main defect relating to reduced visibility would be tackled when there are electric scooters with telescopic steering on the market which, however, are currently very little diffusion and in any case a modification of the steering would require a significant adaptation work. This problem would therefore not allow the use of sharing scooters. On the other hand, the second mode would allow the scooter to be used by both able-bodied and disabled users, but at the expense of a reduced turning radius when using a wheelchair. We therefore believe that this second mode is the most suitable to be used on a permanent basis and that allows access to the benefits and potential of the scooter to the widest possible audience.
However, there is still a lot of work to be done as this project could be extended to a larger number of brands of electric scooters and wheelchairs and also companies operating in the electric scooter rental market could be involved in order to share with them the results obtained in this thesis work thus allowing disabled people to be able to use the modified firmware on the basis of their needs, with a simple request to the server via an application.
Further developments could be aimed at obtaining a finer tuning of the firmware parameters and therefore more effective and comfortable for driving by people with disabilities, also adapting it to the various engine models available on the market. Further room for improvement can be had by integrating cutting-edge technologies in this project, for example through the use of machine learning for computer vision tasks. More specifically, video cameras could be integrated into the scooter and then used to be able to have a representation of the outside world and on the basis of this guarantee greater safety through the aid of machine learning algorithms, for example in helping the user to carry out the braking phase when an obstacle or a red light is detected.
In closing, further developments that have already been foreseen concern for example the possibility of installing a safety belt on the wheelchair, an increased battery that allows you to extend the autonomy of the scooter and a reinforcement of the scooter control unit that allows for greater performance. and faster engine reaction times.
The reinforcement of the control unit consists in adding tin and possibly a copper wire in the rear tracks of the control unit itself, where high levels of current pass through. In this way there will be an increase in the diameter of the same which will allow not to have overheating. A broader and more advanced work can include the replacement of mosfets with higher quality components without causing any damage to the control unit with firmware that use higher currents.



### For information about the project check out [my personal webpage](https://lucatomei.github.io) or follow me on:

<div align="center">
  <a href="https://github.com/LucaTomei/" ><img src="https://img.icons8.com/ios/50/000000/github--v2.gif" width="8%"/></a>
  <a href="https://www.youtube.com/playlist?list=PLc5qWHNIyMOJ6JQbtwOI_JOLSSAsy53RV"><img src="https://img.icons8.com/color/48/000000/youtube--v3.gif" width="8%"/></a>
  <a href="https://it.linkedin.com/in/luca-tomei-760296ab"><img src="https://img.icons8.com/color/48/4a90e2/linkedin-2--v2.gif" width="8%"/></a>
  <a href="https://www.facebook.com/profile.php?id=100010340402905"><img src="https://img.icons8.com/color/48/4a90e2/facebook-circled--v4.gif" width="8%"/></a>
  <a href="https://twitter.com/LucaTomei1995"><img src="https://img.icons8.com/color/48/000000/twitter-circled--v2.gif" width="8%"/></a>
</div>

