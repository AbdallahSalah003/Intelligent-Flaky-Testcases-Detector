#!/bin/bash

if [ "$1" = "train" ]; then
    python src/train_model.py
elif [ "$1" = "test" ]; then
    cp /app/X_test.npy ./X_test.npy
    cp /app/y_test.npy ./y_test.npy
    python src/test_model.py
else
    echo "usage: docker run flaky-test-detector [train|test]"
    exit 1
fi
