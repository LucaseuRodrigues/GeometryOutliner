-How the site works
First of all, this project does not use Django GIS, so all calculations are approximate and 
intended for study purposes only.

-What is Geometry Line?
Geometry Line is a website designed to calculate the area and perimeter of a determined region 
based on user-provided coordinates.

-How users define an area
The website provides a dedicated section where the user can enter geographic coordinates.
An area must be defined using:
a minimum of 3 points
a maximum of 10 points
Each point is defined as a pair of longitude and latitude values.

-Rules for a valid polygon
All data input will be guided and incremental, not submitted in a single block.
To successfully generate a polygon, the following rules must be followed:
All coordinates must be valid numeric values.
The polygon must contain at least 3 points.
Only simple polygons are accepted.
The polygon edges must not intersect or cross each other.
The calculated area of the polygon must be greater than zero.
If any of these rules are violated, the polygon will not be generated.

-User accounts and data persistence
To save assignments and previous calculations, users must register and log in to their account.
All saved data can be accessed later for review.
