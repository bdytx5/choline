#!/bin/bash
# Download Miniconda installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
# Install Miniconda
bash miniconda.sh -b -p $HOME/miniconda
# Initialize conda
source $HOME/miniconda/bin/activate
conda init
# Create environment
conda create --name myenv python=3.8.5 -y
# Activate environment
conda activate myenv
conda install absl-py==1.4.0 -y || pip install absl-py==1.4.0
conda install addict==2.4.0 -y || pip install addict==2.4.0
conda install aiofiles==23.1.0 -y || pip install aiofiles==23.1.0
conda install aiohttp==3.8.4 -y || pip install aiohttp==3.8.4
conda install aiosignal==1.2.0 -y || pip install aiosignal==1.2.0
conda install alabaster==0.7.12 -y || pip install alabaster==0.7.12
conda install albumentations==1.3.0 -y || pip install albumentations==1.3.0
conda install ale-py==0.7.3 -y || pip install ale-py==0.7.3
conda install altair==4.2.2 -y || pip install altair==4.2.2
conda install anaconda-client==1.7.2 -y || pip install anaconda-client==1.7.2
conda install anaconda-navigator==1.10.0 -y || pip install anaconda-navigator==1.10.0
conda install anaconda-project==0.8.3 -y || pip install anaconda-project==0.8.3
conda install antlr4-python3-runtime==4.9.3 -y || pip install antlr4-python3-runtime==4.9.3
conda install anyio==3.6.2 -y || pip install anyio==3.6.2
conda install apache-beam==2.34.0 -y || pip install apache-beam==2.34.0
conda install appdirs==1.4.4 -y || pip install appdirs==1.4.4
conda install area==1.1.1 -y || pip install area==1.1.1
conda install argcomplete==1.12.3 -y || pip install argcomplete==1.12.3
conda install argh==0.26.2 -y || pip install argh==0.26.2
conda install argon2-cffi @ file:///tmp/build/80754af9/argon2-cffi_1596828493937/work -y || pip install argon2-cffi @ file:///tmp/build/80754af9/argon2-cffi_1596828493937/work
conda install asn1crypto @ file:///tmp/build/80754af9/asn1crypto_1596577642040/work -y || pip install asn1crypto @ file:///tmp/build/80754af9/asn1crypto_1596577642040/work
conda install astroid @ file:///tmp/build/80754af9/astroid_1592495912941/work -y || pip install astroid @ file:///tmp/build/80754af9/astroid_1592495912941/work
conda install astropy==4.0.2 -y || pip install astropy==4.0.2
conda install astunparse==1.6.3 -y || pip install astunparse==1.6.3
conda install async-generator==1.10 -y || pip install async-generator==1.10
conda install async-timeout==4.0.2 -y || pip install async-timeout==4.0.2
conda install atomicwrites==1.4.0 -y || pip install atomicwrites==1.4.0
conda install attrdict==2.0.1 -y || pip install attrdict==2.0.1
conda install attrs @ file:///tmp/build/80754af9/attrs_1604765588209/work -y || pip install attrs @ file:///tmp/build/80754af9/attrs_1604765588209/work
conda install audioread==2.1.9 -y || pip install audioread==2.1.9
conda install autopep8 @ file:///tmp/build/80754af9/autopep8_1596578164842/work -y || pip install autopep8 @ file:///tmp/build/80754af9/autopep8_1596578164842/work
conda install AutoROM==0.4.2 -y || pip install AutoROM==0.4.2
conda install AutoROM.accept-rom-license==0.4.2 -y || pip install AutoROM.accept-rom-license==0.4.2
conda install avro-python3==1.9.2.1 -y || pip install avro-python3==1.9.2.1
conda install Babel==2.12.1 -y || pip install Babel==2.12.1
conda install backcall==0.2.0 -y || pip install backcall==0.2.0
conda install backports.functools-lru-cache==1.6.1 -y || pip install backports.functools-lru-cache==1.6.1
conda install backports.shutil-get-terminal-size==1.0.0 -y || pip install backports.shutil-get-terminal-size==1.0.0
conda install backports.tempfile==1.0 -y || pip install backports.tempfile==1.0
conda install backports.weakref==1.0.post1 -y || pip install backports.weakref==1.0.post1
conda install backports.zoneinfo==0.2.1 -y || pip install backports.zoneinfo==0.2.1
conda install bce-python-sdk==0.8.79 -y || pip install bce-python-sdk==0.8.79
conda install beautifulsoup4 @ file:///tmp/build/80754af9/beautifulsoup4_1601924105527/work -y || pip install beautifulsoup4 @ file:///tmp/build/80754af9/beautifulsoup4_1601924105527/work
conda install bitarray @ file:///tmp/build/80754af9/bitarray_1605065113847/work -y || pip install bitarray @ file:///tmp/build/80754af9/bitarray_1605065113847/work
conda install bkcharts==0.2 -y || pip install bkcharts==0.2
conda install black==23.1.0 -y || pip install black==23.1.0
conda install bleach @ file:///tmp/build/80754af9/bleach_1600439572647/work -y || pip install bleach @ file:///tmp/build/80754af9/bleach_1600439572647/work
conda install bokeh @ file:///tmp/build/80754af9/bokeh_1603297833684/work -y || pip install bokeh @ file:///tmp/build/80754af9/bokeh_1603297833684/work
conda install boto==2.49.0 -y || pip install boto==2.49.0
conda install boto3==1.20.6 -y || pip install boto3==1.20.6
conda install botocore==1.23.6 -y || pip install botocore==1.23.6
conda install Bottleneck==1.3.2 -y || pip install Bottleneck==1.3.2
conda install box2d-py==2.3.5 -y || pip install box2d-py==2.3.5
conda install Brotli==1.0.9 -y || pip install Brotli==1.0.9
conda install brotlipy==0.7.0 -y || pip install brotlipy==0.7.0
conda install bs4==0.0.1 -y || pip install bs4==0.0.1
conda install bsa==0.1.0 -y || pip install bsa==0.1.0
conda install cachetools==4.2.0 -y || pip install cachetools==4.2.0
conda install certifi==2021.10.8 -y || pip install certifi==2021.10.8
conda install cffi @ file:///tmp/build/80754af9/cffi_1600699146221/work -y || pip install cffi @ file:///tmp/build/80754af9/cffi_1600699146221/work
conda install chardet==4.0.0 -y || pip install chardet==4.0.0
conda install charset-normalizer==2.0.7 -y || pip install charset-normalizer==2.0.7
conda install # Editable install with no version control (choline==1.0) -y || pip install # Editable install with no version control (choline==1.0)
conda install -e /home/brett/choline/my_choline_project -y || pip install -e /home/brett/choline/my_choline_project
conda install clang==5.0 -y || pip install clang==5.0
conda install click==8.1.3 -y || pip install click==8.1.3
conda install cloudpickle @ file:///tmp/build/80754af9/cloudpickle_1598884132938/work -y || pip install cloudpickle @ file:///tmp/build/80754af9/cloudpickle_1598884132938/work
conda install clyent==1.2.2 -y || pip install clyent==1.2.2
conda install cmake==3.27.2 -y || pip install cmake==3.27.2
conda install colorama @ file:///tmp/build/80754af9/colorama_1603211150991/work -y || pip install colorama @ file:///tmp/build/80754af9/colorama_1603211150991/work
conda install commonmark==0.9.1 -y || pip install commonmark==0.9.1
conda install conda==4.11.0 -y || pip install conda==4.11.0
conda install conda-build==3.20.5 -y || pip install conda-build==3.20.5
conda install conda-package-handling @ file:///tmp/build/80754af9/conda-package-handling_1603018141399/work -y || pip install conda-package-handling @ file:///tmp/build/80754af9/conda-package-handling_1603018141399/work
conda install conda-verify==3.4.2 -y || pip install conda-verify==3.4.2
conda install contextlib2==0.6.0.post1 -y || pip install contextlib2==0.6.0.post1
conda install coremltools==5.2.0 -y || pip install coremltools==5.2.0
conda install crcmod==1.7 -y || pip install crcmod==1.7
conda install cryptography @ file:///tmp/build/80754af9/cryptography_1601046815590/work -y || pip install cryptography @ file:///tmp/build/80754af9/cryptography_1601046815590/work
conda install cssselect==1.2.0 -y || pip install cssselect==1.2.0
conda install cssutils==2.6.0 -y || pip install cssutils==2.6.0
conda install cycler==0.10.0 -y || pip install cycler==0.10.0
conda install Cython @ file:///tmp/build/80754af9/cython_1594831566883/work -y || pip install Cython @ file:///tmp/build/80754af9/cython_1594831566883/work
conda install cytoolz==0.11.0 -y || pip install cytoolz==0.11.0
conda install dask @ file:///tmp/build/80754af9/dask-core_1602083700509/work -y || pip install dask @ file:///tmp/build/80754af9/dask-core_1602083700509/work
conda install datasets==2.9.0 -y || pip install datasets==2.9.0
conda install DateTime==5.1 -y || pip install DateTime==5.1
conda install decorator==4.4.2 -y || pip install decorator==4.4.2
conda install deepspeed==0.6.1 -y || pip install deepspeed==0.6.1
conda install defusedxml==0.7.1 -y || pip install defusedxml==0.7.1
conda install Deprecated==1.2.13 -y || pip install Deprecated==1.2.13
conda install detectron2 @ git+https://github.com/facebookresearch/detectron2.git@1523b3e9929a06d798871eb9afc4c9f770743baf -y || pip install detectron2 @ git+https://github.com/facebookresearch/detectron2.git@1523b3e9929a06d798871eb9afc4c9f770743baf
conda install diff-match-patch @ file:///tmp/build/80754af9/diff-match-patch_1594828741838/work -y || pip install diff-match-patch @ file:///tmp/build/80754af9/diff-match-patch_1594828741838/work
conda install dill==0.3.6 -y || pip install dill==0.3.6
conda install distlib==0.3.6 -y || pip install distlib==0.3.6
conda install distributed @ file:///tmp/build/80754af9/distributed_1605066520644/work -y || pip install distributed @ file:///tmp/build/80754af9/distributed_1605066520644/work
conda install distro==1.8.0 -y || pip install distro==1.8.0
conda install dm-tree==0.1.6 -y || pip install dm-tree==0.1.6
conda install dnspython==2.1.0 -y || pip install dnspython==2.1.0
conda install docker==4.4.4 -y || pip install docker==4.4.4
conda install docker-pycreds==0.4.0 -y || pip install docker-pycreds==0.4.0
conda install docopt==0.6.2 -y || pip install docopt==0.6.2
conda install docutils==0.16 -y || pip install docutils==0.16
conda install easydict==1.9 -y || pip install easydict==1.9
conda install entrypoints==0.3 -y || pip install entrypoints==0.3
conda install et-xmlfile==1.0.1 -y || pip install et-xmlfile==1.0.1
conda install evdev==1.4.0 -y || pip install evdev==1.4.0
conda install eventlet==0.32.0 -y || pip install eventlet==0.32.0
conda install exceptiongroup==1.1.1 -y || pip install exceptiongroup==1.1.1
conda install fairscale==0.4.13 -y || pip install fairscale==0.4.13
conda install fast_ctc_decode==0.3.2 -y || pip install fast_ctc_decode==0.3.2
conda install fastapi==0.95.0 -y || pip install fastapi==0.95.0
conda install fastavro==1.4.7 -y || pip install fastavro==1.4.7
conda install fastcache==1.1.0 -y || pip install fastcache==1.1.0
conda install fasteners==0.16.3 -y || pip install fasteners==0.16.3
conda install ffmpy==0.3.0 -y || pip install ffmpy==0.3.0
conda install fiftyone==0.14.0 -y || pip install fiftyone==0.14.0
conda install fiftyone-brain==0.7.1 -y || pip install fiftyone-brain==0.7.1
conda install fiftyone-db==0.3.0 -y || pip install fiftyone-db==0.3.0
conda install filelock==3.8.0 -y || pip install filelock==3.8.0
conda install fire==0.5.0 -y || pip install fire==0.5.0
conda install flake8 @ file:///tmp/build/80754af9/flake8_1601911421857/work -y || pip install flake8 @ file:///tmp/build/80754af9/flake8_1601911421857/work
conda install Flask==2.2.3 -y || pip install Flask==2.2.3
conda install flask-babel==3.0.1 -y || pip install flask-babel==3.0.1
conda install flatbuffers==1.12 -y || pip install flatbuffers==1.12
conda install fonttools==4.39.2 -y || pip install fonttools==4.39.2
conda install frozenlist==1.3.1 -y || pip install frozenlist==1.3.1
conda install fsspec==2023.1.0 -y || pip install fsspec==2023.1.0
conda install ftfy==6.0.3 -y || pip install ftfy==6.0.3
conda install future==0.18.2 -y || pip install future==0.18.2
conda install fvcore==0.1.5.post20221221 -y || pip install fvcore==0.1.5.post20221221
conda install gast==0.4.0 -y || pip install gast==0.4.0
conda install gdown==4.6.0 -y || pip install gdown==4.6.0
conda install geojson==2.5.0 -y || pip install geojson==2.5.0
conda install gevent==23.7.0 -y || pip install gevent==23.7.0
conda install geventhttpclient==2.0.2 -y || pip install geventhttpclient==2.0.2
conda install gin-config==0.5.0 -y || pip install gin-config==0.5.0
conda install gitdb==4.0.9 -y || pip install gitdb==4.0.9
conda install GitPython==3.1.31 -y || pip install GitPython==3.1.31
conda install glob2==0.7 -y || pip install glob2==0.7
conda install gmpy2==2.0.8 -y || pip install gmpy2==2.0.8
conda install google-api-core==1.31.4 -y || pip install google-api-core==1.31.4
conda install google-api-python-client==1.12.8 -y || pip install google-api-python-client==1.12.8
conda install google-apitools==0.5.31 -y || pip install google-apitools==0.5.31
conda install google-auth==2.21.0 -y || pip install google-auth==2.21.0
conda install google-auth-httplib2==0.1.0 -y || pip install google-auth-httplib2==0.1.0
conda install google-auth-oauthlib==0.4.6 -y || pip install google-auth-oauthlib==0.4.6
conda install google-cloud-aiplatform==1.8.0 -y || pip install google-cloud-aiplatform==1.8.0
conda install google-cloud-bigquery==2.31.0 -y || pip install google-cloud-bigquery==2.31.0
conda install google-cloud-bigquery-storage==2.10.1 -y || pip install google-cloud-bigquery-storage==2.10.1
conda install google-cloud-bigtable==1.7.0 -y || pip install google-cloud-bigtable==1.7.0
conda install google-cloud-core==1.7.2 -y || pip install google-cloud-core==1.7.2
conda install google-cloud-datastore==1.15.3 -y || pip install google-cloud-datastore==1.15.3
conda install google-cloud-dlp==1.0.0 -y || pip install google-cloud-dlp==1.0.0
conda install google-cloud-language==1.3.0 -y || pip install google-cloud-language==1.3.0
conda install google-cloud-pubsub==1.7.0 -y || pip install google-cloud-pubsub==1.7.0
conda install google-cloud-recommendations-ai==0.2.0 -y || pip install google-cloud-recommendations-ai==0.2.0
conda install google-cloud-spanner==1.19.1 -y || pip install google-cloud-spanner==1.19.1
conda install google-cloud-storage==1.43.0 -y || pip install google-cloud-storage==1.43.0
conda install google-cloud-videointelligence==1.16.1 -y || pip install google-cloud-videointelligence==1.16.1
conda install google-cloud-vision==1.0.0 -y || pip install google-cloud-vision==1.0.0
conda install google-crc32c==1.3.0 -y || pip install google-crc32c==1.3.0
conda install google-pasta==0.2.0 -y || pip install google-pasta==0.2.0
conda install google-resumable-media==2.1.0 -y || pip install google-resumable-media==2.1.0
conda install googleapis-common-protos==1.54.0 -y || pip install googleapis-common-protos==1.54.0
conda install gpt4all==0.3.6 -y || pip install gpt4all==0.3.6
conda install gradio==3.22.1 -y || pip install gradio==3.22.1
conda install graphviz==0.19.1 -y || pip install graphviz==0.19.1
conda install greenlet==2.0.2 -y || pip install greenlet==2.0.2
conda install grpc-google-iam-v1==0.12.3 -y || pip install grpc-google-iam-v1==0.12.3
conda install grpcio==1.56.0 -y || pip install grpcio==1.56.0
conda install grpcio-gcp==0.2.2 -y || pip install grpcio-gcp==0.2.2
conda install gviz-api==1.10.0 -y || pip install gviz-api==1.10.0
conda install gym==0.21.0 -y || pip install gym==0.21.0
conda install h11==0.12.0 -y || pip install h11==0.12.0
conda install h5py==3.1.0 -y || pip install h5py==3.1.0
conda install hdfs==2.6.0 -y || pip install hdfs==2.6.0
conda install HeapDict==1.0.1 -y || pip install HeapDict==1.0.1
conda install Historic-Crypto==0.1.6 -y || pip install Historic-Crypto==0.1.6
conda install hjson==3.1.0 -y || pip install hjson==3.1.0
conda install html5lib @ file:///tmp/build/80754af9/html5lib_1593446221756/work -y || pip install html5lib @ file:///tmp/build/80754af9/html5lib_1593446221756/work
conda install httpcore==0.14.1 -y || pip install httpcore==0.14.1
conda install httplib2==0.19.1 -y || pip install httplib2==0.19.1
conda install httpx==0.21.0 -y || pip install httpx==0.21.0
conda install huggingface-hub==0.15.1 -y || pip install huggingface-hub==0.15.1
conda install humanfriendly==10.0 -y || pip install humanfriendly==10.0
conda install hydra-core==1.3.1 -y || pip install hydra-core==1.3.1
conda install idna @ file:///tmp/build/80754af9/idna_1593446292537/work -y || pip install idna @ file:///tmp/build/80754af9/idna_1593446292537/work
conda install imagecodecs==2022.2.22 -y || pip install imagecodecs==2022.2.22
conda install imageio @ file:///tmp/build/80754af9/imageio_1594161405741/work -y || pip install imageio @ file:///tmp/build/80754af9/imageio_1594161405741/work
conda install imageio-ffmpeg==0.4.8 -y || pip install imageio-ffmpeg==0.4.8
conda install imagesize==1.2.0 -y || pip install imagesize==1.2.0
conda install imgaug==0.4.0 -y || pip install imgaug==0.4.0
conda install importlib-metadata==6.1.0 -y || pip install importlib-metadata==6.1.0
conda install importlib-resources==5.4.0 -y || pip install importlib-resources==5.4.0
conda install imutils==0.5.4 -y || pip install imutils==0.5.4
conda install iniconfig @ file:///tmp/build/80754af9/iniconfig_1602780191262/work -y || pip install iniconfig @ file:///tmp/build/80754af9/iniconfig_1602780191262/work
conda install install==1.3.5 -y || pip install install==1.3.5
conda install intervaltree @ file:///tmp/build/80754af9/intervaltree_1598376443606/work -y || pip install intervaltree @ file:///tmp/build/80754af9/intervaltree_1598376443606/work
conda install iopath==0.1.9 -y || pip install iopath==0.1.9
conda install ipykernel @ file:///tmp/build/80754af9/ipykernel_1596207638929/work/dist/ipykernel-5.3.4-py3-none-any.whl -y || pip install ipykernel @ file:///tmp/build/80754af9/ipykernel_1596207638929/work/dist/ipykernel-5.3.4-py3-none-any.whl
conda install ipython @ file:///tmp/build/80754af9/ipython_1604101197014/work -y || pip install ipython @ file:///tmp/build/80754af9/ipython_1604101197014/work
conda install ipython_genutils==0.2.0 -y || pip install ipython_genutils==0.2.0
conda install ipywidgets==7.6.5 -y || pip install ipywidgets==7.6.5
conda install isort @ file:///tmp/build/80754af9/isort_1602603989581/work -y || pip install isort @ file:///tmp/build/80754af9/isort_1602603989581/work
conda install itsdangerous==2.1.2 -y || pip install itsdangerous==2.1.2
conda install jdcal==1.4.1 -y || pip install jdcal==1.4.1
conda install jedi @ file:///tmp/build/80754af9/jedi_1592841866100/work -y || pip install jedi @ file:///tmp/build/80754af9/jedi_1592841866100/work
conda install jeepney @ file:///tmp/build/80754af9/jeepney_1605069705079/work -y || pip install jeepney @ file:///tmp/build/80754af9/jeepney_1605069705079/work
conda install Jinja2==3.1.2 -y || pip install Jinja2==3.1.2
conda install jmespath==0.10.0 -y || pip install jmespath==0.10.0
conda install joblib==0.14.1 -y || pip install joblib==0.14.1
conda install json5==0.9.5 -y || pip install json5==0.9.5
conda install jsonschema @ file:///tmp/build/80754af9/jsonschema_1602607155483/work -y || pip install jsonschema @ file:///tmp/build/80754af9/jsonschema_1602607155483/work
conda install jstyleson==0.0.2 -y || pip install jstyleson==0.0.2
conda install jupyter==1.0.0 -y || pip install jupyter==1.0.0
conda install jupyter-client @ file:///tmp/build/80754af9/jupyter_client_1601311786391/work -y || pip install jupyter-client @ file:///tmp/build/80754af9/jupyter_client_1601311786391/work
conda install jupyter-console @ file:///tmp/build/80754af9/jupyter_console_1598884538475/work -y || pip install jupyter-console @ file:///tmp/build/80754af9/jupyter_console_1598884538475/work
conda install jupyter-core==4.6.3 -y || pip install jupyter-core==4.6.3
conda install jupyter-server==1.13.1 -y || pip install jupyter-server==1.13.1
conda install jupyter-server-mathjax==0.2.3 -y || pip install jupyter-server-mathjax==0.2.3
conda install jupyterlab==2.2.6 -y || pip install jupyterlab==2.2.6
conda install jupyterlab-pygments @ file:///tmp/build/80754af9/jupyterlab_pygments_1601490720602/work -y || pip install jupyterlab-pygments @ file:///tmp/build/80754af9/jupyterlab_pygments_1601490720602/work
conda install jupyterlab-server @ file:///tmp/build/80754af9/jupyterlab_server_1594164409481/work -y || pip install jupyterlab-server @ file:///tmp/build/80754af9/jupyterlab_server_1594164409481/work
conda install jupyterlab-widgets==1.0.2 -y || pip install jupyterlab-widgets==1.0.2
conda install kaleido==0.2.1 -y || pip install kaleido==0.2.1
conda install keras==2.6.0 -y || pip install keras==2.6.0
conda install Keras-Preprocessing==1.1.2 -y || pip install Keras-Preprocessing==1.1.2
conda install keras-tuner==1.1.0 -y || pip install keras-tuner==1.1.0
conda install keyboard==0.13.5 -y || pip install keyboard==0.13.5
conda install keyring @ file:///tmp/build/80754af9/keyring_1601490835422/work -y || pip install keyring @ file:///tmp/build/80754af9/keyring_1601490835422/work
conda install kiwisolver @ file:///tmp/build/80754af9/kiwisolver_1604014535162/work -y || pip install kiwisolver @ file:///tmp/build/80754af9/kiwisolver_1604014535162/work
conda install kt-legacy==1.0.4 -y || pip install kt-legacy==1.0.4
conda install kubernetes==12.0.1 -y || pip install kubernetes==12.0.1
conda install lazy-object-proxy==1.4.3 -y || pip install lazy-object-proxy==1.4.3
conda install libarchive-c==2.9 -y || pip install libarchive-c==2.9
conda install libcst==0.3.23 -y || pip install libcst==0.3.23
conda install linkify-it-py==2.0.0 -y || pip install linkify-it-py==2.0.0
conda install lit==16.0.6 -y || pip install lit==16.0.6
conda install -e git+https://github.com/facebookresearch/llama.git@1076b9c51c77ad06e9d7ba8a4c6df775741732bd#egg=llama -y || pip install -e git+https://github.com/facebookresearch/llama.git@1076b9c51c77ad06e9d7ba8a4c6df775741732bd#egg=llama
conda install llvmlite==0.34.0 -y || pip install llvmlite==0.34.0
conda install lmdb==1.3.0 -y || pip install lmdb==1.3.0
conda install locket==0.2.0 -y || pip install locket==0.2.0
conda install lxml @ file:///tmp/build/80754af9/lxml_1603216285000/work -y || pip install lxml @ file:///tmp/build/80754af9/lxml_1603216285000/work
conda install Markdown==3.3.3 -y || pip install Markdown==3.3.3
conda install markdown-it-py==2.2.0 -y || pip install markdown-it-py==2.2.0
conda install MarkupSafe==2.1.3 -y || pip install MarkupSafe==2.1.3
conda install matplotlib @ file:///tmp/build/80754af9/matplotlib-base_1603378225747/work -y || pip install matplotlib @ file:///tmp/build/80754af9/matplotlib-base_1603378225747/work
conda install mccabe==0.6.1 -y || pip install mccabe==0.6.1
conda install mdit-py-plugins==0.3.3 -y || pip install mdit-py-plugins==0.3.3
conda install mdurl==0.1.2 -y || pip install mdurl==0.1.2
conda install mediapy==1.1.6 -y || pip install mediapy==1.1.6
conda install mistune==0.8.4 -y || pip install mistune==0.8.4
conda install mkl-fft==1.2.0 -y || pip install mkl-fft==1.2.0
conda install mkl-random==1.1.1 -y || pip install mkl-random==1.1.1
conda install mkl-service==2.3.0 -y || pip install mkl-service==2.3.0
conda install ml-metadata==1.3.0 -y || pip install ml-metadata==1.3.0
conda install ml-pipelines-sdk==1.3.4 -y || pip install ml-pipelines-sdk==1.3.4
conda install mock==4.0.2 -y || pip install mock==4.0.2
conda install mongoengine==0.20.0 -y || pip install mongoengine==0.20.0
conda install more-itertools @ file:///tmp/build/80754af9/more-itertools_1605111547926/work -y || pip install more-itertools @ file:///tmp/build/80754af9/more-itertools_1605111547926/work
conda install motor==2.5.1 -y || pip install motor==2.5.1
conda install moviepy==1.0.3 -y || pip install moviepy==1.0.3
conda install mpi4py==3.1.4 -y || pip install mpi4py==3.1.4
conda install mpld3==0.5.9 -y || pip install mpld3==0.5.9
conda install mpmath==1.1.0 -y || pip install mpmath==1.1.0
conda install msgpack==1.0.0 -y || pip install msgpack==1.0.0
conda install multidict==6.0.4 -y || pip install multidict==6.0.4
conda install multipledispatch==0.6.0 -y || pip install multipledispatch==0.6.0
conda install multiprocess==0.70.14 -y || pip install multiprocess==0.70.14
conda install mypy-extensions==0.4.3 -y || pip install mypy-extensions==0.4.3
conda install navigator-updater==0.2.1 -y || pip install navigator-updater==0.2.1
conda install nbclient @ file:///tmp/build/80754af9/nbclient_1602783176460/work -y || pip install nbclient @ file:///tmp/build/80754af9/nbclient_1602783176460/work
conda install nbconvert @ file:///tmp/build/80754af9/nbconvert_1601914830498/work -y || pip install nbconvert @ file:///tmp/build/80754af9/nbconvert_1601914830498/work
conda install nbdime==3.1.1 -y || pip install nbdime==3.1.1
conda install nbformat @ file:///tmp/build/80754af9/nbformat_1602783287752/work -y || pip install nbformat @ file:///tmp/build/80754af9/nbformat_1602783287752/work
conda install ndjson==0.3.1 -y || pip install ndjson==0.3.1
conda install nest-asyncio @ file:///tmp/build/80754af9/nest-asyncio_1605115881283/work -y || pip install nest-asyncio @ file:///tmp/build/80754af9/nest-asyncio_1605115881283/work
conda install networkx==2.8.2 -y || pip install networkx==2.8.2
conda install nibabel==3.2.2 -y || pip install nibabel==3.2.2
conda install ninja==1.11.1 -y || pip install ninja==1.11.1
conda install nltk==3.6.5 -y || pip install nltk==3.6.5
conda install nose==1.3.7 -y || pip install nose==1.3.7
conda install notebook @ file:///tmp/build/80754af9/notebook_1601501575118/work -y || pip install notebook @ file:///tmp/build/80754af9/notebook_1601501575118/work
conda install numba @ file:///tmp/build/80754af9/numba_1600100669015/work -y || pip install numba @ file:///tmp/build/80754af9/numba_1600100669015/work
conda install numexpr==2.7.3 -y || pip install numexpr==2.7.3
conda install numpy==1.22.4 -y || pip install numpy==1.22.4
conda install numpydoc @ file:///tmp/build/80754af9/numpydoc_1605117425582/work -y || pip install numpydoc @ file:///tmp/build/80754af9/numpydoc_1605117425582/work
conda install nvidia-cublas-cu11==11.10.3.66 -y || pip install nvidia-cublas-cu11==11.10.3.66
conda install nvidia-cuda-cupti-cu11==11.7.101 -y || pip install nvidia-cuda-cupti-cu11==11.7.101
conda install nvidia-cuda-nvrtc-cu11==11.7.99 -y || pip install nvidia-cuda-nvrtc-cu11==11.7.99
conda install nvidia-cuda-runtime-cu11==11.7.99 -y || pip install nvidia-cuda-runtime-cu11==11.7.99
conda install nvidia-cudnn-cu11==8.5.0.96 -y || pip install nvidia-cudnn-cu11==8.5.0.96
conda install nvidia-cufft-cu11==10.9.0.58 -y || pip install nvidia-cufft-cu11==10.9.0.58
conda install nvidia-curand-cu11==10.2.10.91 -y || pip install nvidia-curand-cu11==10.2.10.91
conda install nvidia-cusolver-cu11==11.4.0.1 -y || pip install nvidia-cusolver-cu11==11.4.0.1
conda install nvidia-cusparse-cu11==11.7.4.91 -y || pip install nvidia-cusparse-cu11==11.7.4.91
conda install nvidia-nccl-cu11==2.14.3 -y || pip install nvidia-nccl-cu11==2.14.3
conda install nvidia-nvtx-cu11==11.7.91 -y || pip install nvidia-nvtx-cu11==11.7.91
conda install oauth2client==4.1.3 -y || pip install oauth2client==4.1.3
conda install oauthlib==3.1.0 -y || pip install oauthlib==3.1.0
conda install olefile==0.46 -y || pip install olefile==0.46
conda install omegaconf==2.3.0 -y || pip install omegaconf==2.3.0
conda install onnx==1.11.0 -y || pip install onnx==1.11.0
conda install onnx-simplifier==0.3.10 -y || pip install onnx-simplifier==0.3.10
conda install onnxoptimizer==0.2.7 -y || pip install onnxoptimizer==0.2.7
conda install onnxruntime==1.11.1 -y || pip install onnxruntime==1.11.1
conda install opencv-contrib-python==3.4.11.41 -y || pip install opencv-contrib-python==3.4.11.41
conda install opencv-python==4.8.0.74 -y || pip install opencv-python==4.8.0.74
conda install openpyxl @ file:///tmp/build/80754af9/openpyxl_1598113097404/work -y || pip install openpyxl @ file:///tmp/build/80754af9/openpyxl_1598113097404/work
conda install openvino==2022.1.0 -y || pip install openvino==2022.1.0
conda install openvino-dev==2022.1.0 -y || pip install openvino-dev==2022.1.0
conda install openvino-telemetry==2022.1.1 -y || pip install openvino-telemetry==2022.1.1
conda install opt-einsum==3.3.0 -y || pip install opt-einsum==3.3.0
conda install orjson==3.6.5 -y || pip install orjson==3.6.5
conda install outcome==1.2.0 -y || pip install outcome==1.2.0
conda install packaging==23.0 -y || pip install packaging==23.0
conda install paddleocr==2.6.1.3 -y || pip install paddleocr==2.6.1.3
conda install pandas==1.3.5 -y || pip install pandas==1.3.5
conda install pandocfilters @ file:///tmp/build/80754af9/pandocfilters_1605120460739/work -y || pip install pandocfilters @ file:///tmp/build/80754af9/pandocfilters_1605120460739/work
conda install parasail==1.2.4 -y || pip install parasail==1.2.4
conda install parso==0.7.0 -y || pip install parso==0.7.0
conda install partd==1.1.0 -y || pip install partd==1.1.0
conda install path @ file:///tmp/build/80754af9/path_1598376507494/work -y || pip install path @ file:///tmp/build/80754af9/path_1598376507494/work
conda install pathlib2==2.3.5 -y || pip install pathlib2==2.3.5
conda install pathspec==0.11.0 -y || pip install pathspec==0.11.0
conda install pathtools==0.1.2 -y || pip install pathtools==0.1.2
conda install patool==1.12 -y || pip install patool==1.12
conda install patsy==0.5.1 -y || pip install patsy==0.5.1
conda install pdf2docx==0.5.6 -y || pip install pdf2docx==0.5.6
conda install pep8==1.7.1 -y || pip install pep8==1.7.1
conda install pexpect==4.8.0 -y || pip install pexpect==4.8.0
conda install pickleshare==0.7.5 -y || pip install pickleshare==0.7.5
conda install Pillow==8.4.0 -y || pip install Pillow==8.4.0
conda install pkginfo==1.6.1 -y || pip install pkginfo==1.6.1
conda install platformdirs==2.5.2 -y || pip install platformdirs==2.5.2
conda install playwright==1.30.0 -y || pip install playwright==1.30.0
conda install plotly==4.14.3 -y || pip install plotly==4.14.3
conda install pluggy==0.13.1 -y || pip install pluggy==0.13.1
conda install ply==3.11 -y || pip install ply==3.11
conda install pooch==1.5.2 -y || pip install pooch==1.5.2
conda install portalocker==2.7.0 -y || pip install portalocker==2.7.0
conda install portpicker==1.5.0 -y || pip install portpicker==1.5.0
conda install pprintpp==0.4.0 -y || pip install pprintpp==0.4.0
conda install praw==7.7.0 -y || pip install praw==7.7.0
conda install prawcore==2.3.0 -y || pip install prawcore==2.3.0
conda install premailer==3.10.0 -y || pip install premailer==3.10.0
conda install proglog==0.1.10 -y || pip install proglog==0.1.10
conda install progress==1.6 -y || pip install progress==1.6
conda install progressbar2==4.2.0 -y || pip install progressbar2==4.2.0
conda install prometheus-client==0.8.0 -y || pip install prometheus-client==0.8.0
conda install promise==2.3 -y || pip install promise==2.3
conda install prompt-toolkit @ file:///tmp/build/80754af9/prompt-toolkit_1602688806899/work -y || pip install prompt-toolkit @ file:///tmp/build/80754af9/prompt-toolkit_1602688806899/work
conda install proto-plus==1.19.8 -y || pip install proto-plus==1.19.8
conda install protobuf==3.19.1 -y || pip install protobuf==3.19.1
conda install psutil==5.9.3 -y || pip install psutil==5.9.3
conda install ptyprocess==0.6.0 -y || pip install ptyprocess==0.6.0
conda install py @ file:///tmp/build/80754af9/py_1593446248552/work -y || pip install py @ file:///tmp/build/80754af9/py_1593446248552/work
conda install py-cpuinfo==8.0.0 -y || pip install py-cpuinfo==8.0.0
conda install pyarrow==11.0.0 -y || pip install pyarrow==11.0.0
conda install pyasn1==0.4.8 -y || pip install pyasn1==0.4.8
conda install pyasn1-modules==0.2.8 -y || pip install pyasn1-modules==0.2.8
conda install pyclipper==1.3.0.post2 -y || pip install pyclipper==1.3.0.post2
conda install pycocotools==2.0.4 -y || pip install pycocotools==2.0.4
conda install pycodestyle==2.6.0 -y || pip install pycodestyle==2.6.0
conda install pycoral==0.1.0 -y || pip install pycoral==0.1.0
conda install pycosat==0.6.3 -y || pip install pycosat==0.6.3
conda install pycparser @ file:///tmp/build/80754af9/pycparser_1594388511720/work -y || pip install pycparser @ file:///tmp/build/80754af9/pycparser_1594388511720/work
conda install pycryptodome==3.17 -y || pip install pycryptodome==3.17
conda install pycurl==7.43.0.6 -y || pip install pycurl==7.43.0.6
conda install pydantic==1.8.2 -y || pip install pydantic==1.8.2
conda install pydicom==2.3.0 -y || pip install pydicom==2.3.0
conda install pydocstyle @ file:///tmp/build/80754af9/pydocstyle_1598885001695/work -y || pip install pydocstyle @ file:///tmp/build/80754af9/pydocstyle_1598885001695/work
conda install pydot==1.4.2 -y || pip install pydot==1.4.2
conda install pydub==0.25.1 -y || pip install pydub==0.25.1
conda install pyee==9.0.4 -y || pip install pyee==9.0.4
conda install pyflakes==2.2.0 -y || pip install pyflakes==2.2.0
conda install pygame==2.1.2 -y || pip install pygame==2.1.2
conda install pyglet==1.5.21 -y || pip install pyglet==1.5.21
conda install Pygments @ file:///tmp/build/80754af9/pygments_1604103097372/work -y || pip install Pygments @ file:///tmp/build/80754af9/pygments_1604103097372/work
conda install pylint @ file:///tmp/build/80754af9/pylint_1598623985952/work -y || pip install pylint @ file:///tmp/build/80754af9/pylint_1598623985952/work
conda install pymongo==3.12.1 -y || pip install pymongo==3.12.1
conda install PyMuPDF==1.20.2 -y || pip install PyMuPDF==1.20.2
conda install PyNaCl==1.5.0 -y || pip install PyNaCl==1.5.0
conda install pynput==1.7.4 -y || pip install pynput==1.7.4
conda install pyodbc===4.0.0-unsupported -y || pip install pyodbc===4.0.0-unsupported
conda install pyOpenSSL @ file:///tmp/build/80754af9/pyopenssl_1594392929924/work -y || pip install pyOpenSSL @ file:///tmp/build/80754af9/pyopenssl_1594392929924/work
conda install pyparsing==2.4.7 -y || pip install pyparsing==2.4.7
conda install PyQt5==5.15.9 -y || pip install PyQt5==5.15.9
conda install PyQt5-Qt5==5.15.2 -y || pip install PyQt5-Qt5==5.15.2
conda install PyQt5-sip==12.12.1 -y || pip install PyQt5-sip==12.12.1
conda install pyrsistent @ file:///tmp/build/80754af9/pyrsistent_1600141720057/work -y || pip install pyrsistent @ file:///tmp/build/80754af9/pyrsistent_1600141720057/work
conda install PySocks==1.7.1 -y || pip install PySocks==1.7.1
conda install pytest==0.0.0 -y || pip install pytest==0.0.0
conda install python-dateutil==2.8.1 -y || pip install python-dateutil==2.8.1
conda install python-docx==0.8.11 -y || pip install python-docx==0.8.11
conda install python-dotenv==0.20.0 -y || pip install python-dotenv==0.20.0
conda install python-jsonrpc-server @ file:///tmp/build/80754af9/python-jsonrpc-server_1600278539111/work -y || pip install python-jsonrpc-server @ file:///tmp/build/80754af9/python-jsonrpc-server_1600278539111/work
conda install python-language-server @ file:///tmp/build/80754af9/python-language-server_1600454544709/work -y || pip install python-language-server @ file:///tmp/build/80754af9/python-language-server_1600454544709/work
conda install python-multipart==0.0.6 -y || pip install python-multipart==0.0.6
conda install python-rapidjson==1.10 -y || pip install python-rapidjson==1.10
conda install python-utils==3.4.5 -y || pip install python-utils==3.4.5
conda install python-xlib==0.31 -y || pip install python-xlib==0.31
conda install pytube==15.0.0 -y || pip install pytube==15.0.0
conda install pytz==2022.7.1 -y || pip install pytz==2022.7.1
conda install pytz-deprecation-shim==0.1.0.post0 -y || pip install pytz-deprecation-shim==0.1.0.post0
conda install PyVirtualDisplay==3.0 -y || pip install PyVirtualDisplay==3.0
conda install PyWavelets @ file:///tmp/build/80754af9/pywavelets_1601658317819/work -y || pip install PyWavelets @ file:///tmp/build/80754af9/pywavelets_1601658317819/work
conda install pyxdg @ file:///tmp/build/80754af9/pyxdg_1603822279816/work -y || pip install pyxdg @ file:///tmp/build/80754af9/pyxdg_1603822279816/work
conda install PyYAML==5.3.1 -y || pip install PyYAML==5.3.1
conda install pyzmq==19.0.2 -y || pip install pyzmq==19.0.2
conda install QDarkStyle==2.8.1 -y || pip install QDarkStyle==2.8.1
conda install QtAwesome @ file:///tmp/build/80754af9/qtawesome_1602272867890/work -y || pip install QtAwesome @ file:///tmp/build/80754af9/qtawesome_1602272867890/work
conda install qtconsole @ file:///tmp/build/80754af9/qtconsole_1600870028330/work -y || pip install qtconsole @ file:///tmp/build/80754af9/qtconsole_1600870028330/work
conda install QtPy==1.9.0 -y || pip install QtPy==1.9.0
conda install qudida==0.0.4 -y || pip install qudida==0.0.4
conda install rapidfuzz==2.13.7 -y || pip install rapidfuzz==2.13.7
conda install rarfile==4.0 -y || pip install rarfile==4.0
conda install rawpy==0.17.1 -y || pip install rawpy==0.17.1
conda install ray==2.0.1 -y || pip install ray==2.0.1
conda install regex==2023.8.8 -y || pip install regex==2023.8.8
conda install requests==2.26.0 -y || pip install requests==2.26.0
conda install requests-oauthlib==1.3.1 -y || pip install requests-oauthlib==1.3.1
conda install requests-toolbelt==0.9.1 -y || pip install requests-toolbelt==0.9.1
conda install resampy==0.2.2 -y || pip install resampy==0.2.2
conda install responses==0.18.0 -y || pip install responses==0.18.0
conda install retrying==1.3.3 -y || pip install retrying==1.3.3
conda install rfc3986==1.5.0 -y || pip install rfc3986==1.5.0
conda install rich==12.4.4 -y || pip install rich==12.4.4
conda install roboflow==0.2.4 -y || pip install roboflow==0.2.4
conda install rope @ file:///tmp/build/80754af9/rope_1602264064449/work -y || pip install rope @ file:///tmp/build/80754af9/rope_1602264064449/work
conda install rsa==4.9 -y || pip install rsa==4.9
conda install Rtree==0.9.4 -y || pip install Rtree==0.9.4
conda install ruamel_yaml==0.15.87 -y || pip install ruamel_yaml==0.15.87
conda install s3transfer==0.5.0 -y || pip install s3transfer==0.5.0
conda install sacremoses==0.0.46 -y || pip install sacremoses==0.0.46
conda install safetensors==0.3.1 -y || pip install safetensors==0.3.1
conda install scikit-build==0.16.2 -y || pip install scikit-build==0.16.2
conda install scikit-image==0.17.2 -y || pip install scikit-image==0.17.2
conda install scikit-learn==0.19.2 -y || pip install scikit-learn==0.19.2
conda install scipy @ file:///tmp/build/80754af9/scipy_1616703172749/work -y || pip install scipy @ file:///tmp/build/80754af9/scipy_1616703172749/work
conda install seaborn @ file:///tmp/build/80754af9/seaborn_1600553570093/work -y || pip install seaborn @ file:///tmp/build/80754af9/seaborn_1600553570093/work
conda install SecretStorage==3.1.2 -y || pip install SecretStorage==3.1.2
conda install selenium==4.10.0 -y || pip install selenium==4.10.0
conda install Send2Trash==1.5.0 -y || pip install Send2Trash==1.5.0
conda install sentence-transformers==2.2.2 -y || pip install sentence-transformers==2.2.2
conda install sentencepiece==0.1.97 -y || pip install sentencepiece==0.1.97
conda install sentry-sdk==1.5.12 -y || pip install sentry-sdk==1.5.12
conda install setproctitle==1.2.3 -y || pip install setproctitle==1.2.3
conda install Shapely==1.8.2 -y || pip install Shapely==1.8.2
conda install shortuuid==1.0.9 -y || pip install shortuuid==1.0.9
conda install simplegeneric==0.8.1 -y || pip install simplegeneric==0.8.1
conda install singledispatch @ file:///tmp/build/80754af9/singledispatch_1602523705405/work -y || pip install singledispatch @ file:///tmp/build/80754af9/singledispatch_1602523705405/work
conda install sip==4.19.13 -y || pip install sip==4.19.13
conda install six @ file:///tmp/build/80754af9/six_1605205327372/work -y || pip install six @ file:///tmp/build/80754af9/six_1605205327372/work
conda install smmap==5.0.0 -y || pip install smmap==5.0.0
conda install sniffio==1.2.0 -y || pip install sniffio==1.2.0
conda install snowballstemmer==2.0.0 -y || pip install snowballstemmer==2.0.0
conda install sortedcollections==1.2.1 -y || pip install sortedcollections==1.2.1
conda install sortedcontainers==2.2.2 -y || pip install sortedcontainers==2.2.2
conda install SoundFile==0.10.3.post1 -y || pip install SoundFile==0.10.3.post1
conda install soupsieve==2.0.1 -y || pip install soupsieve==2.0.1
conda install Sphinx @ file:///tmp/build/80754af9/sphinx_1597428793432/work -y || pip install Sphinx @ file:///tmp/build/80754af9/sphinx_1597428793432/work
conda install sphinxcontrib-applehelp==1.0.2 -y || pip install sphinxcontrib-applehelp==1.0.2
conda install sphinxcontrib-devhelp==1.0.2 -y || pip install sphinxcontrib-devhelp==1.0.2
conda install sphinxcontrib-htmlhelp==1.0.3 -y || pip install sphinxcontrib-htmlhelp==1.0.3
conda install sphinxcontrib-jsmath==1.0.1 -y || pip install sphinxcontrib-jsmath==1.0.1
conda install sphinxcontrib-qthelp==1.0.3 -y || pip install sphinxcontrib-qthelp==1.0.3
conda install sphinxcontrib-serializinghtml==1.1.4 -y || pip install sphinxcontrib-serializinghtml==1.1.4
conda install sphinxcontrib-websupport @ file:///tmp/build/80754af9/sphinxcontrib-websupport_1597081412696/work -y || pip install sphinxcontrib-websupport @ file:///tmp/build/80754af9/sphinxcontrib-websupport_1597081412696/work
conda install split-folders==0.4.3 -y || pip install split-folders==0.4.3
conda install spyder-kernels @ file:///tmp/build/80754af9/spyder-kernels_1599056754858/work -y || pip install spyder-kernels @ file:///tmp/build/80754af9/spyder-kernels_1599056754858/work
conda install SQLAlchemy @ file:///tmp/build/80754af9/sqlalchemy_1603397987316/work -y || pip install SQLAlchemy @ file:///tmp/build/80754af9/sqlalchemy_1603397987316/work
conda install starlette==0.26.1 -y || pip install starlette==0.26.1
conda install statsmodels @ file:///tmp/build/80754af9/statsmodels_1602280205159/work -y || pip install statsmodels @ file:///tmp/build/80754af9/statsmodels_1602280205159/work
conda install sympy @ file:///tmp/build/80754af9/sympy_1605119542615/work -y || pip install sympy @ file:///tmp/build/80754af9/sympy_1605119542615/work
conda install tables==3.6.1 -y || pip install tables==3.6.1
conda install tabulate==0.8.9 -y || pip install tabulate==0.8.9
conda install tblib @ file:///tmp/build/80754af9/tblib_1597928476713/work -y || pip install tblib @ file:///tmp/build/80754af9/tblib_1597928476713/work
conda install tensorboard==2.13.0 -y || pip install tensorboard==2.13.0
conda install tensorboard-data-server==0.7.1 -y || pip install tensorboard-data-server==0.7.1
conda install tensorboard-plugin-profile==2.5.0 -y || pip install tensorboard-plugin-profile==2.5.0
conda install tensorboard-plugin-wit==1.8.1 -y || pip install tensorboard-plugin-wit==1.8.1
conda install tensorboardX==2.4 -y || pip install tensorboardX==2.4
conda install tensorflow==2.6.1 -y || pip install tensorflow==2.6.1
conda install tensorflow-addons==0.16.1 -y || pip install tensorflow-addons==0.16.1
conda install tensorflow-data-validation==1.3.0 -y || pip install tensorflow-data-validation==1.3.0
conda install tensorflow-datasets==4.4.0 -y || pip install tensorflow-datasets==4.4.0
conda install tensorflow-estimator==2.4.0 -y || pip install tensorflow-estimator==2.4.0
conda install tensorflow-gpu==2.4.0 -y || pip install tensorflow-gpu==2.4.0
conda install tensorflow-hub==0.12.0 -y || pip install tensorflow-hub==0.12.0
conda install tensorflow-metadata==1.2.0 -y || pip install tensorflow-metadata==1.2.0
conda install tensorflow-model-analysis==0.34.1 -y || pip install tensorflow-model-analysis==0.34.1
conda install tensorflow-probability==0.14.1 -y || pip install tensorflow-probability==0.14.1
conda install tensorflow-serving-api==2.6.1 -y || pip install tensorflow-serving-api==2.6.1
conda install tensorflow-transform==1.3.0 -y || pip install tensorflow-transform==1.3.0
conda install tensorflowjs==3.18.0 -y || pip install tensorflowjs==3.18.0
conda install termcolor==2.2.0 -y || pip install termcolor==2.2.0
conda install terminado==0.9.1 -y || pip install terminado==0.9.1
conda install testpath==0.4.4 -y || pip install testpath==0.4.4
conda install texttable==1.6.4 -y || pip install texttable==1.6.4
conda install tf-agents==0.10.0 -y || pip install tf-agents==0.10.0
conda install tfx==1.3.4 -y || pip install tfx==1.3.4
conda install tfx-bsl==1.3.0 -y || pip install tfx-bsl==1.3.0
conda install thop==0.1.1.post2209072238 -y || pip install thop==0.1.1.post2209072238
conda install threadpoolctl @ file:///tmp/tmp9twdgx9k/threadpoolctl-2.1.0-py3-none-any.whl -y || pip install threadpoolctl @ file:///tmp/tmp9twdgx9k/threadpoolctl-2.1.0-py3-none-any.whl
conda install tifffile==2020.10.1 -y || pip install tifffile==2020.10.1
conda install TikTokApi==5.2.2 -y || pip install TikTokApi==5.2.2
conda install tiktoken==0.4.0 -y || pip install tiktoken==0.4.0
conda install timm==0.6.12 -y || pip install timm==0.6.12
conda install tk==0.1.0 -y || pip install tk==0.1.0
conda install tokenizers==0.13.2 -y || pip install tokenizers==0.13.2
conda install toml @ file:///tmp/build/80754af9/toml_1592853716807/work -y || pip install toml @ file:///tmp/build/80754af9/toml_1592853716807/work
conda install tomli==2.0.1 -y || pip install tomli==2.0.1
conda install toolz @ file:///tmp/build/80754af9/toolz_1601054250827/work -y || pip install toolz @ file:///tmp/build/80754af9/toolz_1601054250827/work
conda install torch==2.0.1 -y || pip install torch==2.0.1
conda install torch-tb-profiler==0.3.1 -y || pip install torch-tb-profiler==0.3.1
conda install torchaudio==0.9.0 -y || pip install torchaudio==0.9.0
conda install torchdata==0.6.1 -y || pip install torchdata==0.6.1
conda install torchsummary==1.5.1 -y || pip install torchsummary==1.5.1
conda install torchtext==0.15.2 -y || pip install torchtext==0.15.2
conda install torchvision==0.15.2 -y || pip install torchvision==0.15.2
conda install tornado==6.1 -y || pip install tornado==6.1
conda install tqdm==4.64.1 -y || pip install tqdm==4.64.1
conda install traitlets @ file:///tmp/build/80754af9/traitlets_1602787416690/work -y || pip install traitlets @ file:///tmp/build/80754af9/traitlets_1602787416690/work
conda install transformers==4.30.2 -y || pip install transformers==4.30.2
conda install trio==0.22.0 -y || pip install trio==0.22.0
conda install trio-websocket==0.10.3 -y || pip install trio-websocket==0.10.3
conda install triton==2.0.0 -y || pip install triton==2.0.0
conda install tritonclient==2.31.0 -y || pip install tritonclient==2.31.0
conda install typeguard==2.13.3 -y || pip install typeguard==2.13.3
conda install typing-inspect==0.7.1 -y || pip install typing-inspect==0.7.1
conda install typing_extensions==4.4.0 -y || pip install typing_extensions==4.4.0
conda install tzdata==2021.5 -y || pip install tzdata==2021.5
conda install tzlocal==4.1 -y || pip install tzlocal==4.1
conda install uc-micro-py==1.0.1 -y || pip install uc-micro-py==1.0.1
conda install ujson @ file:///tmp/build/80754af9/ujson_1602523317881/work -y || pip install ujson @ file:///tmp/build/80754af9/ujson_1602523317881/work
conda install ultralytics==8.0.153 -y || pip install ultralytics==8.0.153
conda install unicodecsv==0.14.1 -y || pip install unicodecsv==0.14.1
conda install universal-analytics-python3==1.1.1 -y || pip install universal-analytics-python3==1.1.1
conda install update-checker==0.18.0 -y || pip install update-checker==0.18.0
conda install uritemplate==3.0.1 -y || pip install uritemplate==3.0.1
conda install uritools==3.0.2 -y || pip install uritools==3.0.2
conda install urlextract==1.4.0 -y || pip install urlextract==1.4.0
conda install urllib3==1.26.16 -y || pip install urllib3==1.26.16
conda install uvicorn==0.21.1 -y || pip install uvicorn==0.21.1
conda install vastai==0.1.7 -y || pip install vastai==0.1.7
conda install virtualenv==20.16.6 -y || pip install virtualenv==20.16.6
conda install visualdl==2.5.1 -y || pip install visualdl==2.5.1
conda install voxel51-eta==0.5.3 -y || pip install voxel51-eta==0.5.3
conda install wandb==0.12.17 -y || pip install wandb==0.12.17
conda install watchdog @ file:///tmp/build/80754af9/watchdog_1593447344699/work -y || pip install watchdog @ file:///tmp/build/80754af9/watchdog_1593447344699/work
conda install wcwidth @ file:///tmp/build/80754af9/wcwidth_1593447189090/work -y || pip install wcwidth @ file:///tmp/build/80754af9/wcwidth_1593447189090/work
conda install webencodings==0.5.1 -y || pip install webencodings==0.5.1
conda install websocket-client==1.2.3 -y || pip install websocket-client==1.2.3
conda install websockets==10.4 -y || pip install websockets==10.4
conda install Werkzeug==2.3.6 -y || pip install Werkzeug==2.3.6
conda install wget==3.2 -y || pip install wget==3.2
conda install widgetsnbextension==3.5.1 -y || pip install widgetsnbextension==3.5.1
conda install wrapt==1.11.2 -y || pip install wrapt==1.11.2
conda install wsproto==1.2.0 -y || pip install wsproto==1.2.0
conda install wurlitzer @ file:///tmp/build/80754af9/wurlitzer_1594753850195/work -y || pip install wurlitzer @ file:///tmp/build/80754af9/wurlitzer_1594753850195/work
conda install x2paddle==1.4.0 -y || pip install x2paddle==1.4.0
conda install xgboost==1.4.2 -y || pip install xgboost==1.4.2
conda install xlrd==1.2.0 -y || pip install xlrd==1.2.0
conda install XlsxWriter @ file:///tmp/build/80754af9/xlsxwriter_1602692860603/work -y || pip install XlsxWriter @ file:///tmp/build/80754af9/xlsxwriter_1602692860603/work
conda install xlwt==1.3.0 -y || pip install xlwt==1.3.0
conda install xmltodict==0.12.0 -y || pip install xmltodict==0.12.0
conda install xxhash==3.2.0 -y || pip install xxhash==3.2.0
conda install yacs==0.1.8 -y || pip install yacs==0.1.8
conda install yapf @ file:///tmp/build/80754af9/yapf_1593528177422/work -y || pip install yapf @ file:///tmp/build/80754af9/yapf_1593528177422/work
conda install yarl==1.8.2 -y || pip install yarl==1.8.2
conda install youtube-dl==2021.12.17 -y || pip install youtube-dl==2021.12.17
conda install zict==2.0.0 -y || pip install zict==2.0.0
conda install zipp @ file:///tmp/build/80754af9/zipp_1604001098328/work -y || pip install zipp @ file:///tmp/build/80754af9/zipp_1604001098328/work
conda install zope.event==4.5.0 -y || pip install zope.event==4.5.0
conda install zope.interface @ file:///tmp/build/80754af9/zope.interface_1602002420968/work -y || pip install zope.interface @ file:///tmp/build/80754af9/zope.interface_1602002420968/work
conda install  -y || pip install 