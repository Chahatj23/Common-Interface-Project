SHELL := /bin/bash

BLOCKDIR := ../blocks/blocks/xcosblocks

SRCFILES := $(sort $(wildcard common/*.py))
SRCFILES += $(sort $(wildcard blocks/*.py))
SRCFILES += $(sort $(wildcard ports/*.py))
SRCFILES += $(sort $(wildcard links/*.py))

TARGET := xcosblocks.py
TARGET2 := $(BLOCKDIR)/$(TARGET)

all : $(TARGET) $(TARGET2)

$(TARGET) : $(SRCFILES)
	@echo Making $@ ...
	@for f in $^; do \
	    echo "# BEGIN $$f"; \
	    echo; \
	    echo; \
	    cat "$$f"; \
	    echo; \
	    echo "# END $$f"; \
	done > $@

flake8 : $(TARGET)
	flake8 --statistics $(TARGET)

.xcosblocks.txt : $(TARGET) parsexcosblocks.awk
	@echo Making $@ ...
	@./parsexcosblocks.awk $(TARGET) > $@

.srcflake8 : $(TARGET) .xcosblocks.txt usexcosblocks.awk
	@echo 'flake8 common/*.py blocks/*.py ports/*.py links/*.py'
	@flake8 $(TARGET) | ./usexcosblocks.awk .xcosblocks.txt -; \
	    exit $${PIPESTATUS[0]}
	touch $@

$(TARGET2) : .srcflake8
	cp -f $(TARGET) $@
