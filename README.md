# Description 

AI Controls music player with signs. Simple console application with TensorFlow and Python. Using RetinaNet50 as base, pre-trained model.  

# Instructions

The script's looking for 'songs' folder in the same dir as the main. Signs it recognizes and following actions:


Start Player            |  Stop Player | Next Song | Previous Song
:-------------------------:|:-------------------------: |:------------------------- |:------------------------- 
![start](https://i.ibb.co/bHHsgK9/Capture.png)   |  ![stop](https://i.ibb.co/Mn7Zpbb/Capture.png) | ![next](https://i.ibb.co/ggNjDtP/Capture2.png) |   ![back](https://i.ibb.co/jMv80Vy/Capture3.png):
   

# How to run it

Windows executable [here](https://drive.google.com/drive/folders/1ctF42o-dkr8gw6e0BR1HRfqkagWLzSwn?usp=sharing). 

Steps to run the project locally:

1. Create and activate new python virtual environment

2. Run "pip install -r requirements.txt" 

3. Download the Tensorflow 'exported-models' folder in the dir of the main. You can find it on the Windows Exe link above.

4. Run "python -m main"
