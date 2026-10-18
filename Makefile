# Open Seamanship build. MODE=release (default) or MODE=preview.
PYTHON ?= python3
MODE ?= release
export MODE
export PYTHONPATH := $(CURDIR)/build

.PHONY: all check site zim test clean private

all: test
	$(PYTHON) -m osp all

check:
	$(PYTHON) -m osp check

site:
	$(PYTHON) -m osp site

zim:
	$(PYTHON) -m osp zim

private:
	$(PYTHON) -m osp private

test:
	$(PYTHON) -m unittest discover -s tests

clean:
	rm -rf dist
