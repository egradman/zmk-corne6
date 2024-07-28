image::
	git pull
	pdm run python image_generator.py
	rm *.png
	~/go/bin/zmk-viewer generate -f /tmp/corne.keymap crkbd/r2g
	montage crkbd_r2g_split_3x6_3_default_layer.png crkbd_r2g_split_3x6_3_lower_layer.png crkbd_r2g_split_3x6_3_raise_layer.png -tile 1x3 -geometry +0+0 output.jpg  
	mogrify -resize x960 output.jpg
	rm *.png

flash::
	mv ~/Downloads/firmware.zip .
	unzip firmware.zip

left::
	cp corne_left-nice_nano_v2-zmk.uf2 /Volumes/NICENANO

right::
	cp corne_right-nice_nano_v2-zmk.uf2 /Volumes/NICENANO
