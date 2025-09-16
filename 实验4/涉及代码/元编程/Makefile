paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex

plot-%.png: %.dat plot.py
	python3 plot.py -i $*.dat -o $@

.PHONY: clean all

clean:
	rm -f *.pdf *.aux *.log *.png *.out *.toc
	rm -f *~ .*~

clean-safe:
	mkdir -p Untrack
	rm -f *~ .*~
	git ls-files -o | grep -v '^Untrack/' | xargs -I {} mv {} Untrack/ 2>/dev/null || true

all: paper.pdf

# 查看项目状态
status:
	@echo "=== 未跟踪的文件 ==="
	@git ls-files -o || true
	@echo "=== 已修改的文件 ==="
	@git diff --name-only || true
