# How to Create and Use the Playground Container in Linux Environment

This guide provides instructions on how to build and run a Singularity container using the `playground.def` definition file. This container includes an Apache Jena Fuseki server configured with Java 22, equipped with Jupyter Notebook and Firefox.

## Prerequisites
 - Singularity is installed on the host computer - follow instructions from [here](https://docs.sylabs.io/guides/latest/user-guide/)
 - You have access to a `playground.def` file (included in this repository [here](./playground.def))
 - Basic familiarity with linux command-line tools.

## Building the Container

Detailed information about building containers using Singularity can be found [here](https://docs.sylabs.io/guides/latest/user-guide/build_a_container.html).

### CLI Quick Reference

```
  # sudo singularity build playground.sif playground.def
  # mkdir playground_local_files
  # singularity run --bind playground_local_files:/persistent playground.sif 
```

### Guide and Explanation

To build a Singularity container from the `playground.def` file provided in this repo, follow these steps:

1. Navigate to your home directory on your computer.
2. Use the following command to create and enter the necessary definition file for singularity to build an image.
   ```
   vim playground.def
   ```
   - **Note**: Use your preferred text editor. VIM is not required.
3. Copy and paste the contents of `playground.def` from this repo into the local copy of `playground.def` you just created and are currently editing. Save the file and quit, returning to the CLI.
   - Visit this [link](https://docs.sylabs.io/guides/latest/user-guide/definition_files.html) for more information on definition files.
4. Use the following command to build the container.
   ```
   sudo singularity build playground.sif playground.def
   ```
   - **Note**: This process can take up to several minutes to complete.
5. If you dont have a directory for the playground container local files (eg. Running it for the very first time), create a new directory using the following command.
   ```
   # mkdir <directory_name> --> Creates a directory
   mkdir playground_local_files
   ```
6. To run the container use the following command. This "allows you to run your container and run the specific features of it."
   ```
   singularity run --bind playground_local_files:/persistent playground.sif 
   ```
   
   #### Start and stop the Zena Fuseki server
7. Handle the server using the start and stop options (Option 1 & 2).

### Starting the Server

**Note:** If using a specific port for your jena fuseki server use the command in step 10.

8. While running the container you can use [start option](#start-and-stop-the-server) to start up the apache-jena-fuseki server.
   - Additionally, you can use the curl command in the host computer, it will output information about the server in JSON format.
   ```
   curl -X GET http://localhost:3030/$/server
   ```
   - Another way to verify the server is to go to use the command `hostname -I` to see the host computer's IP address. In your browser, type in `http://ip-address-here:3030. The apache-jena-fuseki webpage should appear and can be interacted with.
   - **Note**: If two IP addresses appear, use the one on the right.

9. To stop the server, use the [stop option]((#start-and-stop-the-server)).

## Using Jupyter Notebook in a Singularity Container

1. Activate server hosting with Jupyter using option 3.
   - This will run the Jupyter server in the background on port 8888
2. Copy and paste the URL (`localhost:8888`) into your browser to gain access to jupyter notebooks features.

## Stopping Jupyter Notebooks Server

1. When you want to stop the server, use `Control + C` (or `Command + C` if you are in a Mac Environment) to prompt to stop the server and confirm stopping the server by pressing the `y` key.