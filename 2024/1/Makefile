.PHONY: run sample test reinit-ys compile-ys run-ys sample-ys test-ys

run:
	clj -M -m main input/star.in

sample:
	clj -M -m main input/sample.in

test:
	clj -M test/main.clj

reinit-ys:
	cp src/main.clj ys/src/main.clj
	cp test/*.clj ys/test/

compile-ys:
	ys -c ys/src/calc.yml -o ys/src/calc.clj

run-ys: compile-ys
	cd ys && clj -M -m main ../input/star.in && cd ..

sample-ys: compile-ys
	cd ys && clj -M -m main ../input/sample.in && cd ..

test-ys:
	cd ys && clj -M test/main.clj && cd ..
