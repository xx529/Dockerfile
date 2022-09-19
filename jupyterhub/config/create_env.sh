# install miniconda
sh /miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"

# init conda env
./miniconda/bin/conda init
source ~/.bashrc

# create user env
conda create -n ${USER} python=3.8 -y
pip install ipykernel -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m ipykernel install --user --name=${USER} --display-name ${USER}