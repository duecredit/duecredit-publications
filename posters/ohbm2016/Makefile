all: anal_script.py.svg demo_script.py.svg duecredit-qr.png

duecredit-qr.png:
	qrencode -s 50 -d 300 -l H -o duecredit-qr.png http://duecredit.org

PYGMENTIZE_FLAGS=-l python -O style=emacs
%.py.tex: %.py; pygmentize -f latex $(PYGMENTIZE_FLAGS) -o $@ $^
%.py.svg: %.py; pygmentize -f svg $(PYGMENTIZE_FLAGS) -o $@ $^
