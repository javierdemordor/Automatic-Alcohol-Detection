#!/bin/bash

for dir in /home/javier/Documents/Aalto/ASR/Project/ALC/*;
do
	cd '/home/javier/Documents/Aalto/ASR/Project/ALC'
	cd $dir

	mkdir /home/javier/Documents/Aalto/ASR/Project/Features/${dir}
	for file in *.wav;
	do
		/home/javier/Documents/Aalto/ASR/opensmile-3.0-linux-x64/bin/SMILExtract -C /home/javier/Documents/Aalto/ASR/opensmile-3.0-linux-x64/config/is09-13/IS11_speaker_state.conf -I ${file} -O /home/javier/Documents/Aalto/ASR/Project/Features/${file}.arff

	done
done

