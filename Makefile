SAMPLE=sample_fire_images.png
THRESH=50


# python3 fire.py YCC 50 ./fire_grdtruths/s1.jpg ./output/output_new2.jpg sample_fire_images.png ./fire_grdtruths/
# SPACE THRESHOLD INPUT_FILE OUTPUT_FILE SAMPLE_FILE GROUND_TRUTH

# GROUND TRUTH TESTING
tests: c1 c2 c3 c4 s1 s2 s3 s4

c1:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/c1_large.jpg ./output/output_c1.jpg $(SAMPLE) ./fire_grdtruths/c1_flameB.tif
c2:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/c2.jpg ./output/output_c2.jpg $(SAMPLE) ./fire_grdtruths/c2_flameB.tif
c3:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/c3.png ./output/output_c3.jpg $(SAMPLE) ./fire_grdtruths/c3_flameB.tif
c4:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/c4.jpg ./output/output_c4.jpg $(SAMPLE) ./fire_grdtruths/c4_flameB.tif

s1:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/s1.jpg ./output/output_s1.jpg $(SAMPLE) ./fire_grdtruths/s1_flameB.tif
s2:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/s2.tif ./output/output_s2.jpg $(SAMPLE) ./fire_grdtruths/s2_flameB.tif
s3:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/s3.jpg ./output/output_s3.jpg $(SAMPLE) ./fire_grdtruths/s3_flameB.tif
s4:
	python3 fire.py YCC $(THRESH) ./fire_grdtruths/s4.jpg ./output/output_s4.jpg $(SAMPLE) ./fire_grdtruths/s4_flameB.tif

nofire:
	python3 fire.py YCC $(THRESH) ./fireImages1/trump.jpg ./output/output_s4.jpg $(SAMPLE) ./fire_grdtruths/s4_flameB.tif

fptests: fp1 fp2 fp3 fp4 fp5 fp6

fp1:
	python3 fire.py YCC $(THRESH) ./falsePositives/fp-1.jpg ./output/fp_output/output_fp-1.jpg $(SAMPLE)
fp2:
	python3 fire.py YCC $(THRESH) ./falsePositives/fp-2.jpg ./output/fp_output/output_fp-2.jpg $(SAMPLE)
fp3:
	python3 fire.py YCC $(THRESH) ./falsePositives/fp-3.jpg ./output/fp_output/output_fp-3.jpg $(SAMPLE)
fp4:
	python3 fire.py YCC $(THRESH) ./falsePositives/fp-4.jpg ./output/fp_output/output_fp-4.jpg $(SAMPLE)
fp5:
	python3 fire.py YCC $(THRESH) ./falsePositives/fp-5.jpg ./output/fp_output/output_fp-5.jpg $(SAMPLE)
fp6:
	python3 fire.py YCC $(THRESH) ./falsePositives/fp-6.jpg ./output/fp_output/output_fp-6.jpg $(SAMPLE)

concat:
# IMAGE 	GROUND_TRUTH 	OUTPUT_FILE
cat_fp1:
	python3 concat.py ./falsePositives/fp-1.jpg ./output/fp_output/output_fp-1.jpg ./output/stack/cat_fp-3.jpg
cat_fp2:
	python3 concat.py ./falsePositives/fp-2.jpg ./output/fp_output/output_fp-2.jpg ./output/stack/cat_fp-2.jpg
cat_fp3:
	python3 concat.py ./falsePositives/fp-3.jpg ./output/fp_output/output_fp-3.jpg ./output/stack/cat_fp-3.jpg
cat_fp4:
	python3 concat.py ./falsePositives/fp-4.jpg ./output/fp_output/output_fp-4.jpg ./output/stack/cat_fp-4.jpg
cat_fp5:
	python3 concat.py ./falsePositives/fp-5.jpg ./output/fp_output/output_fp-5.jpg ./output/stack/cat_fp-5.jpg
cat_fp6:
	python3 concat.py ./falsePositives/fp-6.jpg ./output/fp_output/output_fp-6.jpg ./output/stack/cat_fp-6.jpg