# Astron_1221_Project_1
# **Outline**
#### **Astro Objects**
We define a class of messier objects including their common name, ra, dec, a link to a public commons image, and the apparent angular resolution in  square arcseconds

#### **Telescopes List**
We define a telescope and eye piece class

Create a list common telescopes and eyepieces

The class contains the telescope's focal length, the eyepiece's fov, and the eyepiece's focal length

#### **Height in the sky**
Calculate the Alt Az for a given object

User specifies the object from the class, user's latitude and longitude, date and time, UTC offset

Calculate the Alt Az based on position, date + time, and RA + DEC

Output Altitude in sky based on time

#### **Plots**

Call height in sky for 24 hours starting at User's noon to the following day at noon

Make a plot of object's height in sky over given 24 hour period

Call height in sky for 1 year starting at the first of the month

Make a plot of object's height in sky at midnight over following year

#### **% of Sky Taken Up by Object**

User specifies the telescope and eyepiece used

Calculate the square arcseconds that given setup covers in the sky

Calculate the percent of the field of view is taken up by a given astronomical object, defined in astronomical object class


#### **AI Integration**
Prompt AI and define our tools as height in sky suite and percentage observed tools

User passes their desired object and either latitude/longitude/date/time/UTC offset, or telescope eyepiece setup information

AI uses predefined functions to perform tasks asked by user and returns the given information as well as an image of the object they requested, as defined in the astronomical object class.
