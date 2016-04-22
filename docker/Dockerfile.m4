FROM python:2-onbuild
MAINTAINER Jacopo Mauro

# download and install zephyurs2
RUN cd / && \
	mkdir solvers_exec && \
  cd /solvers_exec && \
  git clone --depth=1 https://jacopomauro@bitbucket.org/jacopomauro/zephyrus2.git && \
  pip install -e /solvers_exec/zephyrus2

# MiniSearch need to be installed before MiniZincIde
include(`MiniSearch_binary.m4')
include(`MiniZincIDE_binary.m4')
include(`ortools_binary.m4')
include(`gecode_binary.m4')
include(`fzn2smt.m4')
include(`chuffed.m4')
include(`z3.m4')

# clone abs_deployer
RUN cd /solvers_exec && \
	git clone --depth=1 -b smart_deployer https://github.com/jacopoMauro/abs_deployer.git

ENV PATH /solvers_exec/abs_deployer:$PATH

# install abs-tools
RUN cd /solvers_exec && \
	apt-get update && \
  apt-get install -y \
		openjdk-7-jdk \
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


