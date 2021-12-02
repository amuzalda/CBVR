# CBVR

cd ${PROJECT_FOLDER}

# On root folder run file server to fetch video files
python -m SimpleHTTPServer 3333

# Run python api server
python api.py

# Run Webapp
cd webapp
source ng.sh
ng serve --proxy-config proxyconf.json
