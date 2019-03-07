SAMPLE=sample_fire_images.png
THRESH=100
COMPILER:=
OPEN:=

ifeq ($(OS),Windows_NT)
	COMPILER=py
	OPEN=
	OSFLAG += WIN
else
	COMPILER=python3
	OPEN=open
	OSFLAG += OSX
endif

# python3 fire.py YCC 50 ./fire_grdtruths/s1.jpg ./output/output_new2.jpg sample_fire_images.png ./fire_grdtruths/
# SPACE THRESHOLD INPUT_FILE OUTPUT_FILE SAMPLE_FILE GROUND_TRUTH

# GROUND TRUTH TESTING

tests: c1 c2 c3 c4 s1 s2 s3 s4

c1:
	$(COMPILER) fire.py YCC $(THRESH) ./fire_grdtruths/c1_large.jpg ./output/output_c1.jpg $(SAMPLE) ./fire_grdtruths/c1_flameB.jpg
c2:
	$(COMPILER) fire.py YCC $(THRESH) ./fire_grdtruths/c2.jpg ./output/output_c2.jpg $(SAMPLE) ./fire_grdtruths/c2_flameB.jpg
c3:
	$(COMPILER) fire.py YCC $(THRESH) ./fire_grdtruths/c3.png ./output/output_c3.jpg $(SAMPLE) ./fire_grdtruths/c3_flameB.jpg
c4:
	$(COMPILER) fire.py YCC $(THRESH) ./fire_grdtruths/c4.jpg ./output/output_c4.jpg $(SAMPLE) ./fire_grdtruths/c4_flameB.jpg

s1:
	$(COMPILER) fire.py YCC $(THRESH) ./fire_grdtruths/s1.jpg ./output/output_s1.jpg $(SAMPLE) ./fire_grdtruths/s1_flameB.jpg
s2:
	$(COMPILER) fire.py YCC $(THRESH) ./fire_grdtruths/s2.jpg ./output/output_s2.jpg $(SAMPLE) ./fire_grdtruths/s2_flameB.jpg
s3:
	$(COMPILER) fire.py YCC $(THRESH) ./fire_grdtruths/s3.jpg ./output/output_s3.jpg $(SAMPLE) ./fire_grdtruths/s3_flameB.jpg
s4:
	$(COMPILER) fire.py YCC $(THRESH) ./fire_grdtruths/s4.jpg ./output/output_s4.jpg $(SAMPLE) ./fire_grdtruths/s4_flameB.jpg

# OPENS GROUND TRUTH TESTING FILES FOR ANALYSIS
stopen: open1 open2 open3 open4 open5 open6 open7 open8

open1:
	$(OPEN) ./output/output_c1.jpg
open2:
	$(OPEN) ./output/output_c2.jpg
open3:
	$(OPEN) ./output/output_c3.jpg
open4:
	$(OPEN) ./output/output_c4.jpg
open5:
	$(OPEN) ./output/output_s1.jpg
open6:
	$(OPEN) ./output/output_s2.jpg
open7:
	$(OPEN) ./output/output_s3.jpg
open8:
	$(OPEN) ./output/output_s4.jpg

# FALSE POSITIVE TESTING
fptests: fp1 fp2 fp3 fp4 fp5 fp6

fp1:
	$(COMPILER) fire.py YCC $(THRESH) ./falsePositives/fp-1.jpg ./output/fp_output/output_fp-1.jpg $(SAMPLE)
fp2:
	$(COMPILER) fire.py YCC $(THRESH) ./falsePositives/fp-2.jpg ./output/fp_output/output_fp-2.jpg $(SAMPLE)
fp3:
	$(COMPILER) fire.py YCC $(THRESH) ./falsePositives/fp-3.jpg ./output/fp_output/output_fp-3.jpg $(SAMPLE)
fp4:
	$(COMPILER) fire.py YCC $(THRESH) ./falsePositives/fp-4.jpg ./output/fp_output/output_fp-4.jpg $(SAMPLE)
fp5:
	$(COMPILER) fire.py YCC $(THRESH) ./falsePositives/fp-5.jpg ./output/fp_output/output_fp-5.jpg $(SAMPLE)
fp6:
	$(COMPILER) fire.py YCC $(THRESH) ./falsePositives/fp-6.jpg ./output/fp_output/output_fp-6.jpg $(SAMPLE)

# OPENS 
fpopen: fpopen1 fpopen2 fpopen3 fpopen4 fpopen5 fpopen6

fpopen1:
	$(OPEN) ./output/fp_output/output_fp-1.jpg
fpopen2:
	$(OPEN) ./output/fp_output/output_fp-2.jpg
fpopen3:
	$(OPEN) ./output/fp_output/output_fp-3.jpg
fpopen4:
	$(OPEN) ./output/fp_output/output_fp-4.jpg
fpopen5:
	$(OPEN) ./output/fp_output/output_fp-5.jpg
fpopen6:
	$(OPEN) ./output/fp_output/output_fp-6.jpg

chtests: ch1 ch2 ch3 ch4


ch1:
	$(COMPILER) fire.py YCC $(THRESH) ./challenging/ch-fire-1.jpg ./output/ch_output/output_ch-1.jpg $(SAMPLE)
ch2:
	$(COMPILER) fire.py YCC $(THRESH) ./challenging/ch-fire-2.jpg ./output/ch_output/output_ch-2.jpg $(SAMPLE)
ch3:
	$(COMPILER) fire.py YCC $(THRESH) ./challenging/ch-fire-3.jpg ./output/ch_output/output_ch-3.jpg $(SAMPLE)
ch4:
	$(COMPILER) fire.py YCC $(THRESH) ./challenging/ch-fire-4.jpg ./output/ch_output/output_ch-4.jpg $(SAMPLE)

chopen: chopen1 chopen2 chopen3 chopen4

chopen1:
	$(OPEN) ./output/ch_output/output_ch-1.jpg
chopen2:
	$(OPEN) ./output/ch_output/output_ch-2.jpg
chopen3:
	$(OPEN) ./output/ch_output/output_ch-3.jpg
chopen4:
	$(OPEN) ./output/ch_output/output_ch-4.jpg

clean:
	rm ./output/*.jpg ./output/fp_output/*.jpg ./output/ch_output/*.jpg