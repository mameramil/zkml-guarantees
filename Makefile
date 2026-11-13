.PHONY: all e1 e2 e3 e4 e5 report

all: e1 e2 e3 e4 e5 report

e1:
	python experiments/e1_binding_cost/run.py

e2:
	python experiments/e2_substitution/e2a.py
	python experiments/e2_substitution/e2b.py
	python experiments/e2_substitution/e2c.py
	python experiments/e2_substitution/e2d.py
	python experiments/e2_substitution/e2e.py

e3:
	python experiments/e3_fidelity/run.py

e4:
	python experiments/e4_determinacy/run.py

e5:
	python experiments/e5_completeness/run.py

report:
	python report/generate_tables.py

clean:
	rm -f results/*.json
