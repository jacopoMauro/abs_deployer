FROM python:2-onbuild
MAINTAINER Jacopo Mauro

RUN \
	###############
	# install needed packages
	###############  
	apt-get update && \
  apt-get install -y openjdk-7-jdk ant cmake bison flex  && \
  rm -rf /var/lib/apt/lists/* && \
	###############
	# install abs-tools
	###############
	cd / && \
	git clone --depth=1 https://github.com/abstools/abstools.git && \
  cd abstools/frontend && ant && \
	###############
	# retreive the abs_deployer tool
	###############
  cd / && \
	git clone --depth=1 -b smart_deployer https://github.com/jacopoMauro/abs_deployer.git && \
	###############
	# compile gecode
	###############
	cd / && \
  wget http://www.gecode.org/download/gecode-4.4.0.tar.gz && \
  tar -zxvf gecode-4.4.0.tar.gz && \
  cd gecode-4.4.0 && \
  ./configure --disable-examples --prefix=/gecode-4.4.0 && \
  make && make install && \
  rm -rf /gecode-4.4.0.tar.gz && \
	###############
	# download minisearch binary
	###############
	cd / && \
  wget http://www.minizinc.org/minisearch/minisearch-0.1.0b1-Linux64.tar.gz && \
  tar -zxvf minisearch-0.1.0b1-Linux64.tar.gz && \
  rm -rf minisearch-0.1.0b1-Linux64.tar.gz && \
	###############
	cd / && \
  git clone --depth=1 https://jacopomauro@bitbucket.org/jacopomauro/zephyrus2.git && \
	pip install -e /zephyrus2
	
	

ENV PATH /abs_deployer:$PATH
ENV PATH /minisearch-0.1.0b1-Linux/bin:$PATH
ENV CLASSPATH=/abstools/frontend/dist/absfrontend.jar
# update variables for gecode
ENV PATH /gecode-4.4.0/bin:$PATH
ENV LD_LIBRARY_PATH=/gecode-4.4.0/lib:$LD_LIBRARY_PATH

WORKDIR /abs_deployer
