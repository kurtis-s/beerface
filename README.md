# beerface
[Chernoff faces](https://en.wikipedia.org/wiki/Chernoff_face) data visualization of beer brewing styles.

The beer style characteristics are from the [BJCP Style Guidelines](http://www.bjcp.org/stylecenter.php) from 2008, 
specifically the XML version available here: http://www.bjcp.org/docs/xmlstyleguide.zip.  The facial features of
the Chernoff faces are generated using the average of the low/high values for IBU, SRM, OG, FG, and ABV in each beer
category.

To create the visualization

1.  Run stylecsvgen.py to parse beer category characteristics information from styleguide2008.xml (requires [lxml](http://lxml.de/))
2.  Run beerface.R to generate a PDF with Chernoff faces (requires [dplyr](https://cran.r-project.org/web/packages/dplyr/index.html) and [aplpack](https://cran.r-project.org/web/packages/aplpack/index.html))


![Beer category data visualization](./beerfaces_afedit.gif?raw=true)
