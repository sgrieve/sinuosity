## Sinuosity

[![DOI](https://zenodo.org/badge/265599848.svg)](https://zenodo.org/badge/latestdoi/265599848)

The following code needs `fiona` and `shapely` installed, using either `pip` or `conda`, and expects a shapefile containing a single polyline.

It works by creating two shapely `LineString`s and then using their length attribute to calculate sinuosity.

If you are using a geographic coordinate system, you will need to calculate great circle distances. To do this I usually use `pyproj`'s `geod.inv` method.

### Usage

Run the script with a shapefile filename as follows:

```
python sinuosity.py myline.shp
```

This will calculate the sinuosity of the line stored in `myline.shp` and output the result to the screen.

### Install

This code used `shapely` and `fiona` which can both be `pip` installed using:

```
pip install -r requirements.txt
```

### Licence

This code is MIT Licensed, see `LICENCE.txt` for details.

### Citing

If you would like to cite this script, you can grab the bibtex file [here](https://doi2bib.org/bib/10.5281/zenodo.3835970).
