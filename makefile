all:
	python imagine_pixels.py foo.ppm
	convert foo.ppm foo.png
