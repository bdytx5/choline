#!/bin/bash
# Download Miniconda installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
# Install Miniconda
bash miniconda.sh -b -p $HOME/miniconda
# Initialize conda
source $HOME/miniconda/bin/activate
conda init
# Create environment
conda create --name choline python=3.10.10 -y
# Activate environment
conda activate choline
conda install absl-py==1.4.0 -y || pip install absl-py==1.4.0
conda install accelerate==0.23.0 -y || pip install accelerate==0.23.0
conda install aiohttp==3.8.5 -y || pip install aiohttp==3.8.5
conda install aiosignal==1.3.1 -y || pip install aiosignal==1.3.1
conda install altgraph==0.17.3 -y || pip install altgraph==0.17.3
conda install appdirs==1.4.4 -y || pip install appdirs==1.4.4
conda install astunparse==1.6.3 -y || pip install astunparse==1.6.3
conda install async-timeout==4.0.3 -y || pip install async-timeout==4.0.3
conda install attrs==23.1.0 -y || pip install attrs==23.1.0
conda install awsgi==0.0.5 -y || pip install awsgi==0.0.5
conda install banana-cli==0.0.15 -y || pip install banana-cli==0.0.15
conda install bcrypt==4.0.1 -y || pip install bcrypt==4.0.1
conda install beautifulsoup4==4.12.2 -y || pip install beautifulsoup4==4.12.2
conda install blinker==1.6.2 -y || pip install blinker==1.6.2
conda install boltons @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_f63n9uulmp/croot/boltons_1677628710094/work -y || pip install boltons @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_f63n9uulmp/croot/boltons_1677628710094/work
conda install boto3==1.28.25 -y || pip install boto3==1.28.25
conda install botocore==1.31.25 -y || pip install botocore==1.31.25
conda install brotlipy==0.7.0 -y || pip install brotlipy==0.7.0
conda install bs4==0.0.1 -y || pip install bs4==0.0.1
conda install CacheControl==0.13.1 -y || pip install CacheControl==0.13.1
conda install cachetools==5.3.1 -y || pip install cachetools==5.3.1
conda install certifi==2022.12.7 -y || pip install certifi==2022.12.7
conda install cffi @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_ab19r4bji3/croot/cffi_1670423206034/work -y || pip install cffi @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_ab19r4bji3/croot/cffi_1670423206034/work
conda install chardet==4.0.0 -y || pip install chardet==4.0.0
conda install charset-normalizer==3.1.0 -y || pip install charset-normalizer==3.1.0
conda install click==8.1.3 -y || pip install click==8.1.3
conda install cloudevents==1.9.0 -y || pip install cloudevents==1.9.0
conda install cloudpickle==2.2.1 -y || pip install cloudpickle==2.2.1
conda install conda @ file:///private/var/folders/k1/30mswbxs7r1g6zwn8y4fyt500000gp/T/abs_3ehd9hpsix/croot/conda_1690494984812/work -y || pip install conda @ file:///private/var/folders/k1/30mswbxs7r1g6zwn8y4fyt500000gp/T/abs_3ehd9hpsix/croot/conda_1690494984812/work
conda install conda-content-trust @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_11146a2b-93c2-444c-a378-ad4fac363e991s0r1hnp/croots/recipe/conda-content-trust_1658126383571/work -y || pip install conda-content-trust @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_11146a2b-93c2-444c-a378-ad4fac363e991s0r1hnp/croots/recipe/conda-content-trust_1658126383571/work
conda install conda-package-handling @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_5f3f459f9v/croot/conda-package-handling_1672865025324/work -y || pip install conda-package-handling @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_5f3f459f9v/croot/conda-package-handling_1672865025324/work
conda install conda_package_streaming @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_58gpsa_6af/croot/conda-package-streaming_1670508144037/work -y || pip install conda_package_streaming @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_58gpsa_6af/croot/conda-package-streaming_1670508144037/work
conda install contourpy==1.1.0 -y || pip install contourpy==1.1.0
conda install cryptography @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_a9zjqvif1f/croot/cryptography_1677533099634/work -y || pip install cryptography @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_a9zjqvif1f/croot/cryptography_1677533099634/work
conda install cycler==0.10.0 -y || pip install cycler==0.10.0
conda install datasets==2.14.5 -y || pip install datasets==2.14.5
conda install DateTime==5.1 -y || pip install DateTime==5.1
conda install decorator==4.4.2 -y || pip install decorator==4.4.2
conda install deprecation==2.1.0 -y || pip install deprecation==2.1.0
conda install dill==0.3.7 -y || pip install dill==0.3.7
conda install dm-tree==0.1.8 -y || pip install dm-tree==0.1.8
conda install docker-pycreds==0.4.0 -y || pip install docker-pycreds==0.4.0
conda install exceptiongroup==1.1.2 -y || pip install exceptiongroup==1.1.2
conda install filelock==3.12.2 -y || pip install filelock==3.12.2
conda install fire==0.5.0 -y || pip install fire==0.5.0
conda install firebase==4.0.1 -y || pip install firebase==4.0.1
conda install firebase-admin==6.2.0 -y || pip install firebase-admin==6.2.0
conda install firebase-functions==0.1.1 -y || pip install firebase-functions==0.1.1
conda install Flask==2.3.2 -y || pip install Flask==2.3.2
conda install Flask-Cors==4.0.0 -y || pip install Flask-Cors==4.0.0
conda install flatbuffers==23.5.26 -y || pip install flatbuffers==23.5.26
conda install fonttools==4.40.0 -y || pip install fonttools==4.40.0
conda install frozenlist==1.4.0 -y || pip install frozenlist==1.4.0
conda install fsspec==2023.6.0 -y || pip install fsspec==2023.6.0
conda install functions-framework==3.4.0 -y || pip install functions-framework==3.4.0
conda install gast==0.4.0 -y || pip install gast==0.4.0
conda install gitdb==4.0.10 -y || pip install gitdb==4.0.10
conda install GitPython==3.1.31 -y || pip install GitPython==3.1.31
conda install google-api-core==2.11.1 -y || pip install google-api-core==2.11.1
conda install google-api-python-client==2.93.0 -y || pip install google-api-python-client==2.93.0
conda install google-auth==2.21.0 -y || pip install google-auth==2.21.0
conda install google-auth-httplib2==0.1.0 -y || pip install google-auth-httplib2==0.1.0
conda install google-auth-oauthlib==1.0.0 -y || pip install google-auth-oauthlib==1.0.0
conda install google-cloud-core==2.3.2 -y || pip install google-cloud-core==2.3.2
conda install google-cloud-firestore==2.11.1 -y || pip install google-cloud-firestore==2.11.1
conda install google-cloud-storage==2.10.0 -y || pip install google-cloud-storage==2.10.0
conda install google-cloud-texttospeech==2.14.1 -y || pip install google-cloud-texttospeech==2.14.1
conda install google-crc32c==1.5.0 -y || pip install google-crc32c==1.5.0
conda install google-events==0.9.0 -y || pip install google-events==0.9.0
conda install google-pasta==0.2.0 -y || pip install google-pasta==0.2.0
conda install google-resumable-media==2.5.0 -y || pip install google-resumable-media==2.5.0
conda install googleapis-common-protos==1.59.1 -y || pip install googleapis-common-protos==1.59.1
conda install gpt3-package @ file:///Users/brettyoung/Desktop/dev/py_prjs/gpt3/gpt3_package/dist/gpt3_package-0.1.tar.gz#sha256=080cca69cbdf70f56b0871a599b9d9adaa974c5e9735411bce88f128de0ea7fb -y || pip install gpt3-package @ file:///Users/brettyoung/Desktop/dev/py_prjs/gpt3/gpt3_package/dist/gpt3_package-0.1.tar.gz#sha256=080cca69cbdf70f56b0871a599b9d9adaa974c5e9735411bce88f128de0ea7fb
conda install gpt4all==0.3.6 -y || pip install gpt4all==0.3.6
conda install grpcio==1.56.0 -y || pip install grpcio==1.56.0
conda install grpcio-status==1.56.0 -y || pip install grpcio-status==1.56.0
conda install gunicorn==20.1.0 -y || pip install gunicorn==20.1.0
conda install h11==0.14.0 -y || pip install h11==0.14.0
conda install h5py==3.9.0 -y || pip install h5py==3.9.0
conda install httplib2==0.22.0 -y || pip install httplib2==0.22.0
conda install httptools==0.6.0 -y || pip install httptools==0.6.0
conda install huggingface-hub==0.15.1 -y || pip install huggingface-hub==0.15.1
conda install idna==2.10 -y || pip install idna==2.10
conda install imageio==2.31.1 -y || pip install imageio==2.31.1
conda install imageio-ffmpeg==0.4.8 -y || pip install imageio-ffmpeg==0.4.8
conda install importlib==1.0.4 -y || pip install importlib==1.0.4
conda install itsdangerous==2.1.2 -y || pip install itsdangerous==2.1.2
conda install Jinja2==3.1.2 -y || pip install Jinja2==3.1.2
conda install jmespath==1.0.1 -y || pip install jmespath==1.0.1
conda install joblib==1.3.1 -y || pip install joblib==1.3.1
conda install jsonpatch @ file:///tmp/build/80754af9/jsonpatch_1615747632069/work -y || pip install jsonpatch @ file:///tmp/build/80754af9/jsonpatch_1615747632069/work
conda install jsonpointer==2.1 -y || pip install jsonpointer==2.1
conda install keras==2.13.1rc0 -y || pip install keras==2.13.1rc0
conda install keyboard==0.13.5 -y || pip install keyboard==0.13.5
conda install kiwisolver==1.4.4 -y || pip install kiwisolver==1.4.4
conda install libclang==16.0.0 -y || pip install libclang==16.0.0
conda install macholib==1.16.2 -y || pip install macholib==1.16.2
conda install Markdown==3.4.3 -y || pip install Markdown==3.4.3
conda install MarkupSafe==2.1.3 -y || pip install MarkupSafe==2.1.3
conda install matplotlib==3.7.2 -y || pip install matplotlib==3.7.2
conda install moviepy==1.0.3 -y || pip install moviepy==1.0.3
conda install mpmath==1.3.0 -y || pip install mpmath==1.3.0
conda install msgpack==1.0.5 -y || pip install msgpack==1.0.5
conda install multidict==6.0.4 -y || pip install multidict==6.0.4
conda install multiprocess==0.70.15 -y || pip install multiprocess==0.70.15
conda install networkx==3.1 -y || pip install networkx==3.1
conda install nltk==3.8.1 -y || pip install nltk==3.8.1
conda install numpy==1.25.0 -y || pip install numpy==1.25.0
conda install oauthlib==3.2.2 -y || pip install oauthlib==3.2.2
conda install onnx==1.14.0 -y || pip install onnx==1.14.0
conda install onnx-tf==1.10.0 -y || pip install onnx-tf==1.10.0
conda install opencv-python==4.7.0.72 -y || pip install opencv-python==4.7.0.72
conda install opencv-python-headless==4.8.0.76 -y || pip install opencv-python-headless==4.8.0.76
conda install opt-einsum==3.3.0 -y || pip install opt-einsum==3.3.0
conda install outcome==1.2.0 -y || pip install outcome==1.2.0
conda install packaging==23.1 -y || pip install packaging==23.1
conda install pafy==0.5.5 -y || pip install pafy==0.5.5
conda install pandas==2.0.3 -y || pip install pandas==2.0.3
conda install paramiko==3.3.1 -y || pip install paramiko==3.3.1
conda install pathtools==0.1.2 -y || pip install pathtools==0.1.2
conda install Pillow==9.5.0 -y || pip install Pillow==9.5.0
conda install pluggy @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_croot-w6jyveby/pluggy_1648109277227/work -y || pip install pluggy @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_croot-w6jyveby/pluggy_1648109277227/work
conda install ply==3.11 -y || pip install ply==3.11
conda install proglog==0.1.10 -y || pip install proglog==0.1.10
conda install proto-plus==1.22.3 -y || pip install proto-plus==1.22.3
conda install protobuf==4.23.3 -y || pip install protobuf==4.23.3
conda install psutil==5.9.5 -y || pip install psutil==5.9.5
conda install py-cpuinfo==9.0.0 -y || pip install py-cpuinfo==9.0.0
conda install pyarrow==13.0.0 -y || pip install pyarrow==13.0.0
conda install pyasn1==0.5.0 -y || pip install pyasn1==0.5.0
conda install pyasn1-modules==0.3.0 -y || pip install pyasn1-modules==0.3.0
conda install pybboxes==0.1.6 -y || pip install pybboxes==0.1.6
conda install pycosat @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_e9xhel3kyj/croot/pycosat_1666805516297/work -y || pip install pycosat @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_e9xhel3kyj/croot/pycosat_1666805516297/work
conda install pycparser @ file:///tmp/build/80754af9/pycparser_1636541352034/work -y || pip install pycparser @ file:///tmp/build/80754af9/pycparser_1636541352034/work
conda install pydub==0.25.1 -y || pip install pydub==0.25.1
conda install pygame==2.5.0 -y || pip install pygame==2.5.0
conda install pyinstaller==5.13.0 -y || pip install pyinstaller==5.13.0
conda install pyinstaller-hooks-contrib==2023.6 -y || pip install pyinstaller-hooks-contrib==2023.6
conda install PyJWT==2.7.0 -y || pip install PyJWT==2.7.0
conda install PyNaCl==1.5.0 -y || pip install PyNaCl==1.5.0
conda install pyobjc==9.2 -y || pip install pyobjc==9.2
conda install pyobjc-core==9.2 -y || pip install pyobjc-core==9.2
conda install pyobjc-framework-Accessibility==9.2 -y || pip install pyobjc-framework-Accessibility==9.2
conda install pyobjc-framework-Accounts==9.2 -y || pip install pyobjc-framework-Accounts==9.2
conda install pyobjc-framework-AddressBook==9.2 -y || pip install pyobjc-framework-AddressBook==9.2
conda install pyobjc-framework-AdServices==9.2 -y || pip install pyobjc-framework-AdServices==9.2
conda install pyobjc-framework-AdSupport==9.2 -y || pip install pyobjc-framework-AdSupport==9.2
conda install pyobjc-framework-AppleScriptKit==9.2 -y || pip install pyobjc-framework-AppleScriptKit==9.2
conda install pyobjc-framework-AppleScriptObjC==9.2 -y || pip install pyobjc-framework-AppleScriptObjC==9.2
conda install pyobjc-framework-ApplicationServices==9.2 -y || pip install pyobjc-framework-ApplicationServices==9.2
conda install pyobjc-framework-AppTrackingTransparency==9.2 -y || pip install pyobjc-framework-AppTrackingTransparency==9.2
conda install pyobjc-framework-AudioVideoBridging==9.2 -y || pip install pyobjc-framework-AudioVideoBridging==9.2
conda install pyobjc-framework-AuthenticationServices==9.2 -y || pip install pyobjc-framework-AuthenticationServices==9.2
conda install pyobjc-framework-AutomaticAssessmentConfiguration==9.2 -y || pip install pyobjc-framework-AutomaticAssessmentConfiguration==9.2
conda install pyobjc-framework-Automator==9.2 -y || pip install pyobjc-framework-Automator==9.2
conda install pyobjc-framework-AVFoundation==9.2 -y || pip install pyobjc-framework-AVFoundation==9.2
conda install pyobjc-framework-AVKit==9.2 -y || pip install pyobjc-framework-AVKit==9.2
conda install pyobjc-framework-AVRouting==9.2 -y || pip install pyobjc-framework-AVRouting==9.2
conda install pyobjc-framework-BackgroundAssets==9.2 -y || pip install pyobjc-framework-BackgroundAssets==9.2
conda install pyobjc-framework-BusinessChat==9.2 -y || pip install pyobjc-framework-BusinessChat==9.2
conda install pyobjc-framework-CalendarStore==9.2 -y || pip install pyobjc-framework-CalendarStore==9.2
conda install pyobjc-framework-CallKit==9.2 -y || pip install pyobjc-framework-CallKit==9.2
conda install pyobjc-framework-CFNetwork==9.2 -y || pip install pyobjc-framework-CFNetwork==9.2
conda install pyobjc-framework-ClassKit==9.2 -y || pip install pyobjc-framework-ClassKit==9.2
conda install pyobjc-framework-CloudKit==9.2 -y || pip install pyobjc-framework-CloudKit==9.2
conda install pyobjc-framework-Cocoa==9.2 -y || pip install pyobjc-framework-Cocoa==9.2
conda install pyobjc-framework-Collaboration==9.2 -y || pip install pyobjc-framework-Collaboration==9.2
conda install pyobjc-framework-ColorSync==9.2 -y || pip install pyobjc-framework-ColorSync==9.2
conda install pyobjc-framework-Contacts==9.2 -y || pip install pyobjc-framework-Contacts==9.2
conda install pyobjc-framework-ContactsUI==9.2 -y || pip install pyobjc-framework-ContactsUI==9.2
conda install pyobjc-framework-CoreAudio==9.2 -y || pip install pyobjc-framework-CoreAudio==9.2
conda install pyobjc-framework-CoreAudioKit==9.2 -y || pip install pyobjc-framework-CoreAudioKit==9.2
conda install pyobjc-framework-CoreBluetooth==9.2 -y || pip install pyobjc-framework-CoreBluetooth==9.2
conda install pyobjc-framework-CoreData==9.2 -y || pip install pyobjc-framework-CoreData==9.2
conda install pyobjc-framework-CoreHaptics==9.2 -y || pip install pyobjc-framework-CoreHaptics==9.2
conda install pyobjc-framework-CoreLocation==9.2 -y || pip install pyobjc-framework-CoreLocation==9.2
conda install pyobjc-framework-CoreMedia==9.2 -y || pip install pyobjc-framework-CoreMedia==9.2
conda install pyobjc-framework-CoreMediaIO==9.2 -y || pip install pyobjc-framework-CoreMediaIO==9.2
conda install pyobjc-framework-CoreMIDI==9.2 -y || pip install pyobjc-framework-CoreMIDI==9.2
conda install pyobjc-framework-CoreML==9.2 -y || pip install pyobjc-framework-CoreML==9.2
conda install pyobjc-framework-CoreMotion==9.2 -y || pip install pyobjc-framework-CoreMotion==9.2
conda install pyobjc-framework-CoreServices==9.2 -y || pip install pyobjc-framework-CoreServices==9.2
conda install pyobjc-framework-CoreSpotlight==9.2 -y || pip install pyobjc-framework-CoreSpotlight==9.2
conda install pyobjc-framework-CoreText==9.2 -y || pip install pyobjc-framework-CoreText==9.2
conda install pyobjc-framework-CoreWLAN==9.2 -y || pip install pyobjc-framework-CoreWLAN==9.2
conda install pyobjc-framework-CryptoTokenKit==9.2 -y || pip install pyobjc-framework-CryptoTokenKit==9.2
conda install pyobjc-framework-DataDetection==9.2 -y || pip install pyobjc-framework-DataDetection==9.2
conda install pyobjc-framework-DeviceCheck==9.2 -y || pip install pyobjc-framework-DeviceCheck==9.2
conda install pyobjc-framework-DictionaryServices==9.2 -y || pip install pyobjc-framework-DictionaryServices==9.2
conda install pyobjc-framework-DiscRecording==9.2 -y || pip install pyobjc-framework-DiscRecording==9.2
conda install pyobjc-framework-DiscRecordingUI==9.2 -y || pip install pyobjc-framework-DiscRecordingUI==9.2
conda install pyobjc-framework-DiskArbitration==9.2 -y || pip install pyobjc-framework-DiskArbitration==9.2
conda install pyobjc-framework-DVDPlayback==9.2 -y || pip install pyobjc-framework-DVDPlayback==9.2
conda install pyobjc-framework-EventKit==9.2 -y || pip install pyobjc-framework-EventKit==9.2
conda install pyobjc-framework-ExceptionHandling==9.2 -y || pip install pyobjc-framework-ExceptionHandling==9.2
conda install pyobjc-framework-ExecutionPolicy==9.2 -y || pip install pyobjc-framework-ExecutionPolicy==9.2
conda install pyobjc-framework-ExtensionKit==9.2 -y || pip install pyobjc-framework-ExtensionKit==9.2
conda install pyobjc-framework-ExternalAccessory==9.2 -y || pip install pyobjc-framework-ExternalAccessory==9.2
conda install pyobjc-framework-FileProvider==9.2 -y || pip install pyobjc-framework-FileProvider==9.2
conda install pyobjc-framework-FileProviderUI==9.2 -y || pip install pyobjc-framework-FileProviderUI==9.2
conda install pyobjc-framework-FinderSync==9.2 -y || pip install pyobjc-framework-FinderSync==9.2
conda install pyobjc-framework-FSEvents==9.2 -y || pip install pyobjc-framework-FSEvents==9.2
conda install pyobjc-framework-GameCenter==9.2 -y || pip install pyobjc-framework-GameCenter==9.2
conda install pyobjc-framework-GameController==9.2 -y || pip install pyobjc-framework-GameController==9.2
conda install pyobjc-framework-GameKit==9.2 -y || pip install pyobjc-framework-GameKit==9.2
conda install pyobjc-framework-GameplayKit==9.2 -y || pip install pyobjc-framework-GameplayKit==9.2
conda install pyobjc-framework-HealthKit==9.2 -y || pip install pyobjc-framework-HealthKit==9.2
conda install pyobjc-framework-ImageCaptureCore==9.2 -y || pip install pyobjc-framework-ImageCaptureCore==9.2
conda install pyobjc-framework-IMServicePlugIn==9.2 -y || pip install pyobjc-framework-IMServicePlugIn==9.2
conda install pyobjc-framework-InputMethodKit==9.2 -y || pip install pyobjc-framework-InputMethodKit==9.2
conda install pyobjc-framework-InstallerPlugins==9.2 -y || pip install pyobjc-framework-InstallerPlugins==9.2
conda install pyobjc-framework-InstantMessage==9.2 -y || pip install pyobjc-framework-InstantMessage==9.2
conda install pyobjc-framework-Intents==9.2 -y || pip install pyobjc-framework-Intents==9.2
conda install pyobjc-framework-IntentsUI==9.2 -y || pip install pyobjc-framework-IntentsUI==9.2
conda install pyobjc-framework-IOBluetooth==9.2 -y || pip install pyobjc-framework-IOBluetooth==9.2
conda install pyobjc-framework-IOBluetoothUI==9.2 -y || pip install pyobjc-framework-IOBluetoothUI==9.2
conda install pyobjc-framework-IOSurface==9.2 -y || pip install pyobjc-framework-IOSurface==9.2
conda install pyobjc-framework-iTunesLibrary==9.2 -y || pip install pyobjc-framework-iTunesLibrary==9.2
conda install pyobjc-framework-KernelManagement==9.2 -y || pip install pyobjc-framework-KernelManagement==9.2
conda install pyobjc-framework-LatentSemanticMapping==9.2 -y || pip install pyobjc-framework-LatentSemanticMapping==9.2
conda install pyobjc-framework-LaunchServices==9.2 -y || pip install pyobjc-framework-LaunchServices==9.2
conda install pyobjc-framework-libdispatch==9.2 -y || pip install pyobjc-framework-libdispatch==9.2
conda install pyobjc-framework-libxpc==9.2 -y || pip install pyobjc-framework-libxpc==9.2
conda install pyobjc-framework-LinkPresentation==9.2 -y || pip install pyobjc-framework-LinkPresentation==9.2
conda install pyobjc-framework-LocalAuthentication==9.2 -y || pip install pyobjc-framework-LocalAuthentication==9.2
conda install pyobjc-framework-LocalAuthenticationEmbeddedUI==9.2 -y || pip install pyobjc-framework-LocalAuthenticationEmbeddedUI==9.2
conda install pyobjc-framework-MailKit==9.2 -y || pip install pyobjc-framework-MailKit==9.2
conda install pyobjc-framework-MapKit==9.2 -y || pip install pyobjc-framework-MapKit==9.2
conda install pyobjc-framework-MediaAccessibility==9.2 -y || pip install pyobjc-framework-MediaAccessibility==9.2
conda install pyobjc-framework-MediaLibrary==9.2 -y || pip install pyobjc-framework-MediaLibrary==9.2
conda install pyobjc-framework-MediaPlayer==9.2 -y || pip install pyobjc-framework-MediaPlayer==9.2
conda install pyobjc-framework-MediaToolbox==9.2 -y || pip install pyobjc-framework-MediaToolbox==9.2
conda install pyobjc-framework-Metal==9.2 -y || pip install pyobjc-framework-Metal==9.2
conda install pyobjc-framework-MetalFX==9.2 -y || pip install pyobjc-framework-MetalFX==9.2
conda install pyobjc-framework-MetalKit==9.2 -y || pip install pyobjc-framework-MetalKit==9.2
conda install pyobjc-framework-MetalPerformanceShaders==9.2 -y || pip install pyobjc-framework-MetalPerformanceShaders==9.2
conda install pyobjc-framework-MetalPerformanceShadersGraph==9.2 -y || pip install pyobjc-framework-MetalPerformanceShadersGraph==9.2
conda install pyobjc-framework-MetricKit==9.2 -y || pip install pyobjc-framework-MetricKit==9.2
conda install pyobjc-framework-MLCompute==9.2 -y || pip install pyobjc-framework-MLCompute==9.2
conda install pyobjc-framework-ModelIO==9.2 -y || pip install pyobjc-framework-ModelIO==9.2
conda install pyobjc-framework-MultipeerConnectivity==9.2 -y || pip install pyobjc-framework-MultipeerConnectivity==9.2
conda install pyobjc-framework-NaturalLanguage==9.2 -y || pip install pyobjc-framework-NaturalLanguage==9.2
conda install pyobjc-framework-NetFS==9.2 -y || pip install pyobjc-framework-NetFS==9.2
conda install pyobjc-framework-Network==9.2 -y || pip install pyobjc-framework-Network==9.2
conda install pyobjc-framework-NetworkExtension==9.2 -y || pip install pyobjc-framework-NetworkExtension==9.2
conda install pyobjc-framework-NotificationCenter==9.2 -y || pip install pyobjc-framework-NotificationCenter==9.2
conda install pyobjc-framework-OpenDirectory==9.2 -y || pip install pyobjc-framework-OpenDirectory==9.2
conda install pyobjc-framework-OSAKit==9.2 -y || pip install pyobjc-framework-OSAKit==9.2
conda install pyobjc-framework-OSLog==9.2 -y || pip install pyobjc-framework-OSLog==9.2
conda install pyobjc-framework-PassKit==9.2 -y || pip install pyobjc-framework-PassKit==9.2
conda install pyobjc-framework-PencilKit==9.2 -y || pip install pyobjc-framework-PencilKit==9.2
conda install pyobjc-framework-PHASE==9.2 -y || pip install pyobjc-framework-PHASE==9.2
conda install pyobjc-framework-Photos==9.2 -y || pip install pyobjc-framework-Photos==9.2
conda install pyobjc-framework-PhotosUI==9.2 -y || pip install pyobjc-framework-PhotosUI==9.2
conda install pyobjc-framework-PreferencePanes==9.2 -y || pip install pyobjc-framework-PreferencePanes==9.2
conda install pyobjc-framework-PushKit==9.2 -y || pip install pyobjc-framework-PushKit==9.2
conda install pyobjc-framework-Quartz==9.2 -y || pip install pyobjc-framework-Quartz==9.2
conda install pyobjc-framework-QuickLookThumbnailing==9.2 -y || pip install pyobjc-framework-QuickLookThumbnailing==9.2
conda install pyobjc-framework-ReplayKit==9.2 -y || pip install pyobjc-framework-ReplayKit==9.2
conda install pyobjc-framework-SafariServices==9.2 -y || pip install pyobjc-framework-SafariServices==9.2
conda install pyobjc-framework-SafetyKit==9.2 -y || pip install pyobjc-framework-SafetyKit==9.2
conda install pyobjc-framework-SceneKit==9.2 -y || pip install pyobjc-framework-SceneKit==9.2
conda install pyobjc-framework-ScreenCaptureKit==9.2 -y || pip install pyobjc-framework-ScreenCaptureKit==9.2
conda install pyobjc-framework-ScreenSaver==9.2 -y || pip install pyobjc-framework-ScreenSaver==9.2
conda install pyobjc-framework-ScreenTime==9.2 -y || pip install pyobjc-framework-ScreenTime==9.2
conda install pyobjc-framework-ScriptingBridge==9.2 -y || pip install pyobjc-framework-ScriptingBridge==9.2
conda install pyobjc-framework-SearchKit==9.2 -y || pip install pyobjc-framework-SearchKit==9.2
conda install pyobjc-framework-Security==9.2 -y || pip install pyobjc-framework-Security==9.2
conda install pyobjc-framework-SecurityFoundation==9.2 -y || pip install pyobjc-framework-SecurityFoundation==9.2
conda install pyobjc-framework-SecurityInterface==9.2 -y || pip install pyobjc-framework-SecurityInterface==9.2
conda install pyobjc-framework-ServiceManagement==9.2 -y || pip install pyobjc-framework-ServiceManagement==9.2
conda install pyobjc-framework-SharedWithYou==9.2 -y || pip install pyobjc-framework-SharedWithYou==9.2
conda install pyobjc-framework-SharedWithYouCore==9.2 -y || pip install pyobjc-framework-SharedWithYouCore==9.2
conda install pyobjc-framework-ShazamKit==9.2 -y || pip install pyobjc-framework-ShazamKit==9.2
conda install pyobjc-framework-Social==9.2 -y || pip install pyobjc-framework-Social==9.2
conda install pyobjc-framework-SoundAnalysis==9.2 -y || pip install pyobjc-framework-SoundAnalysis==9.2
conda install pyobjc-framework-Speech==9.2 -y || pip install pyobjc-framework-Speech==9.2
conda install pyobjc-framework-SpriteKit==9.2 -y || pip install pyobjc-framework-SpriteKit==9.2
conda install pyobjc-framework-StoreKit==9.2 -y || pip install pyobjc-framework-StoreKit==9.2
conda install pyobjc-framework-SyncServices==9.2 -y || pip install pyobjc-framework-SyncServices==9.2
conda install pyobjc-framework-SystemConfiguration==9.2 -y || pip install pyobjc-framework-SystemConfiguration==9.2
conda install pyobjc-framework-SystemExtensions==9.2 -y || pip install pyobjc-framework-SystemExtensions==9.2
conda install pyobjc-framework-ThreadNetwork==9.2 -y || pip install pyobjc-framework-ThreadNetwork==9.2
conda install pyobjc-framework-UniformTypeIdentifiers==9.2 -y || pip install pyobjc-framework-UniformTypeIdentifiers==9.2
conda install pyobjc-framework-UserNotifications==9.2 -y || pip install pyobjc-framework-UserNotifications==9.2
conda install pyobjc-framework-UserNotificationsUI==9.2 -y || pip install pyobjc-framework-UserNotificationsUI==9.2
conda install pyobjc-framework-VideoSubscriberAccount==9.2 -y || pip install pyobjc-framework-VideoSubscriberAccount==9.2
conda install pyobjc-framework-VideoToolbox==9.2 -y || pip install pyobjc-framework-VideoToolbox==9.2
conda install pyobjc-framework-Virtualization==9.2 -y || pip install pyobjc-framework-Virtualization==9.2
conda install pyobjc-framework-Vision==9.2 -y || pip install pyobjc-framework-Vision==9.2
conda install pyobjc-framework-WebKit==9.2 -y || pip install pyobjc-framework-WebKit==9.2
conda install pyOpenSSL @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_38h4axtq38/croot/pyopenssl_1677607699670/work -y || pip install pyOpenSSL @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_38h4axtq38/croot/pyopenssl_1677607699670/work
conda install pyparsing==2.4.7 -y || pip install pyparsing==2.4.7
conda install PyQt5-sip==12.11.0 -y || pip install PyQt5-sip==12.11.0
conda install PySocks @ file:///Users/ktietz/ci_310/pysocks_1643961536721/work -y || pip install PySocks @ file:///Users/ktietz/ci_310/pysocks_1643961536721/work
conda install python-dateutil==2.8.2 -y || pip install python-dateutil==2.8.2
conda install python-dotenv==1.0.0 -y || pip install python-dotenv==1.0.0
conda install python-vlc==3.0.18122 -y || pip install python-vlc==3.0.18122
conda install pytube==15.0.0 -y || pip install pytube==15.0.0
conda install pytube3==9.6.4 -y || pip install pytube3==9.6.4
conda install pytz==2023.3 -y || pip install pytz==2023.3
conda install PyYAML==6.0 -y || pip install PyYAML==6.0
conda install regex==2023.6.3 -y || pip install regex==2023.6.3
conda install requests==2.31.0 -y || pip install requests==2.31.0
conda install requests-oauthlib==1.3.1 -y || pip install requests-oauthlib==1.3.1
conda install requests-toolbelt==1.0.0 -y || pip install requests-toolbelt==1.0.0
conda install roboflow==1.1.2 -y || pip install roboflow==1.1.2
conda install rsa==4.9 -y || pip install rsa==4.9
conda install ruamel.yaml @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_aeh5mqcw49/croot/ruamel.yaml_1666304555976/work -y || pip install ruamel.yaml @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_aeh5mqcw49/croot/ruamel.yaml_1666304555976/work
conda install ruamel.yaml.clib @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_f64xdg2rww/croot/ruamel.yaml.clib_1666302244208/work -y || pip install ruamel.yaml.clib @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_f64xdg2rww/croot/ruamel.yaml.clib_1666302244208/work
conda install s3transfer==0.6.1 -y || pip install s3transfer==0.6.1
conda install safetensors==0.3.1 -y || pip install safetensors==0.3.1
conda install sahi==0.11.14 -y || pip install sahi==0.11.14
conda install scikit-learn==1.3.0 -y || pip install scikit-learn==1.3.0
conda install scipy==1.11.1 -y || pip install scipy==1.11.1
conda install scp==0.14.5 -y || pip install scp==0.14.5
conda install seaborn==0.12.2 -y || pip install seaborn==0.12.2
conda install selenium==4.11.2 -y || pip install selenium==4.11.2
conda install sentence-transformers==2.2.2 -y || pip install sentence-transformers==2.2.2
conda install sentencepiece==0.1.99 -y || pip install sentencepiece==0.1.99
conda install sentry-sdk==1.29.2 -y || pip install sentry-sdk==1.29.2
conda install setproctitle==1.3.2 -y || pip install setproctitle==1.3.2
conda install shapely==2.0.1 -y || pip install shapely==2.0.1
conda install sip @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_fbqiv4bzwo/croots/recipe/sip_1659012372184/work -y || pip install sip @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_fbqiv4bzwo/croots/recipe/sip_1659012372184/work
conda install six @ file:///tmp/build/80754af9/six_1644875935023/work -y || pip install six @ file:///tmp/build/80754af9/six_1644875935023/work
conda install smmap==5.0.0 -y || pip install smmap==5.0.0
conda install sniffio==1.3.0 -y || pip install sniffio==1.3.0
conda install sortedcontainers==2.4.0 -y || pip install sortedcontainers==2.4.0
conda install soupsieve==2.4.1 -y || pip install soupsieve==2.4.1
conda install supervision==0.13.0 -y || pip install supervision==0.13.0
conda install sympy==1.12 -y || pip install sympy==1.12
conda install tensorboard==2.13.0 -y || pip install tensorboard==2.13.0
conda install tensorboard-data-server==0.7.1 -y || pip install tensorboard-data-server==0.7.1
conda install tensorboard-plugin-wit==1.8.1 -y || pip install tensorboard-plugin-wit==1.8.1
conda install tensorflow==2.13.0rc1 -y || pip install tensorflow==2.13.0rc1
conda install tensorflow-addons==0.21.0 -y || pip install tensorflow-addons==0.21.0
conda install tensorflow-estimator==2.13.0rc0 -y || pip install tensorflow-estimator==2.13.0rc0
conda install tensorflow-macos==2.13.0rc1 -y || pip install tensorflow-macos==2.13.0rc1
conda install tensorflow-probability==0.21.0 -y || pip install tensorflow-probability==0.21.0
conda install termcolor==2.3.0 -y || pip install termcolor==2.3.0
conda install terminaltables==3.1.10 -y || pip install terminaltables==3.1.10
conda install thop==0.1.1.post2209072238 -y || pip install thop==0.1.1.post2209072238
conda install threadpoolctl==3.1.0 -y || pip install threadpoolctl==3.1.0
conda install tiktoken==0.4.0 -y || pip install tiktoken==0.4.0
conda install timm==0.9.5 -y || pip install timm==0.9.5
conda install tk==0.1.0 -y || pip install tk==0.1.0
conda install tokenizers==0.13.3 -y || pip install tokenizers==0.13.3
conda install toml @ file:///tmp/build/80754af9/toml_1616166611790/work -y || pip install toml @ file:///tmp/build/80754af9/toml_1616166611790/work
conda install toolz @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_362wyqvvgy/croot/toolz_1667464079070/work -y || pip install toolz @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_362wyqvvgy/croot/toolz_1667464079070/work
conda install torch==2.0.1 -y || pip install torch==2.0.1
conda install torchvision==0.15.2 -y || pip install torchvision==0.15.2
conda install tqdm @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_ac7zic_tin/croot/tqdm_1679561870178/work -y || pip install tqdm @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_ac7zic_tin/croot/tqdm_1679561870178/work
conda install transformers==4.30.2 -y || pip install transformers==4.30.2
conda install trio==0.22.1 -y || pip install trio==0.22.1
conda install trio-websocket==0.10.3 -y || pip install trio-websocket==0.10.3
conda install typeguard==2.13.3 -y || pip install typeguard==2.13.3
conda install typing_extensions==4.5.0 -y || pip install typing_extensions==4.5.0
conda install tzdata==2023.3 -y || pip install tzdata==2023.3
conda install ultralytics==8.0.153 -y || pip install ultralytics==8.0.153
conda install uritemplate==4.1.1 -y || pip install uritemplate==4.1.1
conda install urllib3==1.26.16 -y || pip install urllib3==1.26.16
conda install urllib3-secure-extra==0.1.0 -y || pip install urllib3-secure-extra==0.1.0
conda install uvloop==0.17.0 -y || pip install uvloop==0.17.0
conda install vastai==0.1.7 -y || pip install vastai==0.1.7
conda install wandb==0.15.8 -y || pip install wandb==0.15.8
conda install watchdog==3.0.0 -y || pip install watchdog==3.0.0
conda install websockets==11.0.3 -y || pip install websockets==11.0.3
conda install Werkzeug==2.3.6 -y || pip install Werkzeug==2.3.6
conda install wget==3.2 -y || pip install wget==3.2
conda install wrapt==1.15.0 -y || pip install wrapt==1.15.0
conda install wsproto==1.2.0 -y || pip install wsproto==1.2.0
conda install xxhash==3.3.0 -y || pip install xxhash==3.3.0
conda install yarl==1.9.2 -y || pip install yarl==1.9.2
conda install yolov5==7.0.12 -y || pip install yolov5==7.0.12
conda install youtube-dl @ git+https://github.com/ytdl-org/youtube-dl.git@66ab0814c4baa2dc79c2dd5287bc0ad61a37c5b9 -y || pip install youtube-dl @ git+https://github.com/ytdl-org/youtube-dl.git@66ab0814c4baa2dc79c2dd5287bc0ad61a37c5b9
conda install zope.interface==6.0 -y || pip install zope.interface==6.0
conda install zstandard @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_41b3vxtask/croot/zstandard_1677013668452/work -y || pip install zstandard @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_41b3vxtask/croot/zstandard_1677013668452/work
conda install  -y || pip install 