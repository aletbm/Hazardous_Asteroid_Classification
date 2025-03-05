# ☄️ Hazardous Asteroid Classification - NASA JPL Asteroid by [Alexander D. Rios](https://linktr.ee/aletbm)

<img src="https://i.postimg.cc/76MpGPhY/unnamed-1.png">

# Abstract

The ***problem*** we address is identifying potentially hazardous asteroids for planet Earth. The scope of this project can be interesting for various entities, ranging from astronomical research centers to aerospace agencies.

The ***motivation*** behind this project arises from the difficulty I believe exists in tackling such a topic, which allows me to apply all my mathematical, physical, and statistical knowledge for data study. I recognize that it is one of the most complicated projects I have undertaken due to my limited knowledge in the field of astronomy, but I believe I have the necessary tools to deal with some of the challenges this type of project imposes.

The ***first hypothesis*** I can formulate is that asteroids with orbits closer to Earth’s orbit have higher chances of representing a risk for the planet than those further away, and that this is independent of their size.

To verify my hypothesis, I used various methods, both qualitative and quantitative, as well as different designs. Some of the main ones were visualizations like boxplots and statistical descriptions of the data. Key visualizations included boxplots of the `H` and `moid` variables, as well as visualizations of orbits close to Earth and the `neo` vs. `moid` histogram.

Some of the ***extensions of my work*** were calculating the orbital paths of the asteroids through 5 orbital elements or Keplerian elements, the approximate calculation of the asteroid diameters, since this and some other data (`prefix`, `name`, `albedo`, `diameter_sigma`, and `diameter`) had to be excluded from the study due to missing data, i.e., they contained too many null values making them unusable columns. I also had to discard 25,637 records due to extreme outliers, which skewed the useful data. These were discarded considering the vast amount of data available (1M records), but I took care not to unbalance the data more than it already was. On the other hand, I filled in the missing `H` data with the mean because they are homogeneous values.

**Conclusion**: Based on the tools used so far, I concluded that the danger of an asteroid lies in the possibility of it intercepting Earth’s orbit or not. This means that asteroids with orbits close to Earth’s orbit are potentially hazardous, while those with orbits farther away may also be, but with lower probabilities. I also demonstrated that their size does not contribute to their potential danger unless they can intercept Earth’s orbit. Clearly, if a massive asteroid were to intercept Earth, it would cause greater damage than a less massive one.

# Objective  
Throughout human history, there have been countless discussions about the end of the world. One of the main and most plausible causes is the impact of an asteroid. Such an event could be so catastrophic that it threatens to wipe out all existing life on planet Earth.  

But from our position as data scientists, what can we do? To answer this question, we have access to a dataset containing information about various asteroids known to humanity. This dataset describes specific physical and temporal characteristics of these asteroids. Based on this, several questions arise:  

> **Is there a pattern that allows us to identify potentially hazardous asteroids?**  

> **What are the probabilities of an asteroid colliding with Earth in the coming years?**  

## Business context  
An **observatory in Argentina** has detected several asteroids near Earth's orbit. Additionally, it has determined that this weekend, there will be a meteor shower, which consists of debris from asteroids. Fortunately, the observatory has been collecting precise data on these asteroids for several years up to the present.  

**NASA** has hired us to **identify visual patterns** in this data to help **classify** whether these asteroids pose a threat to our ecosystem. The goal is to take preventive actions to **alter their course and avoid a potential impact**, thus preventing the extinction of humanity.  

## Business problem  
Based on the data provided by the observatory, we need to create visualizations to answer the following questions:  

- **Are all asteroids near Earth's orbit potentially hazardous?**  
- **What type of orbit do most asteroids have?**  
- **Is there a relationship between an asteroid's hazard level and its physical size?**  
- **Between Mars and Jupiter, there is an asteroid belt. How does Jupiter's massive size affect the orbits of these asteroids?**  
- **Are there asteroids with orbits smaller than Earth's that pose a potential threat?**  

## Analytical context  
The observatory has provided us with a dataset in `.CSV` format containing approximately one million records on asteroids. Some of the recorded characteristics include orbital eccentricity, longitude of the descending node, absolute magnitude of the asteroid, among 43 other available features.  

The internal index of the dataset is named `id`.  

Based on this data, we need to carry out the following tasks:  

- **Read and preview the dataset.**  
- **Detect and process missing data, determine whether it can be discarded, or otherwise, fill in the gaps.**  
- **Detect and process outliers.**  
- **Identify relevant features.**  
- **Analyze and create visualizations of the data to answer the proposed questions and identify useful patterns.**

# About the dataset  

This dataset was created by the researcher in Astronomy and Astrophysics, Mir Sakhawat Hossain. It is officially maintained by the Jet Propulsion Laboratory (JPL) of the California Institute of Technology, an organization supervised by NASA. This dataset contains various types of data related to asteroids.  

It can be used in Machine Learning projects for both classification and regression tasks.  

## Column definitions 
| Feature | Description |
|----|-------------|
| id | Internal ID |
| spkid | Primary ID |
| fullname | Full designation/name of the object |
| pdes | Primary designation of the object |
| name | Object name as per the International Astronomical Union |
| prefix | Comet prefix |
| neo | Near-Earth Object (Y/N) |
| pha | Potentially Hazardous Asteroid (Y/N) |
| H | Absolute magnitude parameter |
| diameter | Object diameter (equivalent to a sphere) (km) |
| albedo | Geometric albedo |
| diameter_sigma | 1-sigma uncertainty in the object's diameter (km) |
| orbit_id | Orbit solution ID |
| epoch | Osculation epoch in Julian day format (TBD) |
| epoch_mjd | Osculation epoch in Modified Julian day format (TBD) |
| epoch_cal | Osculation epoch in calendar date/time format (TBD) |
| equinox | Reference frame equinox |
| e | Eccentricity |
| a | Semi-major axis (au) |
| q | Perihelion distance (au) |
| i | Inclination. Angle relative to the x-y ecliptic plane (deg) |
| om | Longitude of the ascending node (deg) |
| w | Argument of perihelion (deg) |
| ma | Mean anomaly (deg) |
| ad | Aphelion distance (au) (also called Q) |
| n | Mean motion (deg/d) |
| tp | Time of perihelion passage (TBD) |
| tp_cal | Time of perihelion passage in calendar date/time format (TBD) |
| per | Orbital sidereal period (d) |
| per_y | Orbital sidereal period (years) |
| moid | Minimum orbit intersection distance with Earth (au) |
| moid_ld | Minimum orbit intersection distance with Earth (LD) |
| sigma_e | Eccentricity (1-sigma uncertainty) |
| sigma_a | Semi-major axis (1-sigma uncertainty) (au) |
| sigma_q | Perihelion distance (1-sigma uncertainty) (au) |
| sigma_i | Inclination. Angle relative to the x-y ecliptic plane (1-sigma uncertainty) (deg) |
| sigma_om | Longitude of the ascending node (1-sigma uncertainty) (deg) |
| sigma_w | Argument of perihelion (1-sigma uncertainty) (deg) |
| sigma_ma | Mean anomaly (1-sigma uncertainty) (deg) |
| sigma_ad | Aphelion distance (1-sigma uncertainty) (au) |
| sigma_n | Mean motion (1-sigma uncertainty) (deg/d) |
| sigma_tp | Time of perihelion passage (1-sigma uncertainty) (TBD) |
| sigma_per | Orbital sidereal period (1-sigma uncertainty) (d) |
| class | Orbit classification |
| rms | Normalized orbit fit RMS (arcsec) |

# Visualizations with Poliastro
![Asteroids](./src/asteroids.gif)

