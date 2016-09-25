#!/bin/bash

acpi | tr -d ' ' | cut -d ',' -f 2
