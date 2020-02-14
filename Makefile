VERSION     = $(shell python -c "import json; v=open('package.json'); print(json.loads(v.read())['version']); v.close()")
PROJECT     = qq_server
REGISTRY	= d.v87.us

build:
	@echo ====================build====================
	python setup.py egg_info --egg-base /tmp sdist

package: build
	@echo ====================package====================
	VERSION=$(VERSION) PROJECT=$(PROJECT) exec ./scripts/package
	docker tag $(PROJECT):$(VERSION) $(REGISTRY)/$(PROJECT):$(VERSION)

test:
	@echo ====================test====================
	VERSION=$(VERSION) PROJECT=$(PROJECT)
	hrun tests --no-html-report --log-level debug

publish: package
	@echo ====================publish====================
	docker push $(REGISTRY)/$(PROJECT):$(VERSION)

clean:
	rm -rf dist
	rm -rf package/${PROJECT}.tar.gz package/requirements.txt package/pip.conf package/main.py

package-clean: clean
	docker images | grep -E "($(PROJECT)\s+)" | awk '{print $$3}' | uniq | xargs -I {} docker rmi --force {}
