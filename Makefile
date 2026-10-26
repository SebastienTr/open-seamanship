# Open Seamanship build. MODE=release (default) or MODE=preview.
PYTHON ?= python3
MODE ?= release
export MODE
export PYTHONPATH := $(CURDIR)/build

.PHONY: all check site zim test clean private sources fetch-library fetch-private dashboard dashboard-image

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

# Dashboard image for N.O.M.A.D. (Supply Depot custom app). DOCKER=docker by default.
DOCKER ?= docker
DASHBOARD_IMAGE ?= open-seamanship-dashboard

dashboard:
	$(PYTHON) -m osp dashboard

dashboard-image: dashboard
	$(DOCKER) build --build-arg OSP_VERSION=$$($(PYTHON) -c 'from osp import config; print(config.build_info().version)') \
	  -t $(DASHBOARD_IMAGE):$$($(PYTHON) -c 'from osp import config; print(config.build_info().version.lstrip("v"))') dist/dashboard

fetch-library:
	$(PYTHON) scripts/fetch_library.py

fetch-private:
	$(PYTHON) scripts/fetch_private.py

sources:
	$(PYTHON) -m osp sources

test:
	$(PYTHON) -m unittest discover -s tests
	@if command -v node >/dev/null 2>&1; then node tests/js/tide_test.js dashboard/dashboard.js; else echo "node not found: dashboard JS tests skipped"; fi

clean:
	rm -rf dist
