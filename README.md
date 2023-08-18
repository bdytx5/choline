# 🍳🍳🍳choline🍳🍳🍳

The cheapest and easiest way to do ML in the cloud 

we must simplify 

If u have ideas, feel free to make pull requests. 

my email is byyoung3@gmail.com if u want to chat


choline.pro

<insert motivational quote about startups that won't actually help>  



Currently, the main goal is to automate a lot of the processes of training models, as well as ease the process of using p2p GPU's on vast.ai 
The plan may change, but currently this project is focused of building a simple wrapper around Torch, and building a backend that can utilize 
this wrapper to automate training on vast.ai, as well as make improvements on top of the exisitng Torch library. 

For right now, ChatGPT is my Head Business Strategist and Head Junior Programmer. GPT-5 will be interviewing for CTO ;) 

https://chat.openai.com/share/5250bfa3-3783-49ed-9b77-a71592cd3f73

best to read txt's in order of [idk, gameplan, envstuff] 

Core functions (subject to change) 
- Allows for single command that uploads all data to a remote vast instance and starts the training script for you automatically 
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

t0d0 
- ~~figure out how to use vast command line tools and make a short doc on that~~
- ----> https://cloud.vast.ai/cli/ (its pretty good)
- Need to make a custom command that will rent out a GPU and set up an evironment similar to the users
- ------> see vast folder 
- figure out how to create a docker container reliably from a script that runs on the users local machine
- build machine provisioner that finds a machine for the user and starts it up - i guess use vast.ai 
- build server functionality that automatically syncs models to some other location in between epochs
- build fail detection and rollover system that syncs progress with previous run 
- build torch model wrappers (unless other solution is found) that automates model saving
- possibly build wrapper for torch dataset that solved discussed dataset paths that reside outside of the project
- build website, payment console, and CLI login / account infrastructure 
