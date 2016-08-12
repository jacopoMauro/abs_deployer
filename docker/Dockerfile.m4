FROM python:2-onbuild
MAINTAINER Jacopo Mauro

# download and install zephyurs2
RUN cd / && \
	mkdir solvers_exec && \
  cd /solvers_exec && \
  git clone --recursive -b bind_preferences https://jacopomauro@bitbucket.org/jacopomauro/zephyrus2.git && \
	cd zephyrus2 && \
	git checkout 924b50f04c73b8269d3b14157dd0abbf7b5bd99c && \ 
	#check out tested version with smartdeployer
  pip install -e /solvers_exec/zephyrus2

include(`MiniZincIDE_binary.m4')
include(`gecode_binary.m4')
include(`chuffed.m4')

# clone abs_deployer
RUN cd /solvers_exec && \
	git clone --recursive --depth=1 -b bind_pref https://github.com/jacopoMauro/abs_deployer.git

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


