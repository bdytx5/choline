# 🍳🍳🍳choline🍳🍳🍳

The cheapest and easiest way to do ML in the cloud 

we must simplify 

If u have ideas, feel free to make pull requests. 

my email is byyoung3@gmail.com if u want to chat


choline.pro

<insert motivational quote about startups that won't actually help>  

THE THINGS I REALLY WANT ARE .... 
1) a cli that will let me specify when a vast instance will startup, as well as what data it will sync - without writing any sh scripts or installing any linux packages 
2) a python library that will sync my models, and code with the vast instance, and startup and resume a training run when/if the vast instance fails (on another instance) 
3) the library will also let me pause runs and effortlessly resume them, without any programatic code changes, as well as schedule pauses with shutdowns  
4) alerts for various events that occur on training run (accuracy accomplishments and failures), to my email 


Currently, the main goal is to automate a lot of the processes of training models, as well as ease the process of using p2p GPU's on vast.ai 
The plan may change, but currently this project is focused on building a simple wrapper around ML frameworks, and building a backend that can utilize this wrapper to automate training on vast.ai, as well as make improvements on top of the exisitng Exisiting ML libraries. 


The way i see it, serverless is too restrictive, yet pure "serverful" is overkill. The goal is to make a hybrid


Right now, I'm building out the bare bones v1 version that will run on my personal machine. If i it, then I will scale it so everyone can use it. 
If you have a linux machine running 24/7, you will be able to run choline v1. 


best to read txt's in order of [idk, gameplan, envstuff] 




Core functions (subject to change) 
- Allows for single command that uploads all data to a remote vast instance and starts the training script for you automatically
- ability to schedule the above 
- If using the Choline wrapper, it will automatically store models that have been pretrained, along with your script information to a frontend 
- Ability to pause runs and resume via the font end 
- Automatic run restart and new instance creation as a result of failed runs 
- Automatic shutdown of instances at the end of runs 
- Integration with other cloud providers for easy access 
- AI monitoring of runs that communicates with you about possible shutdowns, and maybe even pauses if it suspects poor performance 
- Automatic batch size selection 
- Ability to extend epochs via front end 
- Ability to change learning rate via front end, mid run 
- Potentially supporting a web version of tensor board
- potentially a web based code editor on the front end to make quick changes 


How to contribute

- im in the process of figuring out how to make the wrapper work for 
torch/tf/keras(new keras which i believe uses native tf and torch). so ideas are welcome - the goal is to make it ridiculously simple, yet easily exapandable for power users 
- if you have unrelated ideas, feel free to put them in rambling/ideas_thoughts.txt -- just add ur username next to the date 
- if you are good at backend stuff, I'm working on a architecture for that... 
--> its to manage the users files at a intermediary location to handle vast failures 
----> basically right now its a flask server that recieves an initial call to 
----> reserve storage somewhere (right now local host) and returns the path name 
----> to upload the users scripts/data to, and also starts a listener at that location
----> after that, the listener at the returned location relays the files to the vast ai instance 
----> once it has started up 




t0d0 
CLIENT -- Need to make a custom command that will rent out a GPU and set up an evironment similar to the users
- ~~figure out how to use vast command line tools and make a short doc on that~~
- ----> https://cloud.vast.ai/cli/ (its pretty good)
- ------> see vast folder 
- ~~figure out how to create a docker container reliably from a script that runs on the users local machine~~
- ~~build machine provisioner that finds a machine for the user and starts it up (also sending docker info)~~ - i guess use vast.ai - (need to test)
- build flask api client call that requests storage, and then sends relevant files 

BACKEND -- Need a backend that can handle temporary storage of a users data 
- build flask backend that can recieve requests and provision storage locations and startup a listener that will transfer files to the GPU VM async 
- build server functionality that automatically syncs models to some other location in between epochs
- build fail detection and rollover system that syncs progress with previous run 

DEEP LEARNING LIBRARY ADDONS -- need integrations with popular deep learning frameworks to sync runs with a database 
- build torch model wrappers (unless other solution is found) that automates model saving
- possibly build wrapper for torch dataset that solved discussed dataset paths that reside outside of the project
- build website, payment console, and CLI login / account infrastructure 

FRONTEND - allows for monitoring different runs
- TODO 
