# 🍳🍳🍳choline🍳🍳🍳

A ml library thingy 
If u have ideas, feel free to make pull requests. 
my email is byyoung3@gmail.com if u want to chat




SETUP (mac/linux only!!!)

- Setup vastai account w payment info and setup your ssh-keygen on your local system.. see https://vast.ai/docs/gpu-instances/ssh
- clone the repo, and run the command 'python launch.py llama2code' then follow the instructions given in the command line 
-----> note WE FIND YOU THE BEST DEAL ON A 3090 WITH 120GB OF STORAGE ASSUMED FOR 3HRS AND 1GB UPLOADED AND 120GB DOWNLOADED!
- wait for the instance to set up. You can run 'python status.py' to monitor startup 
- 









ROADMAP 


THE THINGS I REALLY WANT ARE .... 

0) an easy way to launch open source LLM's on vast ai 

1) a cli that will let me specify when a vast instance will startup, as well as what data it will sync - without writing any sh scripts or installing any linux packages 
2) a python library that will sync my models, and code with the vast instance, and startup and resume a training run when/if the vast instance fails (on another instance) 
3) the library will also let me pause runs and effortlessly resume them, without any programatic code changes, as well as schedule pauses with shutdowns  
4) alerts for various events that occur on training run (accuracy accomplishments and failures), to my email 
