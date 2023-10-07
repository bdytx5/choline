#!/bin/bash
# Download Miniconda installer
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
# Install Miniconda
# bash miniconda.sh -b -p $HOME/miniconda
# Initialize conda
# . $HOME/miniconda/bin/activate
# conda init
# Create environment
# conda create --name choline python=3.10.10 -y
# Activate environment
# conda activate choline
# Install vim
sudo apt upgrade
sudo apt install vim -y
sudo apt install python3 -y
sudo apt install python3-pip -y
# Set Wandb API key without user interaction
export WANDB_API_KEY=20
pip install absl-py==1.4.0 || pip3 install absl-py==1.4.0 -y
pip install accelerate==0.23.0 || pip3 install accelerate==0.23.0 -y
pip install aiohttp==3.8.5 || pip3 install aiohttp==3.8.5 -y
pip install aiosignal==1.3.1 || pip3 install aiosignal==1.3.1 -y
pip install altgraph==0.17.3 || pip3 install altgraph==0.17.3 -y
pip install appdirs==1.4.4 || pip3 install appdirs==1.4.4 -y
pip install astunparse==1.6.3 || pip3 install astunparse==1.6.3 -y
pip install async-timeout==4.0.3 || pip3 install async-timeout==4.0.3 -y
pip install attrs==23.1.0 || pip3 install attrs==23.1.0 -y
pip install awsgi==0.0.5 || pip3 install awsgi==0.0.5 -y
pip install banana-cli==0.0.15 || pip3 install banana-cli==0.0.15 -y
pip install bcrypt==4.0.1 || pip3 install bcrypt==4.0.1 -y
pip install beautifulsoup4==4.12.2 || pip3 install beautifulsoup4==4.12.2 -y
pip install blinker==1.6.2 || pip3 install blinker==1.6.2 -y
pip install boltons @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_f63n9uulmp/croot/boltons_1677628710094/work || pip3 install boltons @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_f63n9uulmp/croot/boltons_1677628710094/work -y
pip install boto3==1.28.25 || pip3 install boto3==1.28.25 -y
pip install botocore==1.31.25 || pip3 install botocore==1.31.25 -y
pip install brotlipy==0.7.0 || pip3 install brotlipy==0.7.0 -y
pip install bs4==0.0.1 || pip3 install bs4==0.0.1 -y
pip install CacheControl==0.13.1 || pip3 install CacheControl==0.13.1 -y
pip install cachetools==5.3.1 || pip3 install cachetools==5.3.1 -y
pip install certifi==2022.12.7 || pip3 install certifi==2022.12.7 -y
pip install cffi @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_ab19r4bji3/croot/cffi_1670423206034/work || pip3 install cffi @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_ab19r4bji3/croot/cffi_1670423206034/work -y
pip install chardet==4.0.0 || pip3 install chardet==4.0.0 -y
pip install charset-normalizer==3.1.0 || pip3 install charset-normalizer==3.1.0 -y
pip install click==8.1.3 || pip3 install click==8.1.3 -y
pip install cloudevents==1.9.0 || pip3 install cloudevents==1.9.0 -y
pip install cloudpickle==2.2.1 || pip3 install cloudpickle==2.2.1 -y
pip install conda @ file:///private/var/folders/k1/30mswbxs7r1g6zwn8y4fyt500000gp/T/abs_3ehd9hpsix/croot/conda_1690494984812/work || pip3 install conda @ file:///private/var/folders/k1/30mswbxs7r1g6zwn8y4fyt500000gp/T/abs_3ehd9hpsix/croot/conda_1690494984812/work -y
pip install conda-content-trust @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_11146a2b-93c2-444c-a378-ad4fac363e991s0r1hnp/croots/recipe/conda-content-trust_1658126383571/work || pip3 install conda-content-trust @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_11146a2b-93c2-444c-a378-ad4fac363e991s0r1hnp/croots/recipe/conda-content-trust_1658126383571/work -y
pip install conda-package-handling @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_5f3f459f9v/croot/conda-package-handling_1672865025324/work || pip3 install conda-package-handling @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_5f3f459f9v/croot/conda-package-handling_1672865025324/work -y
pip install conda_package_streaming @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_58gpsa_6af/croot/conda-package-streaming_1670508144037/work || pip3 install conda_package_streaming @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_58gpsa_6af/croot/conda-package-streaming_1670508144037/work -y
pip install contourpy==1.1.0 || pip3 install contourpy==1.1.0 -y
pip install cryptography @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_a9zjqvif1f/croot/cryptography_1677533099634/work || pip3 install cryptography @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_a9zjqvif1f/croot/cryptography_1677533099634/work -y
pip install cycler==0.10.0 || pip3 install cycler==0.10.0 -y
pip install datasets==2.14.5 || pip3 install datasets==2.14.5 -y
pip install DateTime==5.1 || pip3 install DateTime==5.1 -y
pip install decorator==4.4.2 || pip3 install decorator==4.4.2 -y
pip install deprecation==2.1.0 || pip3 install deprecation==2.1.0 -y
pip install dill==0.3.7 || pip3 install dill==0.3.7 -y
pip install dm-tree==0.1.8 || pip3 install dm-tree==0.1.8 -y
pip install docker-pycreds==0.4.0 || pip3 install docker-pycreds==0.4.0 -y
pip install exceptiongroup==1.1.2 || pip3 install exceptiongroup==1.1.2 -y
pip install filelock==3.12.2 || pip3 install filelock==3.12.2 -y
pip install fire==0.5.0 || pip3 install fire==0.5.0 -y
pip install firebase==4.0.1 || pip3 install firebase==4.0.1 -y
pip install firebase-admin==6.2.0 || pip3 install firebase-admin==6.2.0 -y
pip install firebase-functions==0.1.1 || pip3 install firebase-functions==0.1.1 -y
pip install Flask==2.3.2 || pip3 install Flask==2.3.2 -y
pip install Flask-Cors==4.0.0 || pip3 install Flask-Cors==4.0.0 -y
pip install flatbuffers==23.5.26 || pip3 install flatbuffers==23.5.26 -y
pip install fonttools==4.40.0 || pip3 install fonttools==4.40.0 -y
pip install frozenlist==1.4.0 || pip3 install frozenlist==1.4.0 -y
pip install fsspec==2023.6.0 || pip3 install fsspec==2023.6.0 -y
pip install functions-framework==3.4.0 || pip3 install functions-framework==3.4.0 -y
pip install gast==0.4.0 || pip3 install gast==0.4.0 -y
pip install gitdb==4.0.10 || pip3 install gitdb==4.0.10 -y
pip install GitPython==3.1.31 || pip3 install GitPython==3.1.31 -y
pip install google-api-core==2.11.1 || pip3 install google-api-core==2.11.1 -y
pip install google-api-python-client==2.93.0 || pip3 install google-api-python-client==2.93.0 -y
pip install google-auth==2.21.0 || pip3 install google-auth==2.21.0 -y
pip install google-auth-httplib2==0.1.0 || pip3 install google-auth-httplib2==0.1.0 -y
pip install google-auth-oauthlib==1.0.0 || pip3 install google-auth-oauthlib==1.0.0 -y
pip install google-cloud-core==2.3.2 || pip3 install google-cloud-core==2.3.2 -y
pip install google-cloud-firestore==2.11.1 || pip3 install google-cloud-firestore==2.11.1 -y
pip install google-cloud-storage==2.10.0 || pip3 install google-cloud-storage==2.10.0 -y
pip install google-cloud-texttospeech==2.14.1 || pip3 install google-cloud-texttospeech==2.14.1 -y
pip install google-crc32c==1.5.0 || pip3 install google-crc32c==1.5.0 -y
pip install google-events==0.9.0 || pip3 install google-events==0.9.0 -y
pip install google-pasta==0.2.0 || pip3 install google-pasta==0.2.0 -y
pip install google-resumable-media==2.5.0 || pip3 install google-resumable-media==2.5.0 -y
pip install googleapis-common-protos==1.59.1 || pip3 install googleapis-common-protos==1.59.1 -y
pip install gpt3-package @ file:///Users/brettyoung/Desktop/dev/py_prjs/gpt3/gpt3_package/dist/gpt3_package-0.1.tar.gz#sha256=080cca69cbdf70f56b0871a599b9d9adaa974c5e9735411bce88f128de0ea7fb || pip3 install gpt3-package @ file:///Users/brettyoung/Desktop/dev/py_prjs/gpt3/gpt3_package/dist/gpt3_package-0.1.tar.gz#sha256=080cca69cbdf70f56b0871a599b9d9adaa974c5e9735411bce88f128de0ea7fb -y
pip install gpt4all==0.3.6 || pip3 install gpt4all==0.3.6 -y
pip install grpcio==1.56.0 || pip3 install grpcio==1.56.0 -y
pip install grpcio-status==1.56.0 || pip3 install grpcio-status==1.56.0 -y
pip install gunicorn==20.1.0 || pip3 install gunicorn==20.1.0 -y
pip install h11==0.14.0 || pip3 install h11==0.14.0 -y
pip install h5py==3.9.0 || pip3 install h5py==3.9.0 -y
pip install httplib2==0.22.0 || pip3 install httplib2==0.22.0 -y
pip install httptools==0.6.0 || pip3 install httptools==0.6.0 -y
pip install huggingface-hub==0.16.4 || pip3 install huggingface-hub==0.16.4 -y
pip install idna==2.10 || pip3 install idna==2.10 -y
pip install imageio==2.31.1 || pip3 install imageio==2.31.1 -y
pip install imageio-ffmpeg==0.4.8 || pip3 install imageio-ffmpeg==0.4.8 -y
pip install importlib==1.0.4 || pip3 install importlib==1.0.4 -y
pip install itsdangerous==2.1.2 || pip3 install itsdangerous==2.1.2 -y
pip install Jinja2==3.1.2 || pip3 install Jinja2==3.1.2 -y
pip install jmespath==1.0.1 || pip3 install jmespath==1.0.1 -y
pip install joblib==1.3.1 || pip3 install joblib==1.3.1 -y
pip install jsonpatch @ file:///tmp/build/80754af9/jsonpatch_1615747632069/work || pip3 install jsonpatch @ file:///tmp/build/80754af9/jsonpatch_1615747632069/work -y
pip install jsonpointer==2.1 || pip3 install jsonpointer==2.1 -y
pip install keras==2.13.1rc0 || pip3 install keras==2.13.1rc0 -y
pip install keyboard==0.13.5 || pip3 install keyboard==0.13.5 -y
pip install kiwisolver==1.4.4 || pip3 install kiwisolver==1.4.4 -y
pip install libclang==16.0.0 || pip3 install libclang==16.0.0 -y
pip install macholib==1.16.2 || pip3 install macholib==1.16.2 -y
pip install Markdown==3.4.3 || pip3 install Markdown==3.4.3 -y
pip install MarkupSafe==2.1.3 || pip3 install MarkupSafe==2.1.3 -y
pip install matplotlib==3.7.2 || pip3 install matplotlib==3.7.2 -y
pip install moviepy==1.0.3 || pip3 install moviepy==1.0.3 -y
pip install mpmath==1.3.0 || pip3 install mpmath==1.3.0 -y
pip install msgpack==1.0.5 || pip3 install msgpack==1.0.5 -y
pip install multidict==6.0.4 || pip3 install multidict==6.0.4 -y
pip install multiprocess==0.70.15 || pip3 install multiprocess==0.70.15 -y
pip install networkx==3.1 || pip3 install networkx==3.1 -y
pip install nltk==3.8.1 || pip3 install nltk==3.8.1 -y
pip install numpy==1.25.0 || pip3 install numpy==1.25.0 -y
pip install oauthlib==3.2.2 || pip3 install oauthlib==3.2.2 -y
pip install onnx==1.14.0 || pip3 install onnx==1.14.0 -y
pip install onnx-tf==1.10.0 || pip3 install onnx-tf==1.10.0 -y
pip install opencv-python==4.7.0.72 || pip3 install opencv-python==4.7.0.72 -y
pip install opencv-python-headless==4.8.0.76 || pip3 install opencv-python-headless==4.8.0.76 -y
pip install opt-einsum==3.3.0 || pip3 install opt-einsum==3.3.0 -y
pip install outcome==1.2.0 || pip3 install outcome==1.2.0 -y
pip install packaging==23.1 || pip3 install packaging==23.1 -y
pip install pafy==0.5.5 || pip3 install pafy==0.5.5 -y
pip install pandas==2.0.3 || pip3 install pandas==2.0.3 -y
pip install paramiko==3.3.1 || pip3 install paramiko==3.3.1 -y
pip install pathtools==0.1.2 || pip3 install pathtools==0.1.2 -y
pip install Pillow==9.5.0 || pip3 install Pillow==9.5.0 -y
pip install pluggy @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_croot-w6jyveby/pluggy_1648109277227/work || pip3 install pluggy @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_croot-w6jyveby/pluggy_1648109277227/work -y
pip install ply==3.11 || pip3 install ply==3.11 -y
pip install proglog==0.1.10 || pip3 install proglog==0.1.10 -y
pip install proto-plus==1.22.3 || pip3 install proto-plus==1.22.3 -y
pip install protobuf==4.23.3 || pip3 install protobuf==4.23.3 -y
pip install psutil==5.9.5 || pip3 install psutil==5.9.5 -y
pip install py-cpuinfo==9.0.0 || pip3 install py-cpuinfo==9.0.0 -y
pip install pyarrow==13.0.0 || pip3 install pyarrow==13.0.0 -y
pip install pyasn1==0.5.0 || pip3 install pyasn1==0.5.0 -y
pip install pyasn1-modules==0.3.0 || pip3 install pyasn1-modules==0.3.0 -y
pip install pybboxes==0.1.6 || pip3 install pybboxes==0.1.6 -y
pip install pycosat @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_e9xhel3kyj/croot/pycosat_1666805516297/work || pip3 install pycosat @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_e9xhel3kyj/croot/pycosat_1666805516297/work -y
pip install pycparser @ file:///tmp/build/80754af9/pycparser_1636541352034/work || pip3 install pycparser @ file:///tmp/build/80754af9/pycparser_1636541352034/work -y
pip install pydub==0.25.1 || pip3 install pydub==0.25.1 -y
pip install pygame==2.5.0 || pip3 install pygame==2.5.0 -y
pip install pyinstaller==5.13.0 || pip3 install pyinstaller==5.13.0 -y
pip install pyinstaller-hooks-contrib==2023.6 || pip3 install pyinstaller-hooks-contrib==2023.6 -y
pip install PyJWT==2.7.0 || pip3 install PyJWT==2.7.0 -y
pip install PyNaCl==1.5.0 || pip3 install PyNaCl==1.5.0 -y
pip install pynvml==11.5.0 || pip3 install pynvml==11.5.0 -y
pip install pyobjc==9.2 || pip3 install pyobjc==9.2 -y
pip install pyobjc-core==9.2 || pip3 install pyobjc-core==9.2 -y
pip install pyobjc-framework-Accessibility==9.2 || pip3 install pyobjc-framework-Accessibility==9.2 -y
pip install pyobjc-framework-Accounts==9.2 || pip3 install pyobjc-framework-Accounts==9.2 -y
pip install pyobjc-framework-AddressBook==9.2 || pip3 install pyobjc-framework-AddressBook==9.2 -y
pip install pyobjc-framework-AdServices==9.2 || pip3 install pyobjc-framework-AdServices==9.2 -y
pip install pyobjc-framework-AdSupport==9.2 || pip3 install pyobjc-framework-AdSupport==9.2 -y
pip install pyobjc-framework-AppleScriptKit==9.2 || pip3 install pyobjc-framework-AppleScriptKit==9.2 -y
pip install pyobjc-framework-AppleScriptObjC==9.2 || pip3 install pyobjc-framework-AppleScriptObjC==9.2 -y
pip install pyobjc-framework-ApplicationServices==9.2 || pip3 install pyobjc-framework-ApplicationServices==9.2 -y
pip install pyobjc-framework-AppTrackingTransparency==9.2 || pip3 install pyobjc-framework-AppTrackingTransparency==9.2 -y
pip install pyobjc-framework-AudioVideoBridging==9.2 || pip3 install pyobjc-framework-AudioVideoBridging==9.2 -y
pip install pyobjc-framework-AuthenticationServices==9.2 || pip3 install pyobjc-framework-AuthenticationServices==9.2 -y
pip install pyobjc-framework-AutomaticAssessmentConfiguration==9.2 || pip3 install pyobjc-framework-AutomaticAssessmentConfiguration==9.2 -y
pip install pyobjc-framework-Automator==9.2 || pip3 install pyobjc-framework-Automator==9.2 -y
pip install pyobjc-framework-AVFoundation==9.2 || pip3 install pyobjc-framework-AVFoundation==9.2 -y
pip install pyobjc-framework-AVKit==9.2 || pip3 install pyobjc-framework-AVKit==9.2 -y
pip install pyobjc-framework-AVRouting==9.2 || pip3 install pyobjc-framework-AVRouting==9.2 -y
pip install pyobjc-framework-BackgroundAssets==9.2 || pip3 install pyobjc-framework-BackgroundAssets==9.2 -y
pip install pyobjc-framework-BusinessChat==9.2 || pip3 install pyobjc-framework-BusinessChat==9.2 -y
pip install pyobjc-framework-CalendarStore==9.2 || pip3 install pyobjc-framework-CalendarStore==9.2 -y
pip install pyobjc-framework-CallKit==9.2 || pip3 install pyobjc-framework-CallKit==9.2 -y
pip install pyobjc-framework-CFNetwork==9.2 || pip3 install pyobjc-framework-CFNetwork==9.2 -y
pip install pyobjc-framework-ClassKit==9.2 || pip3 install pyobjc-framework-ClassKit==9.2 -y
pip install pyobjc-framework-CloudKit==9.2 || pip3 install pyobjc-framework-CloudKit==9.2 -y
pip install pyobjc-framework-Cocoa==9.2 || pip3 install pyobjc-framework-Cocoa==9.2 -y
pip install pyobjc-framework-Collaboration==9.2 || pip3 install pyobjc-framework-Collaboration==9.2 -y
pip install pyobjc-framework-ColorSync==9.2 || pip3 install pyobjc-framework-ColorSync==9.2 -y
pip install pyobjc-framework-Contacts==9.2 || pip3 install pyobjc-framework-Contacts==9.2 -y
pip install pyobjc-framework-ContactsUI==9.2 || pip3 install pyobjc-framework-ContactsUI==9.2 -y
pip install pyobjc-framework-CoreAudio==9.2 || pip3 install pyobjc-framework-CoreAudio==9.2 -y
pip install pyobjc-framework-CoreAudioKit==9.2 || pip3 install pyobjc-framework-CoreAudioKit==9.2 -y
pip install pyobjc-framework-CoreBluetooth==9.2 || pip3 install pyobjc-framework-CoreBluetooth==9.2 -y
pip install pyobjc-framework-CoreData==9.2 || pip3 install pyobjc-framework-CoreData==9.2 -y
pip install pyobjc-framework-CoreHaptics==9.2 || pip3 install pyobjc-framework-CoreHaptics==9.2 -y
pip install pyobjc-framework-CoreLocation==9.2 || pip3 install pyobjc-framework-CoreLocation==9.2 -y
pip install pyobjc-framework-CoreMedia==9.2 || pip3 install pyobjc-framework-CoreMedia==9.2 -y
pip install pyobjc-framework-CoreMediaIO==9.2 || pip3 install pyobjc-framework-CoreMediaIO==9.2 -y
pip install pyobjc-framework-CoreMIDI==9.2 || pip3 install pyobjc-framework-CoreMIDI==9.2 -y
pip install pyobjc-framework-CoreML==9.2 || pip3 install pyobjc-framework-CoreML==9.2 -y
pip install pyobjc-framework-CoreMotion==9.2 || pip3 install pyobjc-framework-CoreMotion==9.2 -y
pip install pyobjc-framework-CoreServices==9.2 || pip3 install pyobjc-framework-CoreServices==9.2 -y
pip install pyobjc-framework-CoreSpotlight==9.2 || pip3 install pyobjc-framework-CoreSpotlight==9.2 -y
pip install pyobjc-framework-CoreText==9.2 || pip3 install pyobjc-framework-CoreText==9.2 -y
pip install pyobjc-framework-CoreWLAN==9.2 || pip3 install pyobjc-framework-CoreWLAN==9.2 -y
pip install pyobjc-framework-CryptoTokenKit==9.2 || pip3 install pyobjc-framework-CryptoTokenKit==9.2 -y
pip install pyobjc-framework-DataDetection==9.2 || pip3 install pyobjc-framework-DataDetection==9.2 -y
pip install pyobjc-framework-DeviceCheck==9.2 || pip3 install pyobjc-framework-DeviceCheck==9.2 -y
pip install pyobjc-framework-DictionaryServices==9.2 || pip3 install pyobjc-framework-DictionaryServices==9.2 -y
pip install pyobjc-framework-DiscRecording==9.2 || pip3 install pyobjc-framework-DiscRecording==9.2 -y
pip install pyobjc-framework-DiscRecordingUI==9.2 || pip3 install pyobjc-framework-DiscRecordingUI==9.2 -y
pip install pyobjc-framework-DiskArbitration==9.2 || pip3 install pyobjc-framework-DiskArbitration==9.2 -y
pip install pyobjc-framework-DVDPlayback==9.2 || pip3 install pyobjc-framework-DVDPlayback==9.2 -y
pip install pyobjc-framework-EventKit==9.2 || pip3 install pyobjc-framework-EventKit==9.2 -y
pip install pyobjc-framework-ExceptionHandling==9.2 || pip3 install pyobjc-framework-ExceptionHandling==9.2 -y
pip install pyobjc-framework-ExecutionPolicy==9.2 || pip3 install pyobjc-framework-ExecutionPolicy==9.2 -y
pip install pyobjc-framework-ExtensionKit==9.2 || pip3 install pyobjc-framework-ExtensionKit==9.2 -y
pip install pyobjc-framework-ExternalAccessory==9.2 || pip3 install pyobjc-framework-ExternalAccessory==9.2 -y
pip install pyobjc-framework-FileProvider==9.2 || pip3 install pyobjc-framework-FileProvider==9.2 -y
pip install pyobjc-framework-FileProviderUI==9.2 || pip3 install pyobjc-framework-FileProviderUI==9.2 -y
pip install pyobjc-framework-FinderSync==9.2 || pip3 install pyobjc-framework-FinderSync==9.2 -y
pip install pyobjc-framework-FSEvents==9.2 || pip3 install pyobjc-framework-FSEvents==9.2 -y
pip install pyobjc-framework-GameCenter==9.2 || pip3 install pyobjc-framework-GameCenter==9.2 -y
pip install pyobjc-framework-GameController==9.2 || pip3 install pyobjc-framework-GameController==9.2 -y
pip install pyobjc-framework-GameKit==9.2 || pip3 install pyobjc-framework-GameKit==9.2 -y
pip install pyobjc-framework-GameplayKit==9.2 || pip3 install pyobjc-framework-GameplayKit==9.2 -y
pip install pyobjc-framework-HealthKit==9.2 || pip3 install pyobjc-framework-HealthKit==9.2 -y
pip install pyobjc-framework-ImageCaptureCore==9.2 || pip3 install pyobjc-framework-ImageCaptureCore==9.2 -y
pip install pyobjc-framework-IMServicePlugIn==9.2 || pip3 install pyobjc-framework-IMServicePlugIn==9.2 -y
pip install pyobjc-framework-InputMethodKit==9.2 || pip3 install pyobjc-framework-InputMethodKit==9.2 -y
pip install pyobjc-framework-InstallerPlugins==9.2 || pip3 install pyobjc-framework-InstallerPlugins==9.2 -y
pip install pyobjc-framework-InstantMessage==9.2 || pip3 install pyobjc-framework-InstantMessage==9.2 -y
pip install pyobjc-framework-Intents==9.2 || pip3 install pyobjc-framework-Intents==9.2 -y
pip install pyobjc-framework-IntentsUI==9.2 || pip3 install pyobjc-framework-IntentsUI==9.2 -y
pip install pyobjc-framework-IOBluetooth==9.2 || pip3 install pyobjc-framework-IOBluetooth==9.2 -y
pip install pyobjc-framework-IOBluetoothUI==9.2 || pip3 install pyobjc-framework-IOBluetoothUI==9.2 -y
pip install pyobjc-framework-IOSurface==9.2 || pip3 install pyobjc-framework-IOSurface==9.2 -y
pip install pyobjc-framework-iTunesLibrary==9.2 || pip3 install pyobjc-framework-iTunesLibrary==9.2 -y
pip install pyobjc-framework-KernelManagement==9.2 || pip3 install pyobjc-framework-KernelManagement==9.2 -y
pip install pyobjc-framework-LatentSemanticMapping==9.2 || pip3 install pyobjc-framework-LatentSemanticMapping==9.2 -y
pip install pyobjc-framework-LaunchServices==9.2 || pip3 install pyobjc-framework-LaunchServices==9.2 -y
pip install pyobjc-framework-libdispatch==9.2 || pip3 install pyobjc-framework-libdispatch==9.2 -y
pip install pyobjc-framework-libxpc==9.2 || pip3 install pyobjc-framework-libxpc==9.2 -y
pip install pyobjc-framework-LinkPresentation==9.2 || pip3 install pyobjc-framework-LinkPresentation==9.2 -y
pip install pyobjc-framework-LocalAuthentication==9.2 || pip3 install pyobjc-framework-LocalAuthentication==9.2 -y
pip install pyobjc-framework-LocalAuthenticationEmbeddedUI==9.2 || pip3 install pyobjc-framework-LocalAuthenticationEmbeddedUI==9.2 -y
pip install pyobjc-framework-MailKit==9.2 || pip3 install pyobjc-framework-MailKit==9.2 -y
pip install pyobjc-framework-MapKit==9.2 || pip3 install pyobjc-framework-MapKit==9.2 -y
pip install pyobjc-framework-MediaAccessibility==9.2 || pip3 install pyobjc-framework-MediaAccessibility==9.2 -y
pip install pyobjc-framework-MediaLibrary==9.2 || pip3 install pyobjc-framework-MediaLibrary==9.2 -y
pip install pyobjc-framework-MediaPlayer==9.2 || pip3 install pyobjc-framework-MediaPlayer==9.2 -y
pip install pyobjc-framework-MediaToolbox==9.2 || pip3 install pyobjc-framework-MediaToolbox==9.2 -y
pip install pyobjc-framework-Metal==9.2 || pip3 install pyobjc-framework-Metal==9.2 -y
pip install pyobjc-framework-MetalFX==9.2 || pip3 install pyobjc-framework-MetalFX==9.2 -y
pip install pyobjc-framework-MetalKit==9.2 || pip3 install pyobjc-framework-MetalKit==9.2 -y
pip install pyobjc-framework-MetalPerformanceShaders==9.2 || pip3 install pyobjc-framework-MetalPerformanceShaders==9.2 -y
pip install pyobjc-framework-MetalPerformanceShadersGraph==9.2 || pip3 install pyobjc-framework-MetalPerformanceShadersGraph==9.2 -y
pip install pyobjc-framework-MetricKit==9.2 || pip3 install pyobjc-framework-MetricKit==9.2 -y
pip install pyobjc-framework-MLCompute==9.2 || pip3 install pyobjc-framework-MLCompute==9.2 -y
pip install pyobjc-framework-ModelIO==9.2 || pip3 install pyobjc-framework-ModelIO==9.2 -y
pip install pyobjc-framework-MultipeerConnectivity==9.2 || pip3 install pyobjc-framework-MultipeerConnectivity==9.2 -y
pip install pyobjc-framework-NaturalLanguage==9.2 || pip3 install pyobjc-framework-NaturalLanguage==9.2 -y
pip install pyobjc-framework-NetFS==9.2 || pip3 install pyobjc-framework-NetFS==9.2 -y
pip install pyobjc-framework-Network==9.2 || pip3 install pyobjc-framework-Network==9.2 -y
pip install pyobjc-framework-NetworkExtension==9.2 || pip3 install pyobjc-framework-NetworkExtension==9.2 -y
pip install pyobjc-framework-NotificationCenter==9.2 || pip3 install pyobjc-framework-NotificationCenter==9.2 -y
pip install pyobjc-framework-OpenDirectory==9.2 || pip3 install pyobjc-framework-OpenDirectory==9.2 -y
pip install pyobjc-framework-OSAKit==9.2 || pip3 install pyobjc-framework-OSAKit==9.2 -y
pip install pyobjc-framework-OSLog==9.2 || pip3 install pyobjc-framework-OSLog==9.2 -y
pip install pyobjc-framework-PassKit==9.2 || pip3 install pyobjc-framework-PassKit==9.2 -y
pip install pyobjc-framework-PencilKit==9.2 || pip3 install pyobjc-framework-PencilKit==9.2 -y
pip install pyobjc-framework-PHASE==9.2 || pip3 install pyobjc-framework-PHASE==9.2 -y
pip install pyobjc-framework-Photos==9.2 || pip3 install pyobjc-framework-Photos==9.2 -y
pip install pyobjc-framework-PhotosUI==9.2 || pip3 install pyobjc-framework-PhotosUI==9.2 -y
pip install pyobjc-framework-PreferencePanes==9.2 || pip3 install pyobjc-framework-PreferencePanes==9.2 -y
pip install pyobjc-framework-PushKit==9.2 || pip3 install pyobjc-framework-PushKit==9.2 -y
pip install pyobjc-framework-Quartz==9.2 || pip3 install pyobjc-framework-Quartz==9.2 -y
pip install pyobjc-framework-QuickLookThumbnailing==9.2 || pip3 install pyobjc-framework-QuickLookThumbnailing==9.2 -y
pip install pyobjc-framework-ReplayKit==9.2 || pip3 install pyobjc-framework-ReplayKit==9.2 -y
pip install pyobjc-framework-SafariServices==9.2 || pip3 install pyobjc-framework-SafariServices==9.2 -y
pip install pyobjc-framework-SafetyKit==9.2 || pip3 install pyobjc-framework-SafetyKit==9.2 -y
pip install pyobjc-framework-SceneKit==9.2 || pip3 install pyobjc-framework-SceneKit==9.2 -y
pip install pyobjc-framework-ScreenCaptureKit==9.2 || pip3 install pyobjc-framework-ScreenCaptureKit==9.2 -y
pip install pyobjc-framework-ScreenSaver==9.2 || pip3 install pyobjc-framework-ScreenSaver==9.2 -y
pip install pyobjc-framework-ScreenTime==9.2 || pip3 install pyobjc-framework-ScreenTime==9.2 -y
pip install pyobjc-framework-ScriptingBridge==9.2 || pip3 install pyobjc-framework-ScriptingBridge==9.2 -y
pip install pyobjc-framework-SearchKit==9.2 || pip3 install pyobjc-framework-SearchKit==9.2 -y
pip install pyobjc-framework-Security==9.2 || pip3 install pyobjc-framework-Security==9.2 -y
pip install pyobjc-framework-SecurityFoundation==9.2 || pip3 install pyobjc-framework-SecurityFoundation==9.2 -y
pip install pyobjc-framework-SecurityInterface==9.2 || pip3 install pyobjc-framework-SecurityInterface==9.2 -y
pip install pyobjc-framework-ServiceManagement==9.2 || pip3 install pyobjc-framework-ServiceManagement==9.2 -y
pip install pyobjc-framework-SharedWithYou==9.2 || pip3 install pyobjc-framework-SharedWithYou==9.2 -y
pip install pyobjc-framework-SharedWithYouCore==9.2 || pip3 install pyobjc-framework-SharedWithYouCore==9.2 -y
pip install pyobjc-framework-ShazamKit==9.2 || pip3 install pyobjc-framework-ShazamKit==9.2 -y
pip install pyobjc-framework-Social==9.2 || pip3 install pyobjc-framework-Social==9.2 -y
pip install pyobjc-framework-SoundAnalysis==9.2 || pip3 install pyobjc-framework-SoundAnalysis==9.2 -y
pip install pyobjc-framework-Speech==9.2 || pip3 install pyobjc-framework-Speech==9.2 -y
pip install pyobjc-framework-SpriteKit==9.2 || pip3 install pyobjc-framework-SpriteKit==9.2 -y
pip install pyobjc-framework-StoreKit==9.2 || pip3 install pyobjc-framework-StoreKit==9.2 -y
pip install pyobjc-framework-SyncServices==9.2 || pip3 install pyobjc-framework-SyncServices==9.2 -y
pip install pyobjc-framework-SystemConfiguration==9.2 || pip3 install pyobjc-framework-SystemConfiguration==9.2 -y
pip install pyobjc-framework-SystemExtensions==9.2 || pip3 install pyobjc-framework-SystemExtensions==9.2 -y
pip install pyobjc-framework-ThreadNetwork==9.2 || pip3 install pyobjc-framework-ThreadNetwork==9.2 -y
pip install pyobjc-framework-UniformTypeIdentifiers==9.2 || pip3 install pyobjc-framework-UniformTypeIdentifiers==9.2 -y
pip install pyobjc-framework-UserNotifications==9.2 || pip3 install pyobjc-framework-UserNotifications==9.2 -y
pip install pyobjc-framework-UserNotificationsUI==9.2 || pip3 install pyobjc-framework-UserNotificationsUI==9.2 -y
pip install pyobjc-framework-VideoSubscriberAccount==9.2 || pip3 install pyobjc-framework-VideoSubscriberAccount==9.2 -y
pip install pyobjc-framework-VideoToolbox==9.2 || pip3 install pyobjc-framework-VideoToolbox==9.2 -y
pip install pyobjc-framework-Virtualization==9.2 || pip3 install pyobjc-framework-Virtualization==9.2 -y
pip install pyobjc-framework-Vision==9.2 || pip3 install pyobjc-framework-Vision==9.2 -y
pip install pyobjc-framework-WebKit==9.2 || pip3 install pyobjc-framework-WebKit==9.2 -y
pip install pyOpenSSL @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_38h4axtq38/croot/pyopenssl_1677607699670/work || pip3 install pyOpenSSL @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_38h4axtq38/croot/pyopenssl_1677607699670/work -y
pip install pyparsing==2.4.7 || pip3 install pyparsing==2.4.7 -y
pip install PyQt5-sip==12.11.0 || pip3 install PyQt5-sip==12.11.0 -y
pip install PySocks @ file:///Users/ktietz/ci_310/pysocks_1643961536721/work || pip3 install PySocks @ file:///Users/ktietz/ci_310/pysocks_1643961536721/work -y
pip install python-dateutil==2.8.2 || pip3 install python-dateutil==2.8.2 -y
pip install python-dotenv==1.0.0 || pip3 install python-dotenv==1.0.0 -y
pip install python-vlc==3.0.18122 || pip3 install python-vlc==3.0.18122 -y
pip install pytube==15.0.0 || pip3 install pytube==15.0.0 -y
pip install pytube3==9.6.4 || pip3 install pytube3==9.6.4 -y
pip install pytz==2023.3 || pip3 install pytz==2023.3 -y
pip install PyYAML==6.0 || pip3 install PyYAML==6.0 -y
pip install regex==2023.6.3 || pip3 install regex==2023.6.3 -y
pip install requests==2.31.0 || pip3 install requests==2.31.0 -y
pip install requests-oauthlib==1.3.1 || pip3 install requests-oauthlib==1.3.1 -y
pip install requests-toolbelt==1.0.0 || pip3 install requests-toolbelt==1.0.0 -y
pip install roboflow==1.1.2 || pip3 install roboflow==1.1.2 -y
pip install rsa==4.9 || pip3 install rsa==4.9 -y
pip install ruamel.yaml @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_aeh5mqcw49/croot/ruamel.yaml_1666304555976/work || pip3 install ruamel.yaml @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_aeh5mqcw49/croot/ruamel.yaml_1666304555976/work -y
pip install ruamel.yaml.clib @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_f64xdg2rww/croot/ruamel.yaml.clib_1666302244208/work || pip3 install ruamel.yaml.clib @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_f64xdg2rww/croot/ruamel.yaml.clib_1666302244208/work -y
pip install s3transfer==0.6.1 || pip3 install s3transfer==0.6.1 -y
pip install safetensors==0.3.1 || pip3 install safetensors==0.3.1 -y
pip install sahi==0.11.14 || pip3 install sahi==0.11.14 -y
pip install scikit-learn==1.3.0 || pip3 install scikit-learn==1.3.0 -y
pip install scipy==1.11.1 || pip3 install scipy==1.11.1 -y
pip install scp==0.14.5 || pip3 install scp==0.14.5 -y
pip install seaborn==0.12.2 || pip3 install seaborn==0.12.2 -y
pip install selenium==4.11.2 || pip3 install selenium==4.11.2 -y
pip install sentence-transformers==2.2.2 || pip3 install sentence-transformers==2.2.2 -y
pip install sentencepiece==0.1.99 || pip3 install sentencepiece==0.1.99 -y
pip install sentry-sdk==1.29.2 || pip3 install sentry-sdk==1.29.2 -y
pip install setproctitle==1.3.2 || pip3 install setproctitle==1.3.2 -y
pip install shapely==2.0.1 || pip3 install shapely==2.0.1 -y
pip install sip @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_fbqiv4bzwo/croots/recipe/sip_1659012372184/work || pip3 install sip @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_fbqiv4bzwo/croots/recipe/sip_1659012372184/work -y
pip install six @ file:///tmp/build/80754af9/six_1644875935023/work || pip3 install six @ file:///tmp/build/80754af9/six_1644875935023/work -y
pip install smmap==5.0.0 || pip3 install smmap==5.0.0 -y
pip install sniffio==1.3.0 || pip3 install sniffio==1.3.0 -y
pip install sortedcontainers==2.4.0 || pip3 install sortedcontainers==2.4.0 -y
pip install soupsieve==2.4.1 || pip3 install soupsieve==2.4.1 -y
pip install supervision==0.13.0 || pip3 install supervision==0.13.0 -y
pip install sympy==1.12 || pip3 install sympy==1.12 -y
pip install tensorboard==2.13.0 || pip3 install tensorboard==2.13.0 -y
pip install tensorboard-data-server==0.7.1 || pip3 install tensorboard-data-server==0.7.1 -y
pip install tensorboard-plugin-wit==1.8.1 || pip3 install tensorboard-plugin-wit==1.8.1 -y
pip install tensorflow==2.13.0rc1 || pip3 install tensorflow==2.13.0rc1 -y
pip install tensorflow-addons==0.21.0 || pip3 install tensorflow-addons==0.21.0 -y
pip install tensorflow-estimator==2.13.0rc0 || pip3 install tensorflow-estimator==2.13.0rc0 -y
pip install tensorflow-macos==2.13.0rc1 || pip3 install tensorflow-macos==2.13.0rc1 -y
pip install tensorflow-probability==0.21.0 || pip3 install tensorflow-probability==0.21.0 -y
pip install termcolor==2.3.0 || pip3 install termcolor==2.3.0 -y
pip install terminaltables==3.1.10 || pip3 install terminaltables==3.1.10 -y
pip install thop==0.1.1.post2209072238 || pip3 install thop==0.1.1.post2209072238 -y
pip install threadpoolctl==3.1.0 || pip3 install threadpoolctl==3.1.0 -y
pip install tiktoken==0.4.0 || pip3 install tiktoken==0.4.0 -y
pip install timm==0.9.5 || pip3 install timm==0.9.5 -y
pip install tk==0.1.0 || pip3 install tk==0.1.0 -y
pip install tokenizers==0.14.0 || pip3 install tokenizers==0.14.0 -y
pip install toml @ file:///tmp/build/80754af9/toml_1616166611790/work || pip3 install toml @ file:///tmp/build/80754af9/toml_1616166611790/work -y
pip install toolz @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_362wyqvvgy/croot/toolz_1667464079070/work || pip3 install toolz @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_362wyqvvgy/croot/toolz_1667464079070/work -y
pip install torch==2.0.1 || pip3 install torch==2.0.1 -y
pip install torchvision==0.15.2 || pip3 install torchvision==0.15.2 -y
pip install tqdm @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_ac7zic_tin/croot/tqdm_1679561870178/work || pip3 install tqdm @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_ac7zic_tin/croot/tqdm_1679561870178/work -y
pip install transformers @ git+https://github.com/huggingface/transformers.git@ab37b801b14d8b9c3186548e6e118aff623e6aa1 || pip3 install transformers @ git+https://github.com/huggingface/transformers.git@ab37b801b14d8b9c3186548e6e118aff623e6aa1 -y
pip install trio==0.22.1 || pip3 install trio==0.22.1 -y
pip install trio-websocket==0.10.3 || pip3 install trio-websocket==0.10.3 -y
pip install typeguard==2.13.3 || pip3 install typeguard==2.13.3 -y
pip install typing_extensions==4.5.0 || pip3 install typing_extensions==4.5.0 -y
pip install tzdata==2023.3 || pip3 install tzdata==2023.3 -y
pip install ultralytics==8.0.153 || pip3 install ultralytics==8.0.153 -y
pip install uritemplate==4.1.1 || pip3 install uritemplate==4.1.1 -y
pip install urllib3==1.26.16 || pip3 install urllib3==1.26.16 -y
pip install urllib3-secure-extra==0.1.0 || pip3 install urllib3-secure-extra==0.1.0 -y
pip install uvloop==0.17.0 || pip3 install uvloop==0.17.0 -y
pip install vastai==0.1.7 || pip3 install vastai==0.1.7 -y
pip install wandb==0.15.8 || pip3 install wandb==0.15.8 -y
pip install watchdog==3.0.0 || pip3 install watchdog==3.0.0 -y
pip install websockets==11.0.3 || pip3 install websockets==11.0.3 -y
pip install Werkzeug==2.3.6 || pip3 install Werkzeug==2.3.6 -y
pip install wget==3.2 || pip3 install wget==3.2 -y
pip install wrapt==1.15.0 || pip3 install wrapt==1.15.0 -y
pip install wsproto==1.2.0 || pip3 install wsproto==1.2.0 -y
pip install xxhash==3.3.0 || pip3 install xxhash==3.3.0 -y
pip install yarl==1.9.2 || pip3 install yarl==1.9.2 -y
pip install yolov5==7.0.12 || pip3 install yolov5==7.0.12 -y
pip install youtube-dl @ git+https://github.com/ytdl-org/youtube-dl.git@66ab0814c4baa2dc79c2dd5287bc0ad61a37c5b9 || pip3 install youtube-dl @ git+https://github.com/ytdl-org/youtube-dl.git@66ab0814c4baa2dc79c2dd5287bc0ad61a37c5b9 -y
pip install zope.interface==6.0 || pip3 install zope.interface==6.0 -y
pip install zstandard @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_41b3vxtask/croot/zstandard_1677013668452/work || pip3 install zstandard @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_41b3vxtask/croot/zstandard_1677013668452/work -y
pip install  || pip3 install  -y
idk
