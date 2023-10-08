# 🍳🍳🍳choline🍳🍳🍳
![Choline_cation](https://github.com/bdytx5/choline/assets/32812705/f4805d1d-c06e-4c44-a0fc-4b8433387911)

A ml library thingy 

now on pypi! ==> pip install choline


### choline code
Launches a specified instance in Visual Studio Code. This command allows you to open and work on your project in a remote environment via VS Code.

### choline status
Runs the status command, fetching and displaying the current status of your machine or process. Use this to get real-time updates on your tasks.

### choline init
Enables the creation of a `choline.yaml` configuration file. This will typically include settings for hardware, disk space, and other environment parameters.

### choline stream
Streams data or logs to the console, providing real-time insights into your running tasks. Useful for monitoring progress.

### choline kill
Terminates the local setup of the machine. This command does not affect the remote machine but rather stops the local tasks and processes related to it.

### choline launch
Launches a new instance or task. Note that this command must be run as root.

### choline sync
Syncs your local machine with the remote machine, usually transferring files and data. Use this to keep everything up-to-date.




If u have ideas, feel free to make pull requests.     
     
my email is byyoung3@gmail.com if u want to chat


SETUP (mac/linux only!!!)

- Setup vastai account w payment info and setup your ssh-keygen on your local system.. see https://vast.ai/docs/gpu-instances/ssh
- clone the repo, go to the launch dir, and run the command 'python launch.py launch llama2code' then follow the instructions given in the command line 
-----> note WE FIND YOU THE BEST DEAL ON A 3090 WITH 120GB OF STORAGE ASSUMED FOR 3HRS AND 1GB UPLOADED AND 120GB DOWNLOADED!
- wait for the instance to set up. You can run 'python status.py' to monitor startup 
- after the server api is running, run app.py 



ROADMAP 


THE THINGS I REALLY WANT ARE .... 

0) an easy way to launch open source LLM's on vast ai  ~~codellama~~

0.3) an easy way to duplicate ur local env/data onto a vastai instance

0.5) an easy way to fine tune open source LLM's 

0.7) fault tollerant training 

1) a cli that will let me specify when a vast instance will startup, as well as what data it will sync - without writing any sh scripts or installing any linux packages 

2) a python library that will sync my models, and code with the vast instance, and startup and resume a training run when/if the vast instance fails (on another instance) 

3) the library will also let me pause runs and effortlessly resume them, without any programatic code changes, as well as schedule pauses with shutdowns  
4) alerts for various events that occur on training run (accuracy accomplishments and failures), to my email 
