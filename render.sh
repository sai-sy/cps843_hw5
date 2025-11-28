#!/bin/bash

pandoc report.md -H preamble.tex --from markdown --template=template.latex --pdf-engine=pdflatex -o report.pdf