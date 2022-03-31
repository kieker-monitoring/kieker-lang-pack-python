## Prerequisites
1. python3, pip
2. Java Collector executable 
3. Clone [this](https://github.com/silvergl/spyder) repository, which contains the implementation of Spyder5.
4. Linux (Other OS can be used too. Contribute your instructions in that case).
5. Install `netcat`. (In Ubuntu run `sudo apt update; sudo apt install netcat`.)
##Setup
1. Install [Anaconda](https://www.anaconda.com/products/individual#linux). Consult Anaconda documentation if some instalation steps are unclear.
2. Create new Anaconda environment `conda create --name some_good_name python=3.6`. Minimal Python version is 3.6.
3. Activate the environment you have just created `conda activate some_good_name`.
4. run `python3 -m pip install --upgrade build`.
5. `cd` to the spyder5 directory. 
6. run `conda install -c conda-forge --file requirements/conda.txt` if you are using linux. If you are using macOS run `conda install python.app`.
7. `cd` to the  location  of `kieker-lang-pack-python` directory.
8. adjust the contents of `build.sh` accordingly to the locations of  `spyder, Java Collector, and kieker-lang-pack-python` on your pc
9. Run `build.sh`. To test whether kieker establishes a connection to a server pass `-nc` as an argument. If you want to test your implementation with the Java Collector use `kieker` option.

