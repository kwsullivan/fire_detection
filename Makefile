SAMPLE=sample_fire_images.png
THRESH=50


# python3 fire.py YCC 50 ./fire_grdtruths/s1.jpg ./output/output_new2.jpg sample_fire_images.png ./fire_grdtruths/
# SPACE THRESHOLD INPUT_FILE OUTPUT_FILE SAMPLE_FILE GROUND_TRUTH

# GROUND TRUTH TESTING
tests: c1 c2 c3 c4 s1 s2 s3 s4
c1:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/c1_large.jpg ./output/output_c1.jpg sample_fire_images.png ./fire_grdtruths/c1_flameB.tif
c2:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/c2.jpg ./output/output_c2.jpg sample_fire_images.png ./fire_grdtruths/c2_flameB.tif
c3:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/c3.png ./output/output_c3.jpg sample_fire_images.png ./fire_grdtruths/c3_flameB.tif
c4:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/c4.jpg ./output/output_c4.jpg sample_fire_images.png ./fire_grdtruths/c4_flameB.tif

s1:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/s1.jpg ./output/output_s1.jpg sample_fire_images.png ./fire_grdtruths/s1_flameB.tif
s2:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/s2.tif ./output/output_s2.jpg sample_fire_images.png ./fire_grdtruths/s2_flameB.tif
s3:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/s3.jpg ./output/output_s3.jpg sample_fire_images.png ./fire_grdtruths/s3_flameB.tif
s4:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/s4.png ./output/output_s4.jpg sample_fire_images.png ./fire_grdtruths/s4_flameB.tif