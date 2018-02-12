wdir=`pwd`;
cd ~/AnacondaProjects\
  && conda build purge\
  && conda build coords\
  && conda uninstall -y coords;
conda install -y -c malcolmw coords;
cd $wdir;
