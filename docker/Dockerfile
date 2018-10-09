FROM python:2-stretch
MAINTAINER Jacopo Mauro

RUN apt-get update && \
    apt-get install -y \
        time \
        openjdk-8-jdk-headless \
        libgl1 && \
    rm -rf /var/lib/apt/lists/* && \
    pip install \
        antlr4-python2-runtime \
        toposort \
        psutil \
        click

# download and install zephyrus with all its solvers
# see Zephyrus Docker file for more info
#COPY --from=jacopomauro/zephyrus2 /tool /tool
COPY --from=jacopomauro/zephyrus2:v2.0.1 /tool/ /tool/
# minizinc
ENV PATH "$PATH:/tool/MiniZincIDE/bin"
ENV LD_LIBRARY_PATH "$LD_LIBRARY_PATH:/tool/MiniZincIDE/lib"
# z3 solver
ENV PYTHONPATH "$PYTHONPATH:/tool/z3/install/lib/python-2/site-packages"
ENV PATH "$PATH:/tool/z3/install/bin"
# fzn2smt
ENV CLASSPATH "$CLASSPATH:/tool/fzn2smt:/tool/fzn2smt/antlr-runtime-3.2.jar"
# or-tools
ENV PATH "$PATH:/tool/or-tools/bin"
RUN ln -s /tool/or-tools/ortools/flatzinc/mznlib_sat /tool/MiniZincIDE/share/minizinc/or-tools && \
    # zephryus
    pip install -e /tool/zephyrus2

# install abs-tools
COPY --from=abslang/collaboratory:1.5.6 usr/local/lib/frontend/dist/absfrontend.jar /tool/abstools/absfrontend.jar
ENV CLASSPATH=/tool/abstools/absfrontend.jar:$CLASSPATH

# clone abs_deployer
RUN cd /tool && \
	git clone --recursive --depth=1 https://github.com/jacopoMauro/abs_deployer.git
ENV PATH /tool/abs_deployer:$PATH


WORKDIR /tool/abs_deployer
CMD ["/bin/bash"]

