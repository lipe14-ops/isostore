APP_NAME=isostore
APP_DOWNLOAD_DIR=/opt/$APP_NAME

mkdir $APP_DOWNLOAD_DIR

git clone https://github.com/lipe14-ops/isostore $APP_DOWNLOAD_DIR

cat << EOF > $APP_NAME
    #!/usr/bin/sh
    python $APP_DOWNLOAD_DIR/src/main.py
EOF

chmod +x $APP_NAME
mv $APP_NAME /bin