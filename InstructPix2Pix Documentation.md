## 1. Requirements:
- Anaconda
- Python
- Git

## 2. Setup:
In the Anaconda Terminal enter following commands:
	``conda env create -f environment.yaml
Sets up a new Conda environment with the required modules

	conda activate ip2p
Activates the environment **-> Needs to be entered every time you want to use the program!

	bash scripts/download_checkpoints.sh
Downloads the pretrained AI (~70-100GB)

## 3. Running the program:
1. Open Anaconda Terminal
2. Enter ``conda activate ip2p
3.Change into the ``C:\Users\K017-Labor\Documents\Pix2Pix\instruct-pix2pix`` folder and enter ``python edit_app.py ``for the browser application (http://127.0.0.1:7860/ / train.yaml for memory error) -> Needs an internet connection!
4. Alternatively use ```
python edit_cli.py --input imgs/example.jpg --output imgs/output.jpg --edit "instruction"
###### Optionally, you can specify parameters to tune your result:
``python edit_cli.py --steps 100 --resolution 512 --seed 1371 --cfg-text 7.5 --cfg-image 1.2 --input imgs/example.jpg --output imgs/output.jpg --edit "turn him into a cyborg"

## 4. Workflow
1. Take image with webcam (Res: 1080x1920)
2. Rescale to smaller size (Res: 470x820) ``magick a.jpg -resize 470x820 d.jpg
3. Input the image into ip2p edit app
4. Save the best result 
5. Upscale with magick a.jpg -resize 1080x1920 e.jpg
6. Add QR-Code ``magick a.jpg b.png -gravity southwest -geometry +10+10 -composite c.jpg
7. Print with Selphy Printer
8. -> Rahmen


   
