FROM python:2-stretch
MAINTAINER Jacopo Mauro

# download and install zephyurs2
RUN cd / && \
    mkdir solvers_exec && \
    cd /solvers_exec && \
    git clone --recursive --depth=1 https://jacopomauro@bitbucket.org/jacopomauro/zephyrus2.git && \
    cd zephyrus2 && \
    pip install -e /solvers_exec/zephyrus2 && \
    pip install antlr4-python2-runtime toposort psutil click && \
    apt-get update && \
    apt-get install -y \
        time \
        flex \
		bison \
		nano \
		libqt5core5a \
        libqt5gui5 \
        libqt5network5 \
        libqt5webkit5 \
        libqt5widgets5 && \
    rm -rf /var/lib/apt/lists/*


# Install minizinc suite
RUN cd / && \
  wget https://github.com/MiniZinc/MiniZincIDE/releases/download/2.1.7/MiniZincIDE-2.1.7-bundle-linux-x86_64.tgz && \
  tar -zxvf MiniZincIDE-2.1.7-bundle-linux-x86_64.tgz && \
  rm -rf MiniZincIDE-2.1.7-bundle-linux-x86_64.tgz && \
	mv MiniZincIDE-2.1.7-bundle-linux-x86_64 minizinc
ENV PATH /minizinc:$PATH


  ###############
  # download fzn2smt
  ###############

COPY ./docker_scripts/antlr-runtime-3.2.jar /antlr-runtime-3.2.jar

RUN apt-get update && \
	# openjdk and unzip for the fzn2smt	
	apt-get install -y \
		unzip \
		openjdk-8-jdk && \
	rm -rf /var/lib/apt/lists/* && \
  cd /solvers_exec && \
  wget http://ima.udg.edu/recerca/lap/fzn2smt/version/fzn2smt-2-0-02.zip && \
  unzip fzn2smt-2-0-02.zip && \
  rm -rf fzn2smt-2-0-02.zip

ENV CLASSPATH=/solvers_exec/fzn2smt-2-0-02:/antlr-runtime-3.2.jar:$CLASSPATH


###############
# download and compile z3
###############
RUN cd /solvers_exec && \
	###############
	# install z3
	###############
	git clone --depth 1 https://github.com/Z3Prover/z3.git && \
	cd z3 && \
	python scripts/mk_make.py --python && \
	cd build
	make && \
	make install


# clone abs_deployer
RUN cd /solvers_exec && \
	git clone --recursive --depth=1 https://github.com/jacopoMauro/abs_deployer.git
ENV PATH /solvers_exec/abs_deployer:$PATH

# install abs-tools
RUN cd /solvers_exec && \
	apt-get update && \
    apt-get install -y \
		openjdk-8-jdk \
		ant \
		cmake \
		bison \
		flex && \
    rm -rf /var/lib/apt/lists/* && \
	cd /solvers_exec && \
	git clone --depth=1 https://github.com/abstools/abstools.git && \
    cd /solvers_exec/abstools/frontend && ant

ENV CLASSPATH=/solvers_exec/abstools/frontend/dist/absfrontend.jar:$CLASSPATH
	
WORKDIR /solvers_exec/abs_deployer
CMD ["/bin/bash"]

