FROM python:2-onbuild
MAINTAINER Jacopo Mauro

# install packages 
RUN apt-get update && \
  apt-get install -y openjdk-7-jdk ant && \
  rm -rf /var/lib/apt/lists/* && \
	# install abs-tools
	cd / && \
	git clone --depth=1 https://github.com/abstools/abstools.git && \
  cd abstools/frontend && ant && \
	# retreive the abs_deployer tool
  cd / && \
	git clone --depth=1 https://github.com/jacopoMauro/abs_deployer.git && \
	# install minizinc suite 1.6 from binaries
	# note that zephyrus does not work with the 2.0 minizinc suite
	cd / && \
	wget http://www.minizinc.org/downloads/release-1.6/minizinc-1.6-x86_64-unknown-linux-gnu.tar.gz && \
  tar -zxvf minizinc-1.6-x86_64-unknown-linux-gnu.tar.gz && \
  rm -rf minizinc-1.6-x86_64-unknown-linux-gnu.tar.gz && \
  cd /minizinc-1.6 && \
  ./SETUP
	

ENV PATH /abs_deployer:$PATH
ENV PATH /abs_deployer/docker:$PATH
ENV PATH /minizinc-1.6/bin:$PATH
ENV CLASSPATH=/abstools/frontend/dist/absfrontend.jar

WORKDIR /abs_deployer


