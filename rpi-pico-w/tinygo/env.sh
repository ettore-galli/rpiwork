TINYGO_PATH=$(pwd)/tinygo/bin

if [ -f $TINYGO_PATH/tinygo ]; then
    export PATH=$TINYGO_PATH:$PATH
    echo "Tinygo environment: $TINYGO_PATH"
else
    echo "ERROR: $TINYGO_PATH is not a valid tinygo environment"
fi

