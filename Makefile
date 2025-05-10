# For Windows, run `venv\Scripts\activate` instead of `source venv/bin/activate`

setup:
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt