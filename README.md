# blendersetup
Scripts &amp; env to setup blender on cloud VM

# On Google Drive

[My Colab](https://colab.research.google.com)



# Rendering a test frame from within a docker container

To quickly render a single test frame using the Cycles ray tracer you can run the following command

https://github.com/nytimes/rd-blender-docker/wiki/Getting-started

```
docker run nytimes/blender:latest blender -b -o /tmp/ -E CYCLES -f 1
```
In this example:
```
-b means run Blender in background mode (i.e headless with no GUI)
-o refers to the folder in which you want to save the renders
-E selects the engine used for rendering (Cycles support both GPU and CPU rendering)
-f sets the amount of frames to render
```
Using the images in your own Dockerfile

It should look like something like

```
FROM nytimes/blender:latest

...rest of your own Dockerfile
```
For all tags available see Docker tags or visit the Docker Hub repository
