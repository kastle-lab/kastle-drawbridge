# How to Create and Use a Singularity Container With Apache-Jena-Fuseki in Linux Environment

This guide provides instructions on how to build and run a Singularity container using the `playground.def` definition file. This container includes an Apache Jena Fuseki server configured with Java 22, equipped with Jupyter Notebook and Firefox.

## Prerequisites
 - Singularity is installed on the host computer - follow instructions from [here](https://docs.sylabs.io/guides/latest/user-guide/)
 - You have access to a `playground.def` file (included in this repository [here](./playground.def))
 - Basic familiarity with linux command-line tools.

## Building the Container

Detailed information about building containers using Singularity can be found [here](https://docs.sylabs.io/guides/latest/user-guide/build_a_container.html).

### CLI Quick Reference

```
  # sudo singularity build --sandbox playground.sif playground.def
  # sudo singularity shell --writable playground.sif/
  # cd apache-jena-fuseki-5.0.0/run/
  # vim shiro.ini
      ## follow step 8
  # $JENA_HOME/fuseki start
  # $JENA_HOME/fuseki status
  # curl -X GET http://localhost:3030/$/server
  # $JENA_HOME/fuseki stop
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
   sudo singularity build --sandbox playground.sif playground.def
   ```
   - **Note**: This process can take up to several minutes to complete.
5. To enter the container use the follwing command. This "allows you to spawn a new shell within your container and interact with it as though it were a small virtual machine."
   ```
   sudo singularity shell --writable playground.sif
   ```
   - **Note**: One way to verify that you are inside a singularity container is by looking at the command prompt, which will display `Singularity>` or something similar to `root@DESKTOP-KE54U6:/usr/local/singularity#`.
   
   #### Start and stop the server
6. Start the server using the start command. This will create the /run directory and configuration files.
   ```
   <!-- Start Command -->
   $JENA_HOME/fuseki start


   <!-- Stop Command -->
   $JENA_HOME/fuseki stop
   ```
   - Use the stop to halt the server, before continuing.

### Configuring the Server

7. Navigate to the run folder inside the apache directory `cd /apache-jena-fuseki-5.0.0/run/`
8. Open the `shiro.ini` file
   - Comment out `/$/** = localhostFilter`
   - Where it says "allow any access" uncomment the line `/$/** = anon` and add the following: `/$/stats = anon` and `/$/stats/* = anon`
   - Save and exit file

### Starting the Server

**Note:** If using a specific port for your jena fuseki server use the command in step 10.

9. While inside the container you can use [start command](#start-and-stop-the-server) to start up the apache-jena-fuseki server.
   - To verify the server is running correctly, do the following:
   ```
   $JENA_HOME/fuseki status
   ```
    and the output should say if Fuseki is running and give its PID.
   - Additionally, you can use the curl command, it will output information about the server in JSON format.
   ```
   curl -X GET http://localhost:3030/$/server
   ```
   - Another way to verify the server is to go to use the command `hostname -I` to see the host computer's IP address. In your browser, type in `http://ip-address-here:3030. The apache-jena-fuseki webpage should appear and can be interacted with.
   - **Note**: If two IP addresses appear, use the one on the right.
10. If a specific port is required use the following command `java -Xmx1200M -jar fuseki-server.jar --port=8005`

- If using this method use `http://ip-address-here:PORT#`

11. To stop the server, use the [stop command]((#start-and-stop-the-server)).

## Using Jupyter Notebook in a Singularity Container

1. Navigate to the jupyter directory.
   ```
   cd /root/jupyter-notebooks
   ```
2. Activate server hosting with Jupyter
   ```
   jupyter notebook --no-browser --allow-root --port=5000 > jupyter.out 2> jupyter.err &
   ```
   - This will run the Jupyter server in the background on port 5000
3. To view the available URL's, use the command:
   ```
   jupyter notebook list
   ```
4. Copy and paste the URL from `:: /root/jupyter-notebooks` into your browser to gain access to jupyter notebooks features.

## Stopping Jupyter Notebooks Server

1. Use the command `ps` to display the processes that are currently running. Look for the PID next to "jupyter-notebook".
   ```
   ps
   ```
2. use the following command to terminate the server.
   ```
   kill <pid-here>
   ```
