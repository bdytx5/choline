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



best to read txt's in order of [idk, gameplan, envstuff] 

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
