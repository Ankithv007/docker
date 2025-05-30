# Docker Model Runner (https://docs.docker.com/model-runner/)
Docker Model Runner is a Docker container that is used to run (or serve) a machine learning model.

### Why is it called a “Model Runner”?
`
Because its job is to run the model and return predictions.

“Model” = your trained ML model (e.g., a .pkl or .pt file)

“Runner” = the part that runs the model inside a Docker container

It’s like a “mini server” for predictions.
`
## as of now we need  docker desktop (Docker Desktop 4.40 or later) to use the docker model runner (30/05/2025)
```bash
 - docker model

1. Ensure you have installed Docker Engine.
2. DMR is available as a package. To install it, run:
 -  apt install docker-model-plugin

Model runner status : Check whether the Docker Model Runner is active and displays the current inference engine
  -  docker model status
```

## Pull a model
 - https://hub.docker.com/u/ai    (pull the docker model which ever you want)
```bash
- Pulls a model from Docker Hub to your local environment.
 -  docker model pull <model>
 -  docker model pull ai/smollm2

For List avilable
 -  docker model list
```
## Run a model
Run a model and interact with it using a submitted prompt or in chat mode. When you run a model, Docker calls an Inference Server API endpoint hosted by the Model Runner through Docker Desktop. The model stays in memory until another model is requested, or until a pre-defined inactivity timeout is reached
```bash
One-time prompt
 -  docker model run ai/smollm2 "Hi"

Interactive chat
 -  docker model run ai/smollm2 
```
##  Remove a model
 Removes a downloaded model from your system.
 ```bash
  - docker model rm <model>

```
## to run docker model in your localhost 
```bash
Integrate the Docker Model Runner into your software development lifecycle
You can now start building your Generative AI application powered by the Docker Model Runner.

If you want to try an existing GenAI application, follow these instructions.

1.Set up the sample app. Clone and run the following repository:


 git clone https://github.com/docker/hello-genai.git
2.In your terminal, navigate to the hello-genai directory.

3.Run run.sh for pulling the chosen model and run the app(s): (./run.sh)

4.Open you app in the browser at the addresses specified in the repository README.

You'll see the GenAI app's interface where you can start typing your prompts.

```
