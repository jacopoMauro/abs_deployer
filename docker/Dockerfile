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

###############
# download MiniZincIDE-2.0.13-bundle-linux-x86_64.tgz and untar
###############
RUN ( [ -d /solvers_exec ] || mkdir /solvers_exec ) && \
	cd /solvers_exec && \
	wget https://github.com/MiniZinc/MiniZincIDE/releases/download/2.0.13/MiniZincIDE-2.0.13-bundle-linux-x86_64.tgz && \
	tar -zxvf MiniZincIDE-2.0.13-bundle-linux-x86_64.tgz && \
	mv /solvers_exec/MiniZincIDE-2.0.13-bundle-linux-x86_64 /solvers_exec/MiniZincIDE && \
	rm -rf MiniZincIDE-2.0.13-bundle-linux-x86_64.tgz

ENV PATH /solvers_exec/MiniZincIDE:$PATH

	###############
	# compile gecode (non needed - comes with the binaries of the last minizincIDE)
	###############
	#cd /solvers_exec && \
  #wget http://www.gecode.org/download/gecode-4.4.0.tar.gz && \
  #tar -zxvf gecode-4.4.0.tar.gz && \
  #rm -rf /solvers_exec/gecode-4.4.0.tar.gz && \
  #cd gecode-4.4.0 && \
  #./configure --disable-examples --prefix=/solvers_exec/gecode-4.4.0 && \
  #make && make install && \
  ###############
  # add gecode global def to minizinc
  ###############
  # minisearch has already its gecode global definitions
  #ln -s gecode/flatzinc/mznlib /solvers_exec/MiniZincIDE-2.0.13-bundle-linux-x86_64/share/minizinc/gecode
# ENV PATH /solvers_exec/gecode-4.4.0/bin:$PATH
# ENV LD_LIBRARY_PATH=/solvers_exec/gecode-4.4.0/lib:$LD_LIBRARY_PATH

RUN ( [ -d /solvers_exec ] || mkdir /solvers_exec ) && \
	###############
	# install needed packages
	###############  
	apt-get update && \
	apt-get install -y \
		qt5-default && \
	rm -rf /var/lib/apt/lists/* && \
	[ -d /solvers_exec/minisearch ] && \
  ln -s /solvers_exec/minisearch/share/minizinc/gecode /solvers_exec/MiniZincIDE/share/minizinc/gecode || \
	echo "Minisearch not detected. Continuing"




###############
# download chuffed, add global-dir in minizinc
###############

COPY ./docker_scripts/fzn-chuffed /bin/fzn-chuffed

RUN ( [ -d /solvers_exec ] || mkdir /solvers_exec ) && \
	cd /solvers_exec && \
  git clone --depth=1 https://github.com/geoffchu/chuffed.git && \
  chmod 755 /bin/fzn-chuffed && \ 
	chmod 755 /solvers_exec/chuffed/binary/linux/fzn_chuffed && \
  ( [ -d /solvers_exec/MiniZincIDE ] && \
	  ln -s /solvers_exec/chuffed/binary/linux/mznlib /solvers_exec/MiniZincIDE/share/minizinc/chuffed || \
		echo MiniZincIde not installed ) && \
  ( [ -d /solvers_exec/minisearch ] && \
	ln -s /solvers_exec/chuffed/binary/linux/mznlib /solvers_exec/minisearch/share/minizinc/chuffed || \
		echo MiniSearch not installed )


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


