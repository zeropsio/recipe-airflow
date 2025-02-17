#!/bin/bash

while [ ! -d "/mnt/files" ]; do echo "Waiting for DAGS volume mount..."; sleep 1; done; echo "DAGS volume is ready!"